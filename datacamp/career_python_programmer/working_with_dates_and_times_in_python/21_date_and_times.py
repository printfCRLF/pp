from datetime import datetime
from data import load_bike_data, load_onebike_datetimes


def creating_datetimes_by_hand():
    # Create a datetime object
    dt = datetime(2017, 10, 1, 15, 26, 26)
    # Print the results in ISO 8601 format
    print(dt.isoformat())

    # Create a datetime object
    dt = datetime(2017, 12, 31, 15, 19, 13)

    # Print the results in ISO 8601 format
    print(dt.isoformat())

    # Create a datetime object
    dt = datetime(2017, 12, 31, 15, 19, 13)

    # Replace the year with 1917
    dt_old = dt.replace(year=1917)

    # Print the results in ISO 8601 format
    print(dt_old)


def counting_events_before_and_afternoon(onebike_datetimes):
    # Create dictionary to hold results
    trip_counts = {'AM': 0, 'PM': 0}

    # Loop over all trips
    for trip in onebike_datetimes:
        # Check to see if the trip starts before noon
        if trip['start'].hour < 12:
            # Increment the counter for before noon
            trip_counts['AM'] += 1
        else:
            # Increment the counter for after noon
            trip_counts['PM'] += 1

    print(trip_counts)


# creating_datetimes_by_hand()
onebike_datetimes = load_onebike_datetimes()
counting_events_before_and_afternoon(onebike_datetimes)
