from datetime import datetime, timedelta, timezone
from dateutil import tz
from data import load_onebike_datetimes


def putting_the_bike_trips_into_the_right_timezone(onebike_datetimes):
    # Create a timezone object for Eastern Time
    et = tz.gettz('America/New_York')

    # Loop over trips, updating the datetimes to be in Eastern Time
    for trip in onebike_datetimes:
        # Update trip['start'] and trip['end']
        trip['start'] = trip['start'].replace(tzinfo=et)
        trip['end'] = trip['end'].replace(tzinfo=et)

    return onebike_datetimes


def setting_timezones(onebike_datetimes):
    # Create a timezone object corresponding to UTC-4
    edt = timezone(timedelta(hours=-4))

    # Loop over trips, updating the start and end datetimes to be in UTC-4
    for trip in onebike_datetimes:
        # Update trip['start'] and trip['end']
        trip['start'] = trip['start'].replace(tzinfo=edt)
        trip['end'] = trip['end'].replace(tzinfo=edt)

    return onebike_datetimes


def finding_ambiguous_datetimes(onebike_datetimes):
    # Loop over trips
    for trip in onebike_datetimes:
        # Rides with ambiguous start
        if tz.datetime_ambiguous(trip['start']):
            print("Ambiguous start at " + str(trip['start']))
        # Rides with ambiguous end
        if tz.datetime_ambiguous(trip['end']):
            print("Ambiguous end at " + str(trip['end']))


def cleaning_daylight_saving_data_with_fold(onebike_datetimes):
    trip_durations = []
    for trip in onebike_datetimes:
        # When the start is later than the end, set the fold to be 1
        if trip['start'] > trip['end']:
            trip['end'] = tz.enfold(trip['end'])
            # Convert to UTC
            start = trip['start'].astimezone(timezone.utc)
            end = trip['end'].astimezone(timezone.utc)

            # Subtract the difference
            trip_length_seconds = (end-start).total_seconds()
            trip_durations.append(trip_length_seconds)

    # Take the shortest trip duration
    print("Shortest trip: " + str(min(trip_durations)))


onebike_datetimes = load_onebike_datetimes()
onebike_datetimes_in_ny = putting_the_bike_trips_into_the_right_timezone(
    onebike_datetimes)
# onebike_datetimes_in_ny = setting_timezones(
#     onebike_datetimes)

finding_ambiguous_datetimes(onebike_datetimes_in_ny)
cleaning_daylight_saving_data_with_fold(onebike_datetimes_in_ny)
