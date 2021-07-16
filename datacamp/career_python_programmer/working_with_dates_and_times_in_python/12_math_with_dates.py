from datetime import date
from data import load_hurricanes_data


def subtracting_dates():
    # Create a date object for May 9th, 2007
    start = date(2007, 5, 9)
    # Create a date object for December 13th, 2007
    end = date(2007, 12, 13)
    # Subtract the two dates and print the number of days
    print((end - start).days)


def counting_events_per_calendar_month(florida_hurricane_dates):
    # A dictionary to count hurricanes per calendar month
    hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                             7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    # Loop over all hurricanes
    for hurricane in florida_hurricane_dates:
        # Pull out the month
        month = hurricane.month
        # Increment the count in your dictionary by one
        hurricanes_each_month[month] += 1

    print(hurricanes_each_month)


def putting_a_list_of_dates_in_order(dates_scrambled):
    # Print the first and last scrambled dates
    print(dates_scrambled[0])
    print(dates_scrambled[-1])

    # Put the dates in order
    dates_ordered = sorted(dates_scrambled)

    # Print the first and last ordered dates
    print(dates_ordered[0])
    print(dates_ordered[-1])


hurricanes = load_hurricanes_data()
# subtracting_dates()
# counting_events_per_calendar_month(hurricanes)
putting_a_list_of_dates_in_order(hurricanes)
