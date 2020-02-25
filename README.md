# Cisco Tetration - Hands On Lab
  
[Lab Guide Documentation](https://onstakinc.github.io/cisco-tetration-hol/labguide/)

## Lab Environment Deployment and Git Repo Usage

This lab environment deploys entirely to AWS with the current unique exception of Cisco ISE, which requires deployment to an on-prem vCenter environment with a VPN connection and route table addition. 


#### Files required to deploy to AWS

Deployment of the environment for lab pod(s) requires the use of three files - namely: `parameters.yml`, `cisco-hol-pod-cft-template.yml`, and `launch.py`. 


`launch.py` reads in the parameters unique to each deployment set from `parameters.yml`, then executes one entire deployment of `cisco-hol-pod-cft-template.yml` per number of `student_count` found in `parameters.yml`. Student count begins with `00` and thus we recommend designating the first pod for the lab admin/instructor as a pristene deployment for use in demoing or troubleshooting any issues an actual student might for some reason encounter, and allowing the first student to be the second pod, which would begin with the numbering `01`. 


#### Parameters File Example

Below is an example of a `parameters.yml` file, however with additional inline commented markup, which can also be found in the directory `parameters-templates` under the name `parameters-example.yml`. The inline comments should be fairly self-explanatory. 


```
---
# Prefer using Env Vars to set AWS Access & Secret Keys named as such:
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY 
aws_access_key: 
aws_secret_key: 
aws_region: us-east-2   # << This is the region where you will deploy the lab pods to. Currently only one deployment set per region is supported.

student_count: 1   # << Number of pods to deploy. First pod starts with 00, so recommendation is to deploy 1 more pod than needed and use first for admin/instructor pod
student_prefix: cisco-student 

vpc_id: vpc-017dd7e8fc4a4b9de   # << This is your existing VPC in the above-mentioned AWS region where you will deploy the lab pods to
internet_gateway_id: igw-0dbfdfc228666cee0   # << This IGW needs to exist already in the above VPC
subnet_range_primary: 10.0.0.0/16   # << This will be the "Internal" subnet (inside the ASA FW) for most workloads, including apps
subnet_range_secondary: 198.18.0.0/16   # << This will be the "Internet" subnet (outside the ASA FW) for users and attacker

s3_bucket: 'tetration-hol-cft-template'   # << S3 Bucket is global DNS unique name - change to any arbitrary desired non-overlapping name

ise_server_ip: '172.16.171.49'   # << This is your own private on-prem ISE instance - needs VPN with AWS VGW

asav_ami: ami-0f3cca6491d987102   # << This is the ASAv, is a region-specific image ID, and requires a subscription from AWS Marketplace (search for ASAv BYOL)
ldap_ami: ami-0b416df717b448667   # << This is for MS Active Directory and is a private image that requires a simple copy
mssql_ami: ami-09782396834215732   # << This is for MS Win19 SQL and is a private image that requires a simple copy
iis_ami: ami-091df3f67b36e2250   # << This is for MS Win19 IIS and is a private image that requires a simple copy
mysql_ami: ami-051ba5822fc02da4b   # <<  This is for CentOS7 MySQL and is a private image that requires Lanuch, you to Accept Subscription, then create the AMI
apache_ami: ami-0c85d8851d66cd9f9   # <<  This is for CentOS7 Apache and is a private image that requires Lanuch, you to Accept Subscription, then create the AMI
ansible_ami: ami-0083b10a007c92d2d   # << This is for CentOS7 Ansible and is a private image that requires Lanuch, you to Accept Subscription, then create the AMI
tet_data_ami: ami-0cf7fd4e75d7d91ab   # << This is the Tetration Data Ingest appliance and is a private image that requires a simple copy
tet_edge_ami: ami-05d08946ffda72d18   # << This is the Tetration Edge appliance and is a private image that requires a simple copy
employee_ami: ami-032ca0586c1a78e1d   # << This is the Win10 image for both Employee and SysAdmin and is a private image that requires a simple copy, however due to licensing reboots every hour - will likely be removed
sysadmin_ami: ami-032ca0586c1a78e1d   # << Simple AMI copy but most likely remove
employee_ubuntu_ami: ami-0af925e340025c9f9   # << This is the Ubuntu 18.04 desktop image for both Employee and SysAdmin and is a private image that requires a simple copy
sysadmin_ubuntu_ami: ami-0af925e340025c9f9   # << Simple AMI copy 
attack_server_ami: ami-04f958d48e22e185c   # << This is for Ubuntu Kali Linux with Metasploit and is a private image that requires Lanuch, you to Accept Subscription, then create the AMI
guacamole_ami: ami-007f96a1ed0595540   # << This is for CentOS7 Guacamole and is a private image that requires Lanuch, you to Accept Subscription, then create the AMI
eks_worker_ami: ami-0c4c60006aa81c29b   # << Global AWS Marketplace - will change with region - https://cloud-images.ubuntu.com/docs/aws/eks/

```

#### Dependancies

`launch.py` requires Python 3.7 as well as a number of dependancies that one can easily see with the first few `import` statements in the script.

It is important to note that prior to running `launch.py`, you must have a few things already created in your AWS environment - namely a VPC, an IGW, and a S3 bucket.
1. VPC: This probably goes without saying, but we recommend a non-default VPC. Place your VPC ID in `parameters.yml` in the `vpc_id:` line (no quotes surounding the value). This VPC must have at least two CIDR blocks, one for `subnet_range_primary` and one for `subnet_range_secondary`. It is important that **no** subnets be created in this VPC whatsoever, else the script will error out. `launch.py` will create the subnets and we have a brief discussion about them below. 
2. IGW: You must have one IGW created in your `vpc_id` and designated in the `parameters.yml` in the `internet_gateway_id:` lin (no quotes surounding the value).
3. S3 Bucket: Due to the size of the CFT, AWS requires that we first upload it to an S3 bucket prior to calling it and executing against it. It is required that you have already created the empty S3 bucket and placed the name of the bucket in the `parameters.yml` in the `internet_gateway_id:` lin (no quotes surounding the value).

#### Subnets

A quick discussion on subnets to be created at launch time is in order. This VPC must have at least two CIDR blocks, one for `subnet_range_primary` and one for `subnet_range_secondary`. Due to AWS strict requirement that there be at least two subnets available in order to spin up an EKS cluster, there will be two subnets created in `subnet_range_primary` per student. Say you chose `10.0.0.0

#### IAM Role API Credentials - Scope and Permissions

The AWS API Access key and Secret key used to deploy is preferred to be stored in the local OS environment variables, vs in the `parameters.yml` file, and the same is mentioned at the top of that file in the comments. The en environment variables should be labeled as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, respectively. If this is necessary to change, these variable names must be updated in the `launch.py` script to match your local env var names. 

The AWS credentials used need to have permissions that allow them to create, update, and delete the following:
(aws global)
* S3 bucket (for vpc flow logs)
* IAM role (for EKS)
* IAM User and API Keys with RO access to EC2 & ELB (for student external orchestrators) (this still needs tightening and S3 flow log access)

(region specific)
* Lambda functions
* CloudWatch events for Lambda
* EKS Cluster and Node Group

(vpc specific)
* Route Tables
* Subnets
* Security Groups
* EC2 instances (12 or 14 per student/pod - depending on Win10 decision)
* ELB

#### Deploying to AWS

Assuming you've filled out your desired values in `parameters.yml`, it's time to deploy. Change directory to the `cisco-tetration-hol` directory and run python to launch (the below assumes `python` aliases to `python3` or `python3.7`).

```
cd /<relative-path>/cisco-tetration-hol
python launch.py
```

Assuming all went well and creds are allowing enough, you should have output similar to the following:

```
INFO: Fetching Public IP Of The Orchestrator...
INFO: Management Cidr: 172.116.159.56/32
INFO: Checking VPC ID: vpc-082d43bff04cd342e...
INFO: VPC ID Verified: vpc-082d43bff04cd342e...
INFO: Checking Existing Subnets...
INFO: Subnet Check Completed...
INFO: Checking Available Elastic IPs...
INFO: Created Available Elastic IPs Collection...
INFO: Validating Subnet Range...
INFO: 256 Subnets Are Available...
INFO: Subnet Range Validation Completed...
INFO: Creating Student Accounts Collection...
INFO: [{'account_name': 'cisco-student-00', 'account_password': '8AetfFvCbUiKue', 'public_subnet_01': '10.1.0.0', 'public_subnet_02': '10.1.128.0', 'private_subnet': '198.18.0.0', 'eks_dns': '', 'guacamole_elastic_ip': '3.134.26.220', 'guacamole_elastic_ip_allocation_id': 'eipalloc-00ff1ef8b0c8562ad', 'tet_data_elastic_ip': '3.20.190.112', 'tet_data_elastic_ip_allocation_id': 'eipalloc-025e2db995a9b3751'}]
INFO: Student Accounts Collection Created...
You are about to deploy 1 student pod(s) to vpc-082d43bff04cd342e in the us-east-2 Region
Are you sure you wish to proceed with this deployment (y/Y to continue)? y
INFO: Uploading Template To S3...
INFO: CFT Template Uploaded To S3...
INFO: [{'ParameterKey': 'AccessKey', 'ParameterValue': '<REDACTED>'}, {'ParameterKey': 'SecretKey', 'ParameterValue': '<REDACTED>'}, {'ParameterKey': 'StudentIndex', 'ParameterValue': '0'}, {'ParameterKey': 'StudentName', 'ParameterValue': 'cisco-student-00'}, {'ParameterKey': 'StudentPassword', 'ParameterValue': '8AetfFvCbUiKue'}, {'ParameterKey': 'ManagementCidrBlock', 'ParameterValue': '172.116.159.56/32'}, {'ParameterKey': 'VpcID', 'ParameterValue': 'vpc-082d43bff04cd342e'}, {'ParameterKey': 'InternetGatewayId', 'ParameterValue': 'igw-0fec2ea47e798ea86'}, {'ParameterKey': 'Subnet01CidrBlock', 'ParameterValue': '10.1.0.0/24'}, {'ParameterKey': 'Subnet02CidrBlock', 'ParameterValue': '10.1.128.0/24'}, {'ParameterKey': 'Subnet03CidrBlock', 'ParameterValue': '198.18.0.0/24'}, {'ParameterKey': 'ASAvInsideSubnet', 'ParameterValue': '10.1.0.0'}, {'ParameterKey': 'ASAvOutsideSubnet', 'ParameterValue': '198.18.0.0'}, {'ParameterKey': 'GuacamoleElasticIp', 'ParameterValue': '3.134.26.220'}, {'ParameterKey': 'GuacamoleElasticIpAllocationId', 'ParameterValue': 'eipalloc-00ff1ef8b0c8562ad'}, {'ParameterKey': 'TetDataElasticIp', 'ParameterValue': '3.20.190.112'}, {'ParameterKey': 'TetDataElasticIpAllocationId', 'ParameterValue': 'eipalloc-025e2db995a9b3751'}, {'ParameterKey': 'Region', 'ParameterValue': 'us-east-2'}, {'ParameterKey': 'Subnet01AvailabilityZone', 'ParameterValue': 'a'}, {'ParameterKey': 'Subnet02AvailabilityZone', 'ParameterValue': 'b'}, {'ParameterKey': 'Subnet03AvailabilityZone', 'ParameterValue': 'a'}, {'ParameterKey': 'ISEIPAddress', 'ParameterValue': '172.16.171.49'}, {'ParameterKey': 'Win10EmployeePrivateIp', 'ParameterValue': '198.18.0.12'}, {'ParameterKey': 'Win10SysAdminPrivateIp', 'ParameterValue': '198.18.0.13'}, {'ParameterKey': 'AttackerPrivateIp', 'ParameterValue': '198.18.0.14'}, {'ParameterKey': 'IISOutsidePrivateIp', 'ParameterValue': '198.18.0.15'}, {'ParameterKey': 'ApacheOutsidePrivateIp', 'ParameterValue': '198.18.0.16'}, {'ParameterKey': 'ASAvOutsidePrivateIp01', 'ParameterValue': '198.18.0.17'}, {'ParameterKey': 'ASAvOutsidePrivateIp02', 'ParameterValue': '198.18.0.18'}, {'ParameterKey': 'Ubuntu1804EmployeePrivateIp', 'ParameterValue': '198.18.0.19'}, {'ParameterKey': 'Ubuntu1804SysAdminPrivateIp', 'ParameterValue': '198.18.0.20'}, {'ParameterKey': 'GuacamoleOutsidePrivateIp', 'ParameterValue': '198.18.0.21'}, {'ParameterKey': 'ASAvImageID', 'ParameterValue': 'ami-018637632d5e62976'}, {'ParameterKey': 'LDAPImageID', 'ParameterValue': 'ami-0273c11f1bc3fff82'}, {'ParameterKey': 'MSSQLImageID', 'ParameterValue': 'ami-090ab21d87411b44e'}, {'ParameterKey': 'IISImageID', 'ParameterValue': 'ami-0c4e857f7ec9de0dc'}, {'ParameterKey': 'MySQLImageID', 'ParameterValue': 'ami-0c170ef4a4f9b1789'}, {'ParameterKey': 'ApacheImageID', 'ParameterValue': 'ami-0bb3d60453bbc693a'}, {'ParameterKey': 'AnsibleImageID', 'ParameterValue': 'ami-08faf88a030245bd6'}, {'ParameterKey': 'TetrationDataIngestImageID', 'ParameterValue': 'ami-0c2276fc51ad25018'}, {'ParameterKey': 'TetrationEdgeImageID', 'ParameterValue': 'ami-0cb78ddba97ce6591'}, {'ParameterKey': 'Win10EmployeeImageID', 'ParameterValue': 'ami-03a948df14a70d159'}, {'ParameterKey': 'Win10SysAdminImageID', 'ParameterValue': 'ami-03a948df14a70d159'}, {'ParameterKey': 'Ubuntu1804EmployeeImageID', 'ParameterValue': 'ami-0483fe5b0c9444daa'}, {'ParameterKey': 'Ubuntu1804SysAdminImageID', 'ParameterValue': 'ami-0483fe5b0c9444daa'}, {'ParameterKey': 'AttackerImageID', 'ParameterValue': 'ami-09b253f6574754048'}, {'ParameterKey': 'GuacamoleImageID', 'ParameterValue': 'ami-04e70edcc169673d7'}, {'ParameterKey': 'EKSWorkerImageID', 'ParameterValue': 'ami-0c4c60006aa81c29b'}]
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
.
.
.
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_IN_PROGRESS
INFO: StackName: cisco-student-00, Status: CREATE_COMPLETE
INFO: CloudFormation Completed Successfully...
INFO: Initializing EKS DNS Assembly...
INFO: EKS DNS Assembly Completed...
INFO: StackName: cisco-student-00, Status: Generating CSV Report...
Exiting! All The Tasks Are Completed Successfully...
```

Then you should find in your relative-path `reports` directory, a CSV file with every students' information. An enhancement to export a single XLS file with nicely formatted info *per student* is something we aim to do, in addition to the currently exported single CSV which is still very useful for the Lab Admin. 


##### LICENSE

This lab is provided using the [GPL-3.0](https://github.com/OnstakInc/cisco-tetration-hol/blob/master/LICENSE). You may fork this repo and use it mostly as you like, however you must retain the same GPL license, and you must give credit. This lab was created by [Raheel Anwar](https://github.com/raheel-anwar), Muneeb Ali, [Matt Mullen](https://github.com/mamullen13316), and [Mark Snow](https://github.com/highspeedsnow) with [OnStak](https://onstak.com). 