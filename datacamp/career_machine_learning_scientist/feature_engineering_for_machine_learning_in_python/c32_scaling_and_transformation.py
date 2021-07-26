import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, PowerTransformer
from data import load_stackoverflow_data


def normailization(so_numeric_df):
    # Instantiate MinMaxScaler
    MM_scaler = MinMaxScaler()
    # Fit MM_scaler to the data
    MM_scaler.fit(so_numeric_df[['Age']])
    # Transform the data using the fitted scaler
    so_numeric_df['Age_MM'] = MM_scaler.transform(so_numeric_df[['Age']])
    # Compare the origional and transformed column
    print(so_numeric_df[['Age_MM', 'Age']].head())


def standardization(so_numeric_df):
    # Instantiate StandardScaler
    SS_scaler = StandardScaler()
    # Fit SS_scaler to the data
    SS_scaler.fit(so_numeric_df[['Age']])
    # Transform the data using the fitted scaler
    so_numeric_df['Age_SS'] = SS_scaler.transform(so_numeric_df[['Age']])
    # Compare the origional and transformed column
    print(so_numeric_df[['Age_SS', 'Age']].head())


def log_transformation(so_numeric_df):
    # Instantiate PowerTransformer
    pow_trans = PowerTransformer()
    # Train the transform on the data
    pow_trans.fit(so_numeric_df[["ConvertedSalary"]])
    # Apply the power transform to the data
    so_numeric_df['ConvertedSalary_LG'] = pow_trans.transform(
        so_numeric_df[['ConvertedSalary']])
    # Plot the data before and after the transformation
    so_numeric_df[['ConvertedSalary', 'ConvertedSalary_LG']].hist()
    plt.show()


df = load_stackoverflow_data()
so_numeric_df = df[["ConvertedSalary", "Age", "Years Experience"]]
# normailization(so_numeric_df)
# standardization(so_numeric_df)
log_transformation(so_numeric_df)
