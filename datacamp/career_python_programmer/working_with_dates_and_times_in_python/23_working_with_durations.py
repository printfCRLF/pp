from datetime import datetime
from data import load_onebike_datetimes


def turning_pairs_of_datetimes_into_durations(onebike_datetimes):
    # Initialize a list for all the trip durations
    onebike_durations = []

    for trip in onebike_datetimes:
        # Create a timedelta object corresponding to the length of the trip
        trip_duration = trip['end'] - trip['start']

        # Get the total elapsed seconds in trip_duration
        trip_length_seconds = trip_duration.total_seconds()

        # Append the results to our list
        onebike_durations.append(trip_length_seconds)

    return onebike_durations


def average_trip_time(onebike_durations):
    # What was the total duration of all trips?
    total_elapsed_time = sum(onebike_durations)

    # What was the total number of trips?
    number_of_trips = len(onebike_durations)

    # Divide the total duration by the number of trips
    print(total_elapsed_time / number_of_trips)


def why_time_is_hard(onebike_durations):
    # Calculate shortest and longest trips
    shortest_trip = min(onebike_durations)
    longest_trip = max(onebike_durations)

    # Print out the results
    print("The shortest trip was " + str(shortest_trip) + " seconds")
    print("The longest trip was " + str(longest_trip) + " seconds")


onebike_datetimes = load_onebike_datetimes()
onebike_durations = turning_pairs_of_datetimes_into_durations(
    onebike_datetimes)
average_trip_time(onebike_durations)
why_time_is_hard(onebike_durations)
