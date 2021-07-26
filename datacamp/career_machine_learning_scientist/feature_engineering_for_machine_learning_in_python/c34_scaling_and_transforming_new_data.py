import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, PowerTransformer
from data import load_stackoverflow_data


def train_and_testing_transformation(so_train_numeric, so_test_numeric):
    # Apply a standard scaler to the data
    SS_scaler = StandardScaler()
    # Fit the standard scaler to the data
    SS_scaler.fit(so_train_numeric[["Age"]])
    # Transform the test data using the fitted scaler
    so_test_numeric['Age_ss'] = SS_scaler.transform(so_test_numeric[["Age"]])
    print(so_test_numeric[['Age', 'Age_ss']].head())

    train_std = so_train_numeric['ConvertedSalary'].std()
    train_mean = so_train_numeric['ConvertedSalary'].mean()

    cut_off = train_std * 3
    train_lower, train_upper = train_mean - cut_off, train_mean + cut_off

    # Trim the test DataFrame
    trimmed_df = so_test_numeric[(so_test_numeric['ConvertedSalary'] < train_upper)
                                 & (so_test_numeric['ConvertedSalary'] > train_lower)]


df = load_stackoverflow_data()
so_numeric_df = df[["ConvertedSalary", "Age", "Years Experience"]]
so_train_numeric = so_numeric_df.iloc[:300, :]
so_test_numeric = so_numeric_df.iloc[300:, :]
train_and_testing_transformation(so_train_numeric, so_test_numeric)
