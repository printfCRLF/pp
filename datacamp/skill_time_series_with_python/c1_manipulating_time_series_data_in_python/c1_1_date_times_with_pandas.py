import pandas as pd


def your_first_time_series():
    # Create the range of dates here
    seven_days = pd.date_range(start="2017-1-1", periods=7)

    # Iterate over the dates and print the number and name of the weekday
    for day in seven_days:
        print(day.dayofweek, day.day_name())


your_first_time_series()
