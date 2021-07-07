import pandas as pd
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def calculating_the_search_rate(ri):
    # Check the data type of 'search_conducted'
    print(ri.search_conducted.dtypes)

    # Calculate the search rate by counting the values
    print(ri.search_conducted.value_counts(normalize=True))

    # Calculate the search rate by taking the mean
    # if a columns has the type boolean, mean() returns the percentage of row with value True
    print(ri.search_conducted.mean(), end="\n\n")


def comparing_search_rates_by_gender(ri):
    print("Calculate the search rate for female drivers")
    print(ri[ri.driver_gender == "F"].search_conducted.mean())

    print("Calculate the search rate for male drivers")
    print(ri[ri.driver_gender == "M"].search_conducted.mean())

    print("Calculate the search rate for both groups simultaneously")
    print(ri.groupby("driver_gender").search_conducted.mean(), end="\n\n")


def adding_a_second_factor_to_groupby(ri):
    print("Calculate the search rate for each combination of gender and violation")
    print(ri.groupby(["driver_gender", "violation"]
                     ).search_conducted.mean(), end="\n\n")

    print("Reverse the ordering to group by violation before gender")
    print(ri.groupby(["violation", "driver_gender"]
                     ).search_conducted.mean(), end="\n\n")


ri = prepare_data_for_following_chapters()
calculating_the_search_rate(ri)
comparing_search_rates_by_gender(ri)
adding_a_second_factor_to_groupby(ri)