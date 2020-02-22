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
import json
import urllib
from datetime import datetime

PARAMETERS_FILE = './parameters.yml'
CFT_POD_FILE = './cisco-hol-pod-cft-template.yml'

params = yaml.load(open(PARAMETERS_FILE), Loader=yaml.Loader)


ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

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

S3_BUCKET = params['s3_bucket']

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

MANAGEMENT_CIDR = ''

STACKS_LIST = []
STUDENTS_LIST = []

def password_generator(size=14, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_public_ip():
    result = json.load(urllib.request.urlopen('https://api.ipify.org/?format=json'))
    return result['ip']


#######################################################################
# Get Management Cidr Block ###########################################
#######################################################################
try:
    print(f'INFO: Fetching Public IP Of The Orchestrator...')
    MANAGEMENT_CIDR = f"{get_public_ip()}/32"
    print('INFO: Management Cidr:', MANAGEMENT_CIDR)
except:
    print(f'ERROR: Unable To Assemble Management Cidr')
    exit(1)
#######################################################################


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
# Upload CFT TO S3 Bucket #############################################
#######################################################################
print('INFO: Uploading Template To S3...')
s3 = boto3.resource('s3')
s3.meta.client.upload_file('cisco-hol-pod-cft-template.yml', S3_BUCKET, 'cisco-hol-pod-cft-template.yml')
print('INFO: CFT Template Uploaded To S3...')
#######################################################################

#######################################################################
# Run POD Cloud Formation #############################################
#######################################################################
for student in STUDENTS_LIST:

    try:

        outside_pod_ips = list(ipaddress.ip_network(f"{student['private_subnet']}/24").hosts())

        cloudformation = session.client('cloudformation')
        cloudformation_template = open(CFT_POD_FILE, 'r').read()

        aws_parameters = [
            {'ParameterKey': 'AccessKey', 'ParameterValue': ACCESS_KEY},
            {'ParameterKey': 'SecretKey', 'ParameterValue': SECRET_KEY},

            {'ParameterKey': 'StudentIndex', 'ParameterValue': str(STUDENTS_LIST.index(student))},
            {'ParameterKey': 'StudentName', 'ParameterValue': student['account_name']},
            {'ParameterKey': 'StudentPassword', 'ParameterValue': student['account_password']},
            {'ParameterKey': 'ManagementCidrBlock', 'ParameterValue': MANAGEMENT_CIDR},

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

            {'ParameterKey': 'Win10EmployeePrivateIp', 'ParameterValue': str(outside_pod_ips[11])},
            {'ParameterKey': 'Win10SysAdminPrivateIp', 'ParameterValue': str(outside_pod_ips[12])},
            {'ParameterKey': 'AttackerPrivateIp', 'ParameterValue': str(outside_pod_ips[13])},
            {'ParameterKey': 'IISOutsidePrivateIp', 'ParameterValue': str(outside_pod_ips[14])},
            {'ParameterKey': 'ApacheOutsidePrivateIp', 'ParameterValue': str(outside_pod_ips[15])},
            {'ParameterKey': 'ASAvOutsidePrivateIp01', 'ParameterValue': str(outside_pod_ips[16])},
            {'ParameterKey': 'ASAvOutsidePrivateIp02', 'ParameterValue': str(outside_pod_ips[17])},

            {'ParameterKey': 'ASAvImageID', 'ParameterValue': params['asav_ami']},
            {'ParameterKey': 'LDAPImageID', 'ParameterValue': params['ldap_ami']},
            {'ParameterKey': 'MSSQLImageID', 'ParameterValue': params['mssql_ami']},
            {'ParameterKey': 'IISImageID', 'ParameterValue': params['iis_ami']},
            {'ParameterKey': 'MySQLImageID', 'ParameterValue': params['mysql_ami']},
            {'ParameterKey': 'ApacheImageID', 'ParameterValue': params['apache_ami']},
            {'ParameterKey': 'AnsibleImageID', 'ParameterValue': params['ansible_ami']},
            {'ParameterKey': 'TetrationDataIngestImageID', 'ParameterValue': params['tet_data_ami']},
            {'ParameterKey': 'TetrationEdgeImageID', 'ParameterValue': params['tet_edge_ami']},
            {'ParameterKey': 'Win10EmployeeImageID', 'ParameterValue': params['employee_ami']},
            {'ParameterKey': 'Win10SysAdminImageID', 'ParameterValue': params['sysadmin_ami']},
            {'ParameterKey': 'AttackerImageID', 'ParameterValue': params['attack_server_ami']},
            {'ParameterKey': 'GuacamoleImageID', 'ParameterValue': params['guacamole_ami']},
            {'ParameterKey': 'EKSWorkerImageID', 'ParameterValue': params['eks_worker_ami']}
        ]

        print('INFO:', aws_parameters)

        result = cloudformation.create_stack(
            StackName=student['account_name'],
            # TemplateBody=cloudformation_template,
            TemplateURL=f"https://{S3_BUCKET}.s3.us-east-2.amazonaws.com/cisco-hol-pod-cft-template.yml",
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
try:

    print('INFO: Initializing EKS DNS Assembly...')

    time.sleep(120)

    for student in STUDENTS_LIST:

        client = session.client('elb')

        eks_elbs = client.describe_load_balancers()['LoadBalancerDescriptions']

        elb_tags = client.describe_tags(
            LoadBalancerNames=list(map(lambda e: e['LoadBalancerName'], eks_elbs))
        )

        for elb in elb_tags['TagDescriptions']:
            for tag in elb['Tags']:
                for key in tag:
                    if student['account_name'] in tag[key]:
                        student['eks_dns'] = list(filter(lambda e: e['LoadBalancerName'] == elb['LoadBalancerName'], eks_elbs))[0]['DNSName']
                        break
    

    print('INFO: EKS DNS Assembly Completed...')

except Exception as e:
    print(e)
    exit(1)
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

        student = list(filter(lambda student: student['account_name'] == stack_name, STUDENTS_LIST))[0]

        output = {}

        for o in stack['Stacks'][0]['Outputs']:
            output[o['OutputKey']] = o['OutputValue']

        records.append([
            output['CiscoHOLAWSRegion'],
            output['StudentAccessKey'],
            output['StudentSecretKey'],
            output['CiscoHOLStudentName'],
            output['CiscoHOLStudentPassword'],
            f"https://{output['CiscoHOLGuacamolePublic']}",
            output['CiscoHOLPublicSubnet01'],
            output['CiscoHOLPrivateSubnet'],
            output['CiscoHOLActiveDirectory'],
            output['CiscoHOLIISPublic'],
            output['CiscoHOLIISPrivate'],
            output['CiscoHOLIISOutsidePrivate'],
            output['CiscoHOLMSSQL'],
            output['CiscoHOLApachePublic'],
            output['CiscoHOLApachePrivate'],
            output['CiscoHOLApacheOutsidePrivate'],
            output['CiscoHOLMySql'],
            f"http://{student['eks_dns']}",
            output['EKSClusterCertificate'],
            output['CiscoHOLAnsible'],
            output['CiscoHOLTetrationEdge'],
            output['TetNetworkInterfaces01Data'],
            output['TetNetworkInterfaces02Data'],
            output['TetNetworkInterfaces03Data'],
            output['CiscoHOLASAvPrivate03'],
            output['CiscoHOLASAvPrivate02'],
            output['CiscoHOLASAvPrivate01'],
            output['CiscoHOLAttacker'],
            output['CiscoHOLWin10Employee'],
            output['CiscoHOLWin10SysAdmin'],
        ])

    header = [
        'AWS Region',
        'Student AWS EC2 RO Access Key',
        'Student AWS EC2 RO Secret Key',
        'Student Guacamole Username',
        'Student Guacamole Password', 
        'Guacamole Web Console URL',
        'Student Internal/Inside Corporate Subnet',
        'Student External/Outside Psuedo Internet Subnet',
        'MS Active Directory IP',
        'MS IIS nopCommerce Public IP',
        'MS IIS nopCommerce Inside IP',
        'MS IIS nopCommerce Outside IP',
        'MS SQL Private IP',
        'Apache OpenCart Public IP',
        'Apache OpenCart Inside IP',
        'Apache OpenCart Outside IP',
        'MySQL Private IP',
        'EKS SockShop Public URL (Use for Tetration External Orchestrator)',
        'EKS Cluster Cert (15 min cert?)',
        'Ansible IP',
        'Tetration Edge IP',
        'Tetration Data Ingest IP 1',
        'Tetration Data Ingest IP 2',
        'Tetration Data Ingest IP 3',
        'ASAv Inside IP',
        'ASAv Outside IP',
        'ASAv Management IP',
        'Metasploit Attacker IP',
        'Employee IP',
        'SysAdmin IP'
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
