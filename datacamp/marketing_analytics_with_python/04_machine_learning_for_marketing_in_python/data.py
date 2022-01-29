import pandas as pd


def load_telco_data():
    df = pd.read_csv("data/telco.csv", na_filter=True)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df_without_na = df.dropna()
    df_without_na = df_without_na.reset_index()

    return df_without_na
