import pandas as pd


def load_bike_share_data():
    return pd.read_csv("data/bike_share.csv")


def load_college_data():
    return pd.read_csv("data/college_datav3.csv")


def load_daily_show_guests_data():
    return pd.read_csv("data/daily_show_guests_cleaned.csv")


def load_fy18_4050_data():
    return pd.read_csv("data/FY18_4050_FMRs.csv")


def load_insurance_data():
    return pd.read_csv("data/insurance_premiums.csv")


def load_school_data():
    return pd.read_csv("data/schoolimprovement2010grants.csv")
