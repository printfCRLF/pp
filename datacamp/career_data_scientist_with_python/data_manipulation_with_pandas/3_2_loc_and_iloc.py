import numpy as np
import pandas as pd
from data import load_temperature_data


def slicing_index_values(temperatures):
    # Index temperatures by country & city
    temperatures_ind = temperatures.set_index(["country", "city"])

    # Sort the index of temperatures_ind
    temperatures_srt = temperatures_ind.sort_index()

    # Subset rows from Pakistan to Russia
    print(temperatures_srt.loc["Pakistan":"Russia"])

    # Try to subset rows from Lahore to Moscow
    print(temperatures_srt.loc["Lahore":"Moscow"])

    # Subset rows from Pakistan, Lahore to Russia, Moscow
    print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])


def slice_in_both_directions(temperatures):
    # Index temperatures by country & city
    temperatures_srt = temperatures.set_index(["country", "city"]).sort_index()

    # Subset rows from India, Hyderabad to Iraq, Baghdad
    print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad")])

    # Subset columns from date to avg_temp_c
    print(temperatures_srt.loc[:, "date":"avg_temp_c"])

    # Subset in both directions at once
    print(temperatures_srt.loc[("India", "Hyderabad")          : ("Iraq", "Baghdad"), "date":"avg_temp_c"])


def slicing_time_series(temperatures):
    # Use Boolean conditions to subset temperatures for rows in 2010 and 2011
    temperatures_bool = temperatures[(temperatures["date"] >= "2010") & (
        temperatures["date"] <= "2011-12-31")]
    print(temperatures_bool)

    # Set date as an index and sort the index
    temperatures_ind = temperatures.set_index("date").sort_index()

    # Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
    print(temperatures_ind.loc["2010":"2011"])

    # Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
    print(temperatures_ind.loc["2010-08":"2011-02"])


def subsetting_by_row_column_number(temperatures):
    # Get 23rd row, 2nd column (index 22, 1)
    print(temperatures.iloc[22, 1])

    # Use slicing to get the first 5 rows
    print(temperatures.iloc[:5, ])

    # Use slicing to get columns 3 to 4
    print(temperatures.iloc[:, 2:4])

    # Use slicing in both directions at once
    print(temperatures.iloc[:5, 2:4])


temperatures = load_temperature_data()
# slicing_index_values(temperatures)
# slice_in_both_directions(temperatures)
# slicing_time_series(temperatures)
subsetting_by_row_column_number(temperatures)
