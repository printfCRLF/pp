import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
from dateutil import tz


def timezones_in_pandas(rides):
    # Localize the Start date column to America/New_York
    rides['Start date'] = rides['Start date'].dt.tz_localize(
        "America/New_York", ambiguous="NaT")

    rides['End date'] = rides['End date'].dt.tz_localize(
        "America/New_York", ambiguous="NaT")

    # Print first value
    print(rides['Start date'].iloc[0])
    return rides


def how_long_per_weekday(rides):
    # Add a column for the weekday of the start of the ride
    rides['Ride start weekday'] = rides['Start date'].dt.day_name()

    # Print the median trip time per weekday
    print(rides.groupby("Ride start weekday")['Duration'].median())


def how_long_between_rides(rides):
    # Shift the index of the end date up one; now subract it from the start date
    rides['Time since'] = rides['Start date'] - (rides["End date"].shift(1))

    # Move from a timedelta to a number of seconds, which is easier to work with
    rides['Time since'] = rides['Time since'].dt.total_seconds()

    # Resample to the month
    monthly = rides.resample("M", on="Start date")

    # Print the average hours between rides each month
    print(monthly['Time since'].mean()/(60*60))


rides = pd.read_csv('data/capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])
ride_durations = rides['End date'] - rides["Start date"]
rides['Duration'] = ride_durations.dt.total_seconds()

rides = timezones_in_pandas(rides)
how_long_per_weekday(rides)
how_long_between_rides(rides)
