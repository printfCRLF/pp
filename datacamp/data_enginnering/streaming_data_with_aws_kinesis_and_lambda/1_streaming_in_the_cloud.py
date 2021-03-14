# Import boto3 and create boto3 Firehose client
import boto3 
import util
import _setup

firehose, s3 = _setup.ex_vars
AWS_KEY_ID, AWS_SECRET = util.read_info_datacampDemoUser()

def managing_firehose_delivery_streams(): 
    endpoints = util.get_endpoints()
    firehose = boto3.client('firehose', 
        aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET, 
        region_name='us-east-1', endpoint_url=endpoints['FIREHOSE'])

    # Get list of delivery streams
    response = firehose.list_delivery_streams()

    # Iterate over the response contents and delete every stream
    for stream_name in response['DeliveryStreamNames']:
        firehose.delete_delivery_stream(DeliveryStreamName=stream_name)
        print(f"Deleted stream: {stream_name}")

    # Print list of delivery streams
    print(firehose.list_delivery_streams())
    
def s3_bucket_creation(): 
    # Create the new sd-vehicle-data bucket
    s3.create_bucket(Bucket='bowen-sd-vehicle-data')

    # List the buckets in S3
    for bucket_info in s3.list_buckets()['Buckets']:       
        # Get the bucket_name
        bucket_name = bucket_info['Name']        
        # Generate bucket ARN.
        arn = "arn:aws:s3:::{}".format(bucket_name)
        # Print the ARN
        print(arn)    

def create_your_first_firehose_stream(): 
    s3.create_bucket(Bucket='bowen-sd-vehicle-data')
    res = firehose.create_delivery_stream(
        DeliveryStreamName="gps-delivery-stream",
        DeliveryStreamType="DirectPut",
        S3DestinationConfiguration = {
            "BucketARN": "arn:aws:s3:::bowen-sd-vehicle-data",
            "RoleARN": "arn:aws:iam::046184967052:role/firehoseDeliveryRole1"
        }
    )

    print("Created Firehose Stream ARN: {}".format(res['DeliveryStreamARN']))


#managing_firehose_delivery_streams();
#s3_bucket_creation();
create_your_first_firehose_stream()
