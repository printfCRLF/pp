from datetime import date
from data import load_hurricanes_data


def which_day_of_the_week():
    # Create a date object
    hurricane_andrew = date(1992, 8, 24)
    # Which day of the week is the date?
    print(hurricane_andrew.weekday())


def how_many_hurricanes_come_early(florida_hurricane_dates):
    early_hurricanes = 0
    for hurricane in florida_hurricane_dates:
        if hurricane.month < 6:
            early_hurricanes += 1

    print(early_hurricanes)


# which_day_of_the_week()
hurricanes = load_hurricanes_data()
how_many_hurricanes_come_early(hurricanes)
