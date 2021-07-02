from datetime import datetime
from data import load_bike_data, load_onebike_datetimes


def turning_strings_into_datetimes1():
    # Starting string, in YYYY-MM-DD HH:MM:SS format
    s = '2017-02-03 00:00:01'
    # Write a format string to parse s
    fmt = '%Y-%m-%d %H:%M:%S'
    # Create a datetime object d
    d = datetime.strptime(s, fmt)
    # Print d
    print(d)


def turning_strings_into_datetimes2():
    # Starting string, in YYYY-MM-DD format
    s = '2030-10-15'
    # Write a format string to parse s
    fmt = '%Y-%m-%d'
    # Create a datetime object d
    d = datetime.strptime(s, fmt)
    # Print d
    print(d)


def turning_strings_into_datetimes3():
    # Starting string, in MM/DD/YYYY HH:MM:SS format
    s = '12/15/1986 08:00:00'
    # Write a format string to parse s
    fmt = '%m/%d/%Y %H:%M:%S'
    # Create a datetime object d
    d = datetime.strptime(s, fmt)
    # Print d
    print(d)


def parsing_pairs_of_strings():
    onebike_datetime_strings = [('2017-10-01 15:23:25', '2017-10-01 15:26:26'),
                                ('2017-10-01 15:42:57', '2017-10-01 17:49:59'),
                                ('2017-10-02 06:37:10', '2017-10-02 06:42:53'),
                                ('2017-10-02 08:56:45', '2017-10-02 09:18:03'),
                                ('2017-10-02 18:23:48', '2017-10-02 18:45:05')]
    # Write down the format string
    fmt = "%Y-%m-%d %H:%M:%S"

    # Initialize a list for holding the pairs of datetime objects
    onebike_datetimes = []

    # Loop over all trips
    for (start, end) in onebike_datetime_strings:
        trip = {'start': datetime.strptime(start, fmt),
                'end': datetime.strptime(end, fmt)}
        # Append the trip
        onebike_datetimes.append(trip)

    print(onebike_datetimes)


def recreating_iso_format_with_strftime(onebike_datetimes):
    # Pull out the start of the first trip
    first_start = onebike_datetimes[0]['start']

    # Format to feed to strftime()
    fmt = "%Y-%m-%dT%H:%M:%S"

    # Print out date with .isoformat(), then with .strftime() to compare
    print(first_start.isoformat())
    print(first_start.strftime(fmt))


def unix_timestamps():
    # Starting timestamps
    timestamps = [1514665153, 1514664543]

    dts = []
    for ts in timestamps:
        dts.append(datetime.fromtimestamp(ts))

    print(dts)


# turning_strings_into_datetimes1()
# turning_strings_into_datetimes2()
# turning_strings_into_datetimes3()
# parsing_pairs_of_strings()

# onebike_datetimes = load_onebike_datetimes()
# recreating_iso_format_with_strftime(onebike_datetimes)
unix_timestamps()
