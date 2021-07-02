from datetime import datetime, timezone, timedelta
from dateutil import tz
from data import load_onebike_datetimes

# Summary
# datetime.replace set the timezone on a datetime object.
# datetime.astimezone(tz.gettz("Europe/London")) displays the time in the given local timezone.


def putting_the_bike_trips_into_the_right_timezone(onebike_datetimes):
    # Create a timezone object for Eastern Time
    et = tz.gettz('America/New_York')

    # Loop over trips, updating the datetimes to be in Eastern Time
    for trip in onebike_datetimes[:10]:
        # Update trip['start'] and trip['end']
        trip['start'] = trip['start'].replace(tzinfo=et)
        trip['end'] = trip['end'].replace(tzinfo=et)

    return onebike_datetimes


def what_time_did_the_bike_leave(onebike_datetimes):
    # Create the timezone object
    uk = tz.gettz("Europe/London")
    # Pull out the start of the first trip
    local = onebike_datetimes[0]['start']
    # What time was it in the UK?
    notlocal = local.astimezone(uk)
    # Print them out and see the difference
    print(local.isoformat())
    print(notlocal.isoformat())

    # Create the timezone object
    ist = tz.gettz("Asia/Kolkata")
    # Pull out the start of the first trip
    local = onebike_datetimes[0]['start']
    # What time was it in India?
    notlocal = local.astimezone(ist)
    # Print them out and see the difference
    print(local.isoformat())
    print(notlocal.isoformat())

    # Create the timezone object
    sm = tz.gettz("Pacific/Apia")
    # Pull out the start of the first trip
    local = onebike_datetimes[0]['start']
    # What time was it in Samoa?
    notlocal = local.astimezone(sm)
    # Print them out and see the difference
    print(local.isoformat())
    print(notlocal.isoformat())


onebike_datetimes = load_onebike_datetimes()
onebike_datetimes_in_edt = putting_the_bike_trips_into_the_right_timezone(
    onebike_datetimes)
what_time_did_the_bike_leave(onebike_datetimes_in_edt)
