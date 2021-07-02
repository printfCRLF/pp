import pandas as pd
from datetime import datetime


def load_hurricanes_data():
    return pd.read_pickle("data/florida_hurricane_dates.pkl")


def load_bike_data():
    return pd.read_csv("data/capital-onebike.csv")


def load_onebike_datetimes():
    bike_data = load_bike_data()
    onebike_datetime_strings = bike_data[['Start date', 'End date']]
    onebike_datetimes = []
    format = "%Y-%m-%d %H:%M:%S"

    for index, row in onebike_datetime_strings.iterrows():
        onebike_datetimes.append({
            "start": datetime.strptime(row['Start date'], format),
            "end": datetime.strptime(row['End date'], format)
        })

    return onebike_datetimes
