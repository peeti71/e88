import boto3
import sys
import os
import time



ec2client = boto3.client('ec2',
                         aws_access_key_id = 'AKIAIP62MH4CFI4SKOZQ',
                         aws_secret_access_key = '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',
                         region_name = 'us-east-1')


response = ec2client.describe_instances()

print(response)
