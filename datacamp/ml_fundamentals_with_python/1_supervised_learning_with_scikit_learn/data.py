import pandas as pd


def load_gm_data():
    df = pd.read_csv('data/gm_2008_region.csv')
    X = df.drop(columns=['life', 'Region']).values
    y = df['life'].values
    return X, y


def load_diabetes_data():
    df = pd.read_csv('data/diabetes.csv')
    X = df.drop(columns=['diabetes']).values
    y = df['diabetes'].values
    return X, y
