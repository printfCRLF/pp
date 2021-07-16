from datetime import datetime, timedelta, timezone
from dateutil import tz


def how_many_hours_elapsed_around_daylight_saving():
    # Start on March 12, 2017, midnight, then add 6 hours
    start = datetime(2017, 3, 12, tzinfo=tz.gettz('America/New_York'))
    end = start + timedelta(hours=6)
    print(start.isoformat() + " to " + end.isoformat())

    # How many hours have elapsed?
    print("How many hours have elapsed in local time",
          (end - start).total_seconds()/(60*60))

    # What if we move to UTC?
    print("How many hours have elapsed in UTC", (end.astimezone(
        timezone.utc) - start.astimezone(timezone.utc)).total_seconds()/(60*60))

# In the United Kingdom, Daylight saving time begins on the last Sunday in March.
# March 29 is not always the last Sunday in March


def march_29_midnight_throughout_a_decade():
    # Create starting date
    dt = datetime(2000, 3, 29, tzinfo=tz.gettz("Europe/London"))

    # Loop over the dates, replacing the year, and print the ISO timestamp
    for y in range(2000, 2011):
        print(dt.replace(year=y).isoformat())


how_many_hours_elapsed_around_daylight_saving()
march_29_midnight_throughout_a_decade()
