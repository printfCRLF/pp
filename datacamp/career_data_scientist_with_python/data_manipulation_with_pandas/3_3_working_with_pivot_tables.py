import numpy as np
import pandas as pd
from data import load_temperature_data


def pivot_temperature_by_city_year(temperatures):
    # Add a year column to temperatures
    temperatures["year"] = temperatures["date"].dt.year

    # Pivot avg_temp_c by country and city vs year
    temp_by_country_city_vs_year = temperatures.pivot_table(
        values="avg_temp_c", index=["country", "city"], columns="year")

    # See the result
    print(temp_by_country_city_vs_year)

    return temp_by_country_city_vs_year


def subsetting_pivot_tables(temp_by_country_city_vs_year):
    # Subset for Egypt to India
    temp_by_country_city_vs_year.loc["Egypt":"India"]

    # Subset for Egypt, Cairo to India, Delhi
    temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

    # Subset in both directions at once
    result = temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):(
        "India", "Delhi"), "2005":"2010"]

    print(result)


def subsetting_pivot_tables2(temp_by_country_city_vs_year):
    # Subset for Egypt to India
    temp_by_country_city_vs_year.loc["Egypt":"India"]

    # Subset for Egypt, Cairo to India, Delhi
    temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

    # Subset in both directions at once
    result = temp_by_country_city_vs_year.loc[(
        "Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]

    print(result)


def calculating_on_pivot_table(temp_by_country_city_vs_year):
    # Get the worldwide mean temp by year
    mean_temp_by_year = temp_by_country_city_vs_year.mean()

    # Filter for the year that had the highest mean temp
    print(mean_temp_by_year[mean_temp_by_year >= max(mean_temp_by_year)])

    # Get the mean temp by city
    mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

    # Filter for the city that had the lowest mean temp
    print(mean_temp_by_city[mean_temp_by_city <= min(mean_temp_by_city)])


temperatures = load_temperature_data()
temp_by_country_city_vs_year = pivot_temperature_by_city_year(temperatures)
# subsetting_pivot_tables(temp_by_country_city_vs_year)
# subsetting_pivot_tables2(temp_by_country_city_vs_year)
calculating_on_pivot_table(temp_by_country_city_vs_year)
