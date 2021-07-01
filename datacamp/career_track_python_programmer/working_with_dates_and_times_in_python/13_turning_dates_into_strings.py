from datetime import date
from data import load_hurricanes_data


def printing_dates_in_friendly_format(florida_hurricane_dates):
    # Assign the earliest date to first_date
    first_date = min(florida_hurricane_dates)

    # Convert to ISO and US formats
    iso = "Our earliest hurricane date: " + first_date.isoformat()
    us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

    print("ISO: " + iso)
    print("US: " + us)


def representing_dates_in_different_ways():
    # Create a date object
    andrew = date(1992, 8, 26)
    # Print the date in the format 'YYYY-MM'
    print(andrew.strftime("%Y-%m"))

    # Print the date in the format 'MONTH (YYYY)'
    print(andrew.strftime("%B (%Y)"))

    # Print the date in the format 'YYYY-DDD'
    print(andrew.strftime("%Y-%j"))


hurricanes = load_hurricanes_data()
printing_dates_in_friendly_format(hurricanes)
representing_dates_in_different_ways()
