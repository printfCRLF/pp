import pandas as pd


def load_hurricanes_data():
    return pd.read_pickle("data/florida_hurricane_dates.pkl")
