# _setup.py: Create clients, load data, etc. No need to edit.

import boto3
import util

AWS_KEY_ID, AWS_SECRET = util.read_info_dcUser()

# Create firehose client
firehose = boto3.client('firehose', 
    aws_access_key_id=AWS_KEY_ID, 
    aws_secret_access_key=AWS_SECRET, 
    region_name='us-east-1') 
    #endpoint_url="http://localhost:4573")

# Create s3 client
s3 = boto3.client('s3', 
    aws_access_key_id=AWS_KEY_ID, 
    aws_secret_access_key=AWS_SECRET, 
    region_name='us-east-1')
    #endpoint_url="http://localhost:4572")

# Prep variables for export
ex_vars = [firehose, s3]
