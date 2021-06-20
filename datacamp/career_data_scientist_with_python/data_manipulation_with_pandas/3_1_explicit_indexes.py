import numpy as np
import pandas as pd
from data import load_temperature_data


def setting_and_removing_indices(temperatures):
    # Look at temperatures
    print(temperatures)

    # Index temperatures by city
    temperatures_ind = temperatures.set_index("city")

    # Look at temperatures_ind
    print(temperatures_ind)

    # Reset the index, keeping its contents
    print(temperatures_ind.reset_index())

    # Reset the index, dropping its contents
    print(temperatures_ind.reset_index(drop=True))


def subsetting_with_loc(temperatures):
    temperatures_ind = temperatures.set_index("city")
    # Make a list of cities to subset on
    cities = ["Moscow", "Saint Petersburg"]

    # Subset temperatures using square brackets
    print(temperatures[temperatures["city"].isin(cities)])

    # Subset temperatures_ind using .loc[]
    print(temperatures_ind.loc[cities])


def setting_multi_level_indexes(temperatures):
    # Index temperatures by country & city
    temperatures_ind = temperatures.set_index(["country", "city"])

    # List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
    rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

    # Subset for rows to keep
    print(temperatures_ind.loc[rows_to_keep])


def sorting_by_index_values(temperatures):
    # Index temperatures by country & city
    temperatures_ind = temperatures.set_index(["country", "city"])

    # Sort temperatures_ind by index values
    print(temperatures_ind.sort_index())

    # Sort temperatures_ind by index values at the city level
    print(temperatures_ind.sort_index(level="city"))

    # Sort temperatures_ind by country then descending city
    print(temperatures_ind.sort_index(
        level=["country", "city"], ascending=[True, False]))


temperatures = load_temperature_data()
# setting_and_removing_indices(temperatures)
# subsetting_with_loc(temperatures)
# setting_multi_level_indexes(temperatures)
sorting_by_index_values(temperatures)
