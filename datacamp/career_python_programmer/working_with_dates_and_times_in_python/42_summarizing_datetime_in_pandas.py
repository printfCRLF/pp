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


def how_many_joyrides(rides):
    # Create joyrides
    joyrides = (rides["Start station"] == rides["End station"])
    # Total number of joyrides
    print("{} rides were joyrides".format(joyrides.sum()))
    # Median of all rides
    print("The median duration overall was {:.2f} seconds"
          .format(rides['Duration'].median()))
    # Median of joyrides
    print("The median duration for joyrides was {:.2f} seconds"
          .format(rides[joyrides]['Duration'].median()))


def its_getting_cold_outside(rides):
    # Resample rides to daily, take the size, plot the results
    rides.resample("D", on='Start date').size().plot(ylim=[0, 15])
    plt.show()

    # Resample rides to monthly, take the size, plot the results
    rides.resample("M", on='Start date').size().plot(ylim=[0, 150])
    plt.show()


def members_vs_casual_riders(rides):
    # Resample rides to be monthly on the basis of Start date
    monthly_rides = rides.resample("M", on="Start date")['Member type']
    # Take the ratio of the .value_counts() over the total number of rides
    print(monthly_rides.value_counts() / monthly_rides.size())


def combining_groupby_and_resample(rides):
    # Group rides by member type, and resample to the month
    grouped = rides.groupby('Member type')\
        .resample("M", on="Start date")

    # Print the median duration for each group
    print(grouped["Duration"].median())


rides_data = loading_a_csv_file_in_pandas()
rides = making_timedelta_columns(rides_data)
# how_many_joyrides(rides)
# its_getting_cold_outside(rides)
# members_vs_casual_riders(rides)
combining_groupby_and_resample(rides)
