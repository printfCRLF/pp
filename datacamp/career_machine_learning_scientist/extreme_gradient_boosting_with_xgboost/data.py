import pandas as pd


def load_ridesharing_churn_data():
    return pd.read_csv("data/churn.csv")


def load_ames_housing_data_trimmed():
    return pd.read_csv("data/ames_housing_trimmed_processed.csv")


def load_ames_housing_data_unprocessed():
    return pd.read_csv("data/ames_unprocessed_data.csv")


def load_kidney_data():
    return pd.read_csv("data/chronic_kidney_disease.csv")
