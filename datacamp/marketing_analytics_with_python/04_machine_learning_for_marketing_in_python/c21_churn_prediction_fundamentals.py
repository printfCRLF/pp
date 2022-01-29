import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from data import load_telco_data
from c12_preparation_for_modeling import seperate_numerical_and_categorical_columns, encoding_categorical_and_scale_numerical_variables


def explore_churn_and_split_data(telcom):
    # Print the unique Churn values
    print(set(telcom['Churn']))
    # Calculate the ratio size of each churn group
    telcom.groupby(['Churn']).size() / telcom.shape[0] * 100
    # Split the data into train and test
    train, test = train_test_split(telcom, test_size=.25)

    return train, test


def seperate_features_and_target_variable(telcom, train, test):
    custid = ["customerID"]
    target = ["Churn"]

    # Store column names from `telcom` excluding target variable and customer ID
    cols = [col for col in telcom.columns if col not in custid + target]

    # Extract training features
    train_X = train[cols]
    # Extract training target
    train_Y = train[target]
    # Extract testing features
    test_X = test[cols]
    # Extract testing target
    test_Y = test[target]

    return train_X, train_Y, test_X, test_Y


if __name__ == "__main__":
    telco_raw = load_telco_data()
    categorical, numerical = seperate_numerical_and_categorical_columns(
        telco_raw)
    telcom = encoding_categorical_and_scale_numerical_variables(
        telco_raw, categorical, numerical)
    train, test = explore_churn_and_split_data(telcom)
    seperate_features_and_target_variable(telcom, train, test)
