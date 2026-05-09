#!/usr/bin/env python3
"""
Script to launch an AWS EC2 instance
Requirements: boto3, AWS credentials configured
"""

import boto3
import sys
from botocore.exceptions import ClientError


def launch_ec2_instance(
    image_id="ami-0c55b159cbfafe1f0",  # Amazon Linux 2 AMI (us-east-1)
    instance_type="t2.micro",
    key_name=None,
    security_group_ids=None,
    subnet_id=None,
    instance_name="MyInstance"
):
    """
    Launch a single EC2 instance
    
    Args:
        image_id (str): AMI ID to use for the instance
        instance_type (str): Instance type (t2.micro, t2.small, etc.)
        key_name (str): EC2 key pair name for SSH access
        security_group_ids (list): List of security group IDs
        subnet_id (str): Subnet ID for VPC placement
        instance_name (str): Name tag for the instance
    
    Returns:
        dict: Instance information if successful, None otherwise
    """
    try:
        # Create EC2 client
        ec2_client = boto3.client('ec2', region_name='us-east-1')
        
        # Prepare run_instances parameters
        params = {
            'ImageId': image_id,
            'MinCount': 1,
            'MaxCount': 1,
            'InstanceType': instance_type,
            'TagSpecifications': [
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': instance_name}
                    ]
                }
            ]
        }
        
        # Add optional parameters if provided
        if key_name:
            params['KeyName'] = key_name
        
        if security_group_ids:
            params['SecurityGroupIds'] = security_group_ids
        
        if subnet_id:
            params['SubnetId'] = subnet_id
        
        # Launch the instance
        response = ec2_client.run_instances(**params)
        
        instance = response['Instances'][0]
        instance_id = instance['InstanceId']
        
        print(f"✓ EC2 instance launched successfully!")
        print(f"  Instance ID: {instance_id}")
        print(f"  Instance Type: {instance['InstanceType']}")
        print(f"  State: {instance['State']['Name']}")
        print(f"  AMI ID: {instance['ImageId']}")
        
        return {
            'instance_id': instance_id,
            'instance_type': instance['InstanceType'],
            'state': instance['State']['Name'],
            'ami_id': instance['ImageId']
        }
    
    except ClientError as e:
        print(f"✗ Error launching EC2 instance: {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None


if __name__ == "__main__":
    # Example usage - modify these values as needed
    print("Starting EC2 instance launch...")
    print("-" * 50)
    
    result = launch_ec2_instance(
        image_id="ami-0c55b159cbfafe1f0",  # Update for your region
        instance_type="t2.micro",
        key_name=None,  # Add your key pair name here
        security_group_ids=None,  # Add security group IDs if using VPC
        subnet_id=None,  # Add subnet ID if using VPC
        instance_name="MyInstance"
    )
    
    if result:
        print("-" * 50)
        print("Instance details:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print("Failed to launch instance")
        sys.exit(1)
