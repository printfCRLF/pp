import os 
import pandas as pd 

def read_info(): 
    file_path = os.path.join('E:\\IT\\important', 'datacampDemoUser_accessKeys.csv')
    df = pd.read_csv(file_path)
    access_key_id = df.iloc[0, 0]
    secret_access_key = df.iloc[0, 1]
    return access_key_id, secret_access_key
    # with open(file_path) as file: 
    #     user = file.readline()
    #     access_key_id = file.readline()
    #     secret_access_key = file.readline()
    # return user, access_key_id, secret_access_key

