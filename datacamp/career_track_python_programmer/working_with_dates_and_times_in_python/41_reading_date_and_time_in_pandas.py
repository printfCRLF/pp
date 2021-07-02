import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
from dateutil import tz
from data import load_onebike_datetimes


def loading_a_csv_file_in_pandas():
    # Load CSV into the rides variable
    rides = pd.read_csv('data/capital-onebike.csv',
                        parse_dates=['Start date', 'End date'])
    # Print the initial (0th) row
    print(rides.iloc[0])
    return rides


def making_timedelta_columns(rides):
    # Subtract the start date from the end date
    ride_durations = rides['End date'] - rides["Start date"]
    # Convert the results to seconds
    rides['Duration'] = ride_durations.dt.total_seconds()
    print(rides['Duration'].head())

    return rides

rides_data = loading_a_csv_file_in_pandas()
rides = making_timedelta_columns(rides_data)
