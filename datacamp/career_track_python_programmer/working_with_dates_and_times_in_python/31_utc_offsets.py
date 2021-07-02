from datetime import datetime, timezone, timedelta
from data import load_onebike_datetimes


def creating_timezone_aware_datetimes():
    # October 1, 2017 at 15:26:26, UTC
    dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)
    print("UTC time", dt.isoformat())

    # Create a timezone for Pacific Standard Time, or UTC-8
    pst = timezone(timedelta(hours=-8))
    # October 1, 2017 at 15:26:26, UTC-8
    dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)
    print("Pacifice Standard Time (UTC-8)", dt.isoformat())

    # Create a timezone for Australian Eastern Daylight Time, or UTC+11
    aedt = timezone(timedelta(hours=11))
    # October 1, 2017 at 15:26:26, UTC+11
    dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)
    print("Australian Eastern  Daylight Time (UTC+11)", dt.isoformat())


def setting_timezones(onebike_datetimes):
    # Create a timezone object corresponding to UTC-4
    edt = timezone(timedelta(hours=-4))

    # Loop over trips, updating the start and end datetimes to be in UTC-4
    for trip in onebike_datetimes[:10]:
        # Update trip['start'] and trip['end']
        trip['start'] = trip['start'].replace(tzinfo=edt)
        trip['end'] = trip['end'].replace(tzinfo=edt)

    return onebike_datetimes


def what_time_did_bike_leave_in_UTC(onebike_datetimes):
    # Loop over the trips
    for trip in onebike_datetimes[:10]:
        # Pull out the start
        dt = trip['start']
        # Move dt to be in UTC
        dt = dt.astimezone(timezone.utc)

        # Print the start time in UTC
        print('Original:', trip['start'], '| UTC:', dt.isoformat())


# creating_timezone_aware_datetimes()
onebike_datetimes = load_onebike_datetimes()
onebike_datetimes_in_edt = setting_timezones(onebike_datetimes)
what_time_did_bike_leave_in_UTC(onebike_datetimes_in_edt)
