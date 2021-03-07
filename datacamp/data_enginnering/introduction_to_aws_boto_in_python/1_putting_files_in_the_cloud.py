import boto3 
import util

AWS_KEY_ID, AWS_SECRET = util.read_info()

def your_first_bot3_client(): 
    s3 = boto3.client('s3', region_name='us-east-1', 
                            # Set up AWS credentials 
                            aws_access_key_id=AWS_KEY_ID, 
                            aws_secret_access_key=AWS_SECRET)
    buckets = s3.list_buckets()
    print(buckets)
    return s3


def multiple_clients(): 
    # Generate the boto3 client for interacting with S3 and SNS
    s3 = boto3.client('s3', region_name='eu-north-1', 
                            aws_access_key_id=AWS_KEY_ID, 
                            aws_secret_access_key=AWS_SECRET)

    sns = boto3.client('sns', region_name='eu-north-1', 
                            aws_access_key_id=AWS_KEY_ID, 
                            aws_secret_access_key=AWS_SECRET)

    # List S3 buckets and SNS topics
    buckets = s3.list_buckets()
    topics = sns.list_topics()

    # Print out the list of SNS topics
    print(topics)

def create_a_bucket(s3): 
    response_staging = s3.create_bucket(Bucket='bowen-gim-staging')
    response_processed = s3.create_bucket(Bucket='bowen-gim-processed')
    response_test = s3.create_bucket(Bucket='bowen-gim-test')

    print(response_staging)

def delete_a_bucket(s3): 
    # Delete the gim-test bucket
    s3.delete_bucket(Bucket='bowen-gim-test')

    # Get the list_buckets response
    response = s3.list_buckets()

    # Print each Buckets Name
    for bucket in response['Buckets']:
        print(bucket['Name'])

def deleting_multiple_buckets(s3): 
    # Get the list_buckets response
    response = s3.list_buckets()

    # Delete all the buckets with 'gim', create replacements.
    for bucket in response['Buckets']:
        if 'gim' in bucket['Name']:
            s3.delete_bucket(Bucket=bucket['Name'])
        
    s3.create_bucket(Bucket='bowen-gid-staging')
    s3.create_bucket(Bucket='bowen-gid-processed')
    
    # Print bucket listing after deletion
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])

def putting_files_in_the_cloud(s3): 
    s3.upload_file(Bucket='bowen-gid-staging',
                    Filename='data/final_report.csv',
                    Key='2019/final_report_01_01.csv')

    response = s3.head_object(Bucket='bowen-gid-staging', 
                                Key='2019/final_report_01_01.csv')
    print(response['ContentLength'])

def sprin_cleaning(s3): 
    # List only objects that start with '2018/final_'
    response = s3.list_objects(Bucket='gid-staging', 
                            Prefix='2018/final_')

    # Iterate over the objects
    if 'Contents' in response:
        for obj in response['Contents']:
            s3.delete_object(Bucket='gid-staging', Key=obj['Key'])

    # Print the keys of remaining objects in the bucket
    response = s3.list_objects(Bucket='gid-staging')
    for obj in response['Contents']:
        print(obj['Key'])    

s3 = your_first_bot3_client()
#multiple_clients()
#create_a_bucket(s3)
#delete_a_bucket(s3)
#deleting_multiple_buckets(s3)
putting_files_in_the_cloud(s3)
sprin_cleaning(s3)



