import numpy as np
import pandas as pd 
import datetime as dt 
import missingno as msno 
import matplotlib.pyplot as plt 

banking = pd.read_csv('data/banking_dirty.csv')

def uniformity(): 
    acct_eu = banking['acct_cur'] == 'euro'
    banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1
    banking.loc[acct_eu, 'acct_cur'] = 'dollar'
    assert banking['acct_cur'].unique() == 'dollar'

    print(banking['account_opened'].head())
    banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                            # Infer datetime format
                                            infer_datetime_format = True,
                                            # Return missing value for error
                                            errors = 'coerce') 
    banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')
    print(banking['acct_year'])

def cross_field_validation(): 
    # Store fund columns to sum against
    fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']
    # Find rows where fund_columns row sum == inv_amount
    inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']
    # Store consistent and inconsistent data
    consistent_inv = banking[inv_equ]
    inconsistent_inv = banking[~inv_equ]

    # Store consistent and inconsistent data
    print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

    # Store today's date and find ages
    today = dt.date.today()
    ages_manual = today.year - banking['birth_date'].dt.year
    # Find rows where age column == ages_manual
    age_equ = ages_manual == banking['age']
    # Store consistent and inconsistent data
    consistent_ages = banking[age_equ]
    inconsistent_ages = banking[~age_equ]
    # Store consistent and inconsistent data
    print("Number of inconsistent ages: ", inconsistent_ages.shape[0])

def completeness(): 
    print()

#uniformity()
#cross_field_validation()
completeness()