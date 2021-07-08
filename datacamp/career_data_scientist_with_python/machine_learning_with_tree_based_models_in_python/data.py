import pandas as pd


def load_wisconsin_breast_cancer_data():
    return pd.read_csv("data/wbc.csv")


def load_automobile_data():
    df = pd.read_csv("data/auto.csv")
    X = df.drop(columns=["mpg"])
    X = pd.get_dummies(X)
    y = df["mpg"]
    return X, y


def load_indian_liver_patient_preprocessed_data():
    return pd.read_csv("data/indian_liver_patient/indian_liver_patient_preprocessed.csv")
