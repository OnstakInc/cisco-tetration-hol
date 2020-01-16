import yaml
import boto3
import ipaddress
import string
import random
import time

PARAMETERS_FILE = './parameters.yml'
CFT_POD_FILE = './cisco-hol-pod-cft-template.yml'
CFT_GLOBAL_FILE = './cisco-hol-global-cft-template.yml'

params = yaml.load(open(PARAMETERS_FILE))

ACCESS_KEY = params['aws_access_key']
SECRET_KEY = params['aws_secret_key']
REGION = params['aws_region']
ZONE = params['availability_zone']
VPC_ID = params['aws_vpc_id']
SUBNET_RANGE = params['aws_subnet_range']
STUDENT_COUNT = params['student_count']
STUDENT_PREFIX = params['student_prefix']
EMAIL_ADDRESS = params['email_address']
GLOBAL_STACK_NAME = params['global_stack_name']
PUBLIC_ROUTE_TABLE = ''
PRIVATE_ROUTE_TABLE = ''

# TODO - Uncomment In Final Release
session = boto3.Session(
    # aws_access_key_id=ACCESS_KEY,
    # aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

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
    ips = list(ipaddress.ip_network(SUBNET_RANGE).hosts())

    print(f'INFO: {len(ips)} IP Addresses Are Available...')

    if len(ips) < (STUDENT_COUNT * 2):
        print(f'ERROR: Number Of Required IP Addresses Are {STUDENT_COUNT * 2} But Only {len(ips)} Are Available...')
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
    ips = list(ipaddress.ip_network(SUBNET_RANGE).hosts())

    private_subnet = ips[:len(ips)//2]
    public_subnet = ips[len(ips)//2:]

    for i in range(STUDENT_COUNT):
        STUDENTS_LIST.append({
            'account_name': f'{STUDENT_PREFIX}_0{i}',
            'account_password': password_generator(),
            'public_subnet': f'{public_subnet[i]}/24',
            'private_subnet': f'{private_subnet[i]}/24'
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
try:
    print(f'INFO: Initialize Global CloudFormation...')

    cloudformation = session.client('cloudformation')
    cloudformation_template = open(CFT_GLOBAL_FILE, 'r').read()

    aws_parameters = [
        {'ParameterKey': 'VpcIdParameter', 'ParameterValue': VPC_ID},
        {'ParameterKey': 'RegionParameter', 'ParameterValue': REGION}
    ]

    print(aws_parameters)

    result = cloudformation.create_stack(
        StackName=GLOBAL_STACK_NAME,
        TemplateBody=cloudformation_template,
        Parameters=aws_parameters,
        Capabilities=[
            'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM',
        ]
    )

    print(f'INFO: Gobal Stack Creation In Progress...')

except Exception as e:
    print(e)
    exit(1)
#######################################################################


#######################################################################
# Wait For Global Stack Creation ######################################
#######################################################################
is_completed = False
while not is_completed:

    try:

        cloudformation = session.client('cloudformation')

        status = cloudformation.describe_stacks(
            StackName=GLOBAL_STACK_NAME
        )

        if status['Stacks'][0]['StackStatus'] == 'CREATE_COMPLETE':

            public_rt = next(filter(lambda x: x['OutputKey'] == 'PublicRouteTable', status['Stacks'][0]['Outputs']), None)
            private_rt = next(filter(lambda x: x['OutputKey'] == 'PrivateRouteTable', status['Stacks'][0]['Outputs']), None)
            
            # Set Global Route Table Ids
            PUBLIC_ROUTE_TABLE = public_rt['OutputValue']
            PRIVATE_ROUTE_TABLE = private_rt['OutputValue']

            is_completed = True
            break

        if status['Stacks'][0]['StackStatus'] == 'ROLLBACK_IN_PROGRESS' or  status['Stacks'][0]['StackStatus'] == 'ROLLBACK_COMPLETE':
            print(f'INFO: Stack Failed: {GLOBAL_STACK_NAME}')
            exit(1)

        print(f"INFO: StackName: {GLOBAL_STACK_NAME}, Status: {status['Stacks'][0]['StackStatus']}")

        time.sleep(10)

    except Exception as e:
        print(e)
        exit(1)
#######################################################################


#######################################################################
# Run POD Cloud Formation #############################################
#######################################################################
for student in STUDENTS_LIST:

    try:

        cloudformation = session.client('cloudformation')
        cloudformation_template = open(CFT_POD_FILE, 'r').read()

        aws_parameters = [
            {'ParameterKey': 'StudentName', 'ParameterValue': student['account_name']},
            {'ParameterKey': 'StudentPassword', 'ParameterValue': student['account_password']},
            {'ParameterKey': 'VpcId', 'ParameterValue': VPC_ID},
            {'ParameterKey': 'PublicRouteTableId', 'ParameterValue': PUBLIC_ROUTE_TABLE},
            {'ParameterKey': 'PrivateRouteTableId', 'ParameterValue': PRIVATE_ROUTE_TABLE},
            {'ParameterKey': 'SubnetPrivateCidrBlock', 'ParameterValue': student['private_subnet']},
            {'ParameterKey': 'SubnetPublicCidrBlock', 'ParameterValue': student['public_subnet']},
            {'ParameterKey': 'Region', 'ParameterValue': REGION},
            {'ParameterKey': 'SubnetPrivateAvailabilityZone', 'ParameterValue': ZONE},
            {'ParameterKey': 'SubnetPublicAvailabilityZone', 'ParameterValue': ZONE}
        ]

        print(aws_parameters)

        result = cloudformation.create_stack(
            StackName=student['account_name'],
            TemplateBody=cloudformation_template,
            Parameters=aws_parameters,
            Capabilities=[
                'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM',
            ]
        )

    except Exception as e:
        print(e)
        exit(1)
#######################################################################