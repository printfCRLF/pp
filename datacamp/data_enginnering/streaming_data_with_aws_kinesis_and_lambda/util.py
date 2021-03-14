import os 
import pandas as pd 

def read_info_datacampDemoUser(): 
    file_path = os.path.join('E:\\IT\\important', 'datacampDemoUser_accessKeys.csv')
    df = pd.read_csv(file_path)
    access_key_id = df.iloc[0, 0]
    secret_access_key = df.iloc[0, 1]
    return access_key_id, secret_access_key
    
def read_info_dcUser(): 
    file_path = os.path.join('E:\\IT\\important', 'dcUser_credentials.csv')
    df = pd.read_csv(file_path)
    access_key_id = df.iloc[0, 2]
    secret_access_key = df.iloc[0, 3]
    return access_key_id, secret_access_key

def get_endpoints(): 
    return {
        'FIREHOSE': 'http://localhost:4573',
        'IAM': 'http://localhost:4593',
        'KINESIS': 'http://localhost:4568',
        'LAMBDA': 'http://localhost:4574',
        'S3': 'http://localhost:4572'}

