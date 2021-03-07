import boto3 
import util 
import pandas as pd 

AWS_KEY_ID, AWS_SECRET = util.read_info()
s3 = boto3.client('s3', region_name='us-east-1', 
                        # Set up AWS credentials 
                        aws_access_key_id=AWS_KEY_ID, 
                        aws_secret_access_key=AWS_SECRET)
bucket_name = 'bowen-gid-staging'

def uploading_a_public_reprot(): 
    # Upload the final_report.csv to gid-staging bucket
    s3.upload_file(
    # Complete the filename
    Filename='./data/final_report.csv', 
    # Set the key and bucket
    Key='2019/final_report_2019_02_20.csv', 
    Bucket=bucket_name,
    # During upload, set ACL to public-read
    ExtraArgs = {
        'ACL': 'public-read'})    

def making_multiple_files_public(): 
    # List only objects that start with '2019/final_'
    response = s3.list_objects(
        Bucket=bucket_name, Prefix='2019/final_')

    # Iterate over the objects
    for obj in response['Contents']:
        # Give each object ACL of public-read
        s3.put_object_acl(Bucket=bucket_name, 
                        Key=obj['Key'], 
                        ACL='public-read')
        
        # Print the Public Object URL for each object
        print("https://{}.s3.amazonaws.com/{}".format(bucket_name, obj['Key']))    

def generating_a_presigned_url(): 
    # Generate presigned_url for the uploaded object
    share_url = s3.generate_presigned_url(
        # Specify allowable operations
        ClientMethod='get_object',
        # Set the expiration time
        ExpiresIn=3600,
        # Set bucket and shareable object's name
        Params={'Bucket': bucket_name,'Key': 'final_report.csv'}
        )

    # Print out the presigned URL
    print(share_url)    

def opening_a_private_file(): 
    df_list =  [ ] 

    for file in response['Contents']:
        # For each file in response load the object from S3
        obj = s3.get_object(Bucket='gid-requests', Key=file['Key'])
        # Load the object's StreamingBody with pandas
        obj_df = pd.read_csv(obj['Body'])
        # Append the resulting DataFrame to list
        df_list.append(obj_df)

    # Concat all the DataFrames with pandas
    df = pd.concat(df_list)

    # Preview the resulting DataFrame
    df.head()    

def generate_html_table_from_pandas(): 
    # Generate an HTML table with no border and selected columns
    services_df = pd.DataFrame();
    services_df.to_html('./services_no_border.html',
            # Keep specific columns only
            columns=['service_name', 'link'],
            # Set border
            border=0)

    # Generate an html table with border and all columns.
    services_df.to_html('./services_border_all_columns.html', 
            render_links=True, 
            border=1)

def update_an_html_file_to_s3(): 
    # Upload the lines.html file to S3
    s3.upload_file(Filename='lines.html', 
                # Set the bucket name
                Bucket='datacamp-public', Key='index.html',
                # Configure uploaded file
                ExtraArgs = {
                    # Set proper content type
                    'ContentType':'text/html',
                    # Set proper ACL
                    'ACL': 'public-read'})

    # Print the S3 Public Object URL for the new file.
    print("http://{}.s3.amazonaws.com/{}".format('datacamp-public', 'index.html'))    



#uploading_a_public_reprot()
#making_multiple_files_public()
generating_a_presigned_url()
opening_a_private_file()


