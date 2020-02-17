import yaml
import boto3
import ipaddress
import string
import random
import time
import re
import collections
import csv
import os
from datetime import datetime

PARAMETERS_FILE = './parameters.yml'
CFT_POD_FILE = './cisco-hol-pod-cft-template.yml'
# CFT_GLOBAL_FILE = './cisco-hol-global-cft-template.yml'

params = yaml.load(open(PARAMETERS_FILE), Loader=yaml.Loader)


ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

if ACCESS_KEY == None or ACCESS_KEY == '':
    ACCESS_KEY = params['aws_access_key']

if SECRET_KEY == None or SECRET_KEY == '':
    SECRET_KEY = params['aws_secret_key']

REGION = params['aws_region']
VPC_ID = params['vpc_id']
INTERNET_GATEWAY_ID = params['internet_gateway_id']
SUBNET_RANGE_PRIMARY = params['subnet_range_primary']
SUBNET_RANGE_SECONDARY = params['subnet_range_secondary']
STUDENT_COUNT = params['student_count']
STUDENT_PREFIX = params['student_prefix']
# EMAIL_ADDRESS = params['email_address']
# GLOBAL_STACK_NAME = params['global_stack_name']
# PUBLIC_ROUTE_TABLE = ''
# PRIVATE_ROUTE_TABLE = ''

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

STACKS_LIST = []
STUDENTS_LIST = []


def password_generator(size=14, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


#######################################################################
# Verify VPC Id Provided ##############################################
#######################################################################
try:
    print(f'INFO: Checking VPC ID: {VPC_ID}...')
    ec2 = session.resource('ec2')
    vpc = ec2.Vpc(VPC_ID)
    print(f'INFO: VPC ID Verified: {vpc.vpc_id}...')
except:
    print(f'ERROR: VPC Check Failed! Please provide a valid VPC Id...')
    exit(1)
#######################################################################


#######################################################################
# Check Existing Subnets ##############################################
#######################################################################
print(f'INFO: Checking Existing Subnets...')
filters = [{'Name':'vpcId', 'Values':[VPC_ID]}]

ec2 = session.resource('ec2')
subnets_count = len(list(ec2.subnets.filter(Filters=filters)))

if subnets_count > 0:
    print(f'ERROR: {subnets_count} Subnets Found In Current VPC...')
    exit(1)
print(f'INFO: Subnet Check Completed...')
#######################################################################


#######################################################################
# Calculate & Verify Subnet Range #####################################
#######################################################################
try:
    print(f'INFO: Validating Subnet Range...')
    primary_ips = list(ipaddress.ip_network(SUBNET_RANGE_PRIMARY).hosts())
    secondary_ips = list(ipaddress.ip_network(SUBNET_RANGE_SECONDARY).hosts())

    primary_ips = list(set(list(map(lambda ip: str(re.sub(r'([0-9]+)$', '0', str(ip))), primary_ips))))
    secondary_ips = list(set(list(map(lambda ip: str(re.sub(r'([0-9]+)$', '0', str(ip))), secondary_ips))))

    print(f'INFO: {len(primary_ips)} Subnets Are Available...')

    if len(primary_ips) < (STUDENT_COUNT * 2):
        print(f'ERROR: Number Of Required Primary Subnets Are {STUDENT_COUNT * 2} But Only {len(primary_ips)} Are Available...')
        exit(1)
    
    if len(secondary_ips) < STUDENT_COUNT:
        print(f'ERROR: Number Of Required Secondary Subnets Are {STUDENT_COUNT} But Only {len(secondary_ips)} Are Available...')
        exit(1)

except:
    print(f'ERROR: Invalid Subnet! Please provide a valid subnet range...')
    exit(1)
print(f'INFO: Subnet Range Validation Completed...')
#######################################################################


#######################################################################
# Create Student Accounts #############################################
#######################################################################
try:
    print(f'INFO: Creating Student Accounts Collection...')
    primary_ips = list(ipaddress.ip_network(SUBNET_RANGE_PRIMARY).hosts())
    secondary_ips = list(ipaddress.ip_network(SUBNET_RANGE_SECONDARY).hosts())

    primary_ips = list(collections.OrderedDict.fromkeys(list(map(lambda ip: str(re.sub(r'([0-9]+)$', '0', str(ip))), primary_ips))))
    secondary_ips = list(collections.OrderedDict.fromkeys(list(map(lambda ip: str(re.sub(r'([0-9]+)$', '0', str(ip))), secondary_ips))))

    public_subnet_01 = primary_ips[:len(primary_ips)//2]
    public_subnet_02 = primary_ips[len(primary_ips)//2:]

    for i in range(STUDENT_COUNT):
        STUDENTS_LIST.append({
            'account_name': f'{STUDENT_PREFIX}-0{i}',
            'account_password': password_generator(),
            'public_subnet_01': f'{public_subnet_01[i]}',
            'public_subnet_02': f'{public_subnet_02[i]}',
            'private_subnet': f'{secondary_ips[i]}',
            'eks_dns': ''
        })

    print(f'INFO: {STUDENTS_LIST}')

except:
    print(f'ERROR: Invalid Subnet! Please provide a valid subnet range...')
    exit(1)
print(f'INFO: Student Accounts Collection Created...')
#######################################################################


#######################################################################
# Run Global Cloud Formation ##########################################
#######################################################################
# try:
#     print(f'INFO: Initialize Global CloudFormation...')

#     cloudformation = session.client('cloudformation')
#     cloudformation_template = open(CFT_GLOBAL_FILE, 'r').read()

#     aws_parameters = [
#         {'ParameterKey': 'VpcIdParameter', 'ParameterValue': VPC_ID},
#         {'ParameterKey': 'RegionParameter', 'ParameterValue': REGION}
#     ]

#     print(aws_parameters)

#     result = cloudformation.create_stack(
#         StackName=GLOBAL_STACK_NAME,
#         TemplateBody=cloudformation_template,
#         Parameters=aws_parameters,
#         Capabilities=[
#             'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM',
#         ]
#     )

#     print(f'INFO: Gobal Stack Creation In Progress...')

# except Exception as e:
#     print(e)
#     exit(1)
#######################################################################


#######################################################################
# Wait For Global Stack Creation ######################################
#######################################################################
# is_completed = False
# while not is_completed:

#     try:

#         cloudformation = session.client('cloudformation')

#         status = cloudformation.describe_stacks(
#             StackName=GLOBAL_STACK_NAME
#         )

#         if status['Stacks'][0]['StackStatus'] == 'CREATE_COMPLETE':

#             public_rt = next(filter(lambda x: x['OutputKey'] == 'PublicRouteTable', status['Stacks'][0]['Outputs']), None)
#             private_rt = next(filter(lambda x: x['OutputKey'] == 'PrivateRouteTable', status['Stacks'][0]['Outputs']), None)
            
#             # Set Global Route Table Ids
#             PUBLIC_ROUTE_TABLE = public_rt['OutputValue']
#             PRIVATE_ROUTE_TABLE = private_rt['OutputValue']

#             is_completed = True
#             break

#         if status['Stacks'][0]['StackStatus'] == 'ROLLBACK_IN_PROGRESS' or  status['Stacks'][0]['StackStatus'] == 'ROLLBACK_COMPLETE':
#             print(f'INFO: Stack Failed: {GLOBAL_STACK_NAME}')
#             exit(1)

#         print(f"INFO: StackName: {GLOBAL_STACK_NAME}, Status: {status['Stacks'][0]['StackStatus']}")

#         time.sleep(10)

#     except Exception as e:
#         print(e)
#         exit(1)
#######################################################################


#######################################################################
# Run POD Cloud Formation #############################################
#######################################################################
for student in STUDENTS_LIST:

    try:

        cloudformation = session.client('cloudformation')
        cloudformation_template = open(CFT_POD_FILE, 'r').read()

        aws_parameters = [
            {'ParameterKey': 'AccessKey', 'ParameterValue': ACCESS_KEY},
            {'ParameterKey': 'SecretKey', 'ParameterValue': SECRET_KEY},

            {'ParameterKey': 'StudentIndex', 'ParameterValue': str(STUDENTS_LIST.index(student))},
            {'ParameterKey': 'StudentName', 'ParameterValue': student['account_name']},
            {'ParameterKey': 'StudentPassword', 'ParameterValue': student['account_password']},
            {'ParameterKey': 'VpcID', 'ParameterValue': VPC_ID},
            {'ParameterKey': 'InternetGatewayId', 'ParameterValue': INTERNET_GATEWAY_ID},
            {'ParameterKey': 'Subnet01CidrBlock', 'ParameterValue': f"{student['public_subnet_01']}/24"},
            {'ParameterKey': 'Subnet02CidrBlock', 'ParameterValue': f"{student['public_subnet_02']}/24"},
            {'ParameterKey': 'Subnet03CidrBlock', 'ParameterValue': f"{student['private_subnet']}/24"},

            {'ParameterKey': 'ASAvInsideSubnet', 'ParameterValue': student['public_subnet_01']},
            {'ParameterKey': 'ASAvOutsideSubnet', 'ParameterValue': student['private_subnet']},

            {'ParameterKey': 'Region', 'ParameterValue': REGION},
            {'ParameterKey': 'Subnet01AvailabilityZone', 'ParameterValue': 'a'},
            {'ParameterKey': 'Subnet02AvailabilityZone', 'ParameterValue': 'b'},
            {'ParameterKey': 'Subnet03AvailabilityZone', 'ParameterValue': 'a'},

            {'ParameterKey': 'ASAvImageID', 'ParameterValue': params['asav_ami']},
            {'ParameterKey': 'LDAPImageID', 'ParameterValue': params['ldap_ami']},
            {'ParameterKey': 'MSSCImageID', 'ParameterValue': params['mssc_ami']},
            {'ParameterKey': 'MSSQLImageID', 'ParameterValue': params['mssql_ami']},
            {'ParameterKey': 'IISImageID', 'ParameterValue': params['iis_ami']},
            {'ParameterKey': 'MySQLImageID', 'ParameterValue': params['mysql_ami']},
            {'ParameterKey': 'ApacheImageID', 'ParameterValue': params['apache_ami']},
            {'ParameterKey': 'AnsibleImageID', 'ParameterValue': params['ansible_ami']},
            {'ParameterKey': 'TetrationDataIngestImageID', 'ParameterValue': params['tet_data_ami']},
            {'ParameterKey': 'TetrationEdgeImageID', 'ParameterValue': params['tet_edge_ami']},
            {'ParameterKey': 'Win10UserImageID', 'ParameterValue': params['user_ami']},
            {'ParameterKey': 'Win10DBAImageID', 'ParameterValue': params['dba_ami']},
            {'ParameterKey': 'AttackerImageID', 'ParameterValue': params['attack_server_ami']},
            {'ParameterKey': 'GuacamoleImageID', 'ParameterValue': params['guacamole_ami']},
            {'ParameterKey': 'EKSWorkerImageID', 'ParameterValue': params['eks_worker_ami']}
        ]

        print('INFO:', aws_parameters)

        result = cloudformation.create_stack(
            StackName=student['account_name'],
            TemplateBody=cloudformation_template,
            Parameters=aws_parameters,
            Capabilities=[
                'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM',
            ]
        )

        STACKS_LIST.append(student['account_name'])

    except Exception as e:
        print(e)
        exit(1)
#######################################################################

#######################################################################
# Wait For Stack Creation #############################################
#######################################################################
completed_stacks = []
while True:

    try:

        for stack_name in STACKS_LIST:

            if stack_name in completed_stacks:
                continue

            cloudformation = session.client('cloudformation')

            status = cloudformation.describe_stacks(
                StackName=stack_name
            )

            if status['Stacks'][0]['StackStatus'] == 'CREATE_COMPLETE':
                completed_stacks.append(stack_name)

            if status['Stacks'][0]['StackStatus'] == 'ROLLBACK_IN_PROGRESS' or  status['Stacks'][0]['StackStatus'] == 'ROLLBACK_COMPLETE':
                print(f"ERROR: Stack Failed => {stack_name}")
                print('ERROR: Unable To Complete CloudFormation Deployment.')
                exit(1)

            print(f"INFO: StackName: {stack_name}, Status: {status['Stacks'][0]['StackStatus']}")

        if len(STACKS_LIST) == len(completed_stacks):
            print('INFO: CloudFormation Completed Successfully...')
            break

        time.sleep(10)

    except Exception as e:
        print(e)
        exit(1)
#######################################################################

#######################################################################
# Assemble EKS ELB DNS Records ########################################
#######################################################################

# try:

#     print('INFO: Initializing EKS DNS Assembly...')

#     time.sleep(15)

#     for student in STUDENTS_LIST:

#         client = boto3.client('elb')

#         eks_elbs = client.describe_load_balancers()['LoadBalancerDescriptions']

#         elb_tags = client.describe_tags(
#             LoadBalancerNames=list(map(lambda e: e['LoadBalancerName'], eks_elbs))
#         )

#         for elb in elb_tags['TagDescriptions']:
#             for tag in elb['Tags']:
#                 if tag['Key'] == 'Account' and tag['Value'] == student['account_name']:
#                     student['eks_dns'] = list(filter(lambda e: e['LoadBalancerName'] == elb['LoadBalancerName'], eks_elbs))[0]['DNSName']
#                     break
    
#     print('INFO: EKS DNS Assembly Completed...')

# except Exception as e:
#     print(e)
#     exit(1)

#######################################################################

#######################################################################
# Generate CSV Reports ################################################
#######################################################################

try:

    records = []

    for stack_name in STACKS_LIST:

        print(f"INFO: StackName: {stack_name}, Status: Generating CSV Report...")

        cloudformation = session.client('cloudformation')

        stack = cloudformation.describe_stacks(
            StackName=stack_name
        )

        output = {}

        for o in stack['Stacks'][0]['Outputs']:
            output[o['OutputKey']] = o['OutputValue']

        records.append([
            output['CiscoHOLStudentName'],
            output['CiscoHOLStudentPassword'],
            f"https://{output['CiscoHOLGuacamolePublic']}",
            output['CiscoHOLApachePrivate'],
            output['CiscoHOLApachePublic'],
            output['CiscoHOLIISPrivate'],
            output['CiscoHOLIISPublic'],
            output['CiscoHOLMySql'],
            output['CiscoHOLMSSQL'],
            output['EKSClusterEndpoint'],
            output['CiscoHOLAnsible'],
            output['CiscoHOLTetrationEdge'],
            output['CiscoHOLTetrationData'],
            output['CiscoHOLASAv'],
            output['CiscoHOLAttacker'],
            output['CiscoHOLWin10User'],
            output['CiscoHOLWin10DBA'],
        ])

    header = [
        'Account', 
        'Password', 
        'Web Console URL',
        'Apache OpenCart',
        'Apache OpenCart Public',
        'IIS nopCommerce',
        'IIS nopCommerce Public',
        'MySQL',
        'MSSQL',
        'EKS Clsuter',
        'Ansible',
        'Tetration Edge',
        'Tetration Data',
        'ASAv',
        'Metasploit',
        'Employee',
        'SysAdmin'
    ]

    filename = 'reports/' + datetime.today().strftime('%H-%M-%S %Y-%m-%d') + '-report.csv'

    if not os.path.exists('reports'):
        os.makedirs('reports')

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(records)

except Exception as e:
    print(e)
    exit(1)

#######################################################################


print('Exiting! All The Tasks Are Completed Successfully...')
exit(0)
