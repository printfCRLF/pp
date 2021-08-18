import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score
from glob import glob
from util import replace_outliers, percent_change


def visualizing_messy_data():
    df = pd.read_csv("data/prices.csv", parse_dates=["date"], index_col="date")
    mask = df["symbol"].isin(["EBAY", "NVDA", "YHOO"])
    df = df[mask]

    prices = df.pivot_table(
        values="close", index=df.index, columns="symbol")
    # all_prices = all_prices["2010": "2013"]
    prices.loc["2013", "EBAY"] = np.NaN
    prices.loc["2011":"2012", "NVDA"] = np.NaN
    prices.loc["2011", "YHOO"] = np.NaN
    # Visualize the dataset
    prices.plot()
    plt.tight_layout()
    plt.show()

    # Count the missing values of each time series
    missing_values = prices.isna().sum()
    print(missing_values)

    return prices


# Create a function we'll use to interpolate and plot
def interpolate_and_plot(prices, interpolation):
    # Create a boolean mask for missing values
    missing_values = prices.isna()
    # Interpolate the missing values
    prices_interp = prices.interpolate(interpolation)
    # Plot the results, highlighting the interpolated values in black
    fig, ax = plt.subplots(figsize=(10, 5))
    prices_interp.plot(color='k', alpha=.6, ax=ax, legend=False)
    # Now plot the interpolated values on top in red
    prices_interp[missing_values].plot(ax=ax, color='r', lw=3, legend=False)
    plt.show()


def imputing_missing_values(prices):
    # Interpolate using the latest non-missing value
    interpolation_type = "zero"
    interpolate_and_plot(prices, interpolation_type)

    # Interpolate linearly
    interpolation_type = "linear"
    interpolate_and_plot(prices, interpolation_type)

    # Interpolate with a quadratic function
    interpolation_type = "quadratic"
    interpolate_and_plot(prices, interpolation_type)


def transforming_raw_data():
    df = pd.read_csv("data/prices.csv", parse_dates=["date"], index_col="date")
    mask = df["symbol"].isin(["EBAY", "NVDA", "YHOO", "AAPL"])
    df = df[mask]
    prices = df.pivot_table(values="close", index=df.index, columns="symbol")

    # Apply your custom function and plot
    prices_perc = prices.rolling(20).apply(percent_change)
    prices_perc.loc["2014":"2015"].plot()
    plt.show()

    return prices_perc


def handling_outliers(prices_perc):
    # Apply your preprocessing function to the timeseries and plot the results
    prices_perc = prices_perc.apply(replace_outliers)
    prices_perc.loc["2014":"2015"].plot()
    plt.show()


if __name__ == "__main__":
    sns.set()
    # prices = visualizing_messy_data()
    # imputing_missing_values(prices)
    prices_perc = transforming_raw_data()
    handling_outliers(prices_perc)
