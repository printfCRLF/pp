import pandas as pd
from data import load_homelessness_data


def inspecting_a_data_frame(homelessness):
    # Print the head of the homelessness data
    print(homelessness.head())

    # Print information about homelessness
    print(homelessness.info())

    # Print the shape of homelessness
    print(homelessness.shape)

    # Print a description of homelessness
    print(homelessness.describe())


def parts_of_a_dataframe(homelessness):
    # Print the values of homelessness
    print(homelessness.values)

    # Print the column index of homelessness
    print(homelessness.columns)

    # Print the row index of homelessness
    print(homelessness.index)


homelessness = load_homelessness_data()
inspecting_a_data_frame(homelessness)
parts_of_a_dataframe(homelessness)
