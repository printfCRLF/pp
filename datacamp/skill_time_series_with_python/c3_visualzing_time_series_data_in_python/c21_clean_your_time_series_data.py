import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def findinng_missing_values(co2_levels):
    # Display first seven rows of co2_levels
    print(co2_levels.head(7))
    # Set datestamp column as index
    co2_levels = co2_levels.set_index("datestamp")
    # Print out the number of missing values
    print(co2_levels.isnull().sum())

    return co2_levels


def handle_missing_values(co2_levels):
    # Impute missing values with the next valid observation
    co2_levels = co2_levels.fillna(method="bfill")
    # Print out the number of missing values
    print(co2_levels.isnull().sum())


if __name__ == "__main__":
    sns.set()
    co2_levels = pd.read_csv("data/ch2_co2_levels.csv")
    co2_levels = findinng_missing_values(co2_levels)
    handle_missing_values(co2_levels)
