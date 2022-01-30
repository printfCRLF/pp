import pandas as pd 

def load_c1_data(): 
    df = pd.read_csv("data/chapter_1/online.csv", parse_dates=["InvoiceDate"])
    return df

