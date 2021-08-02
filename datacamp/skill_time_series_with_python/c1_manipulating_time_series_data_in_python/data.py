import pandas as pd

air_quality_folder = "air_quality_data"
stock_folder = "stock_data"


def load_air_quality_nyc_data():
    return pd.read_csv(f"data/{air_quality_folder}/nyc.csv")


def load_co_cities_data():
    df = pd.read_csv(f"data/{air_quality_folder}/co_cities.csv")
    df.date = pd.to_datetime(df.date)
    df.set_index("date", inplace=True)
    return df


def load_stock_yahoo_data():
    df = pd.read_csv(f"data/{stock_folder}/yahoo.csv")
    df.date = pd.to_datetime(df.date)
    df.set_index("date", inplace=True)
    return df


def load_stock_google_data():
    return pd.read_csv(f"data/{stock_folder}/google.csv", parse_dates=["Date"], index_col="Date")
