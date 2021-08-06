import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import multi_period_return


def cumulative_sum_vs_diff():
    data = pd.read_csv("data/stock_data/google.csv",
                       parse_dates=["Date"], index_col="Date")
    data = data.dropna()

    # Calculate differences
    differences = data.diff().dropna()

    # Select start price
    start_price = data.first("D")

    # Calculate cumulative sum
    cumulative_sum = start_price.append(differences).cumsum()

    # Validate cumulative sum equals data
    print(data.dropna().equals(cumulative_sum))


def cumulative_return_of_1000_invested_in_google_vs_apple1():
    data = pd.read_csv("data/stock_data/apple_google.csv",
                       parse_dates=["Date"], index_col="Date")
    data = data.dropna()

    # Define your investment
    investment = 1000

    # Calculate the daily returns here
    returns = data.pct_change()
    # Calculate the cumulative returns here
    returns_plus_one = returns + 1
    cumulative_return = returns_plus_one.cumprod()

    # Calculate and plot the investment return here
    cumulative_return.mul(investment).plot()
    plt.show()


def cumulative_return_of_1000_invested_in_google_vs_apple2():
    data = pd.read_csv("data/stock_data/apple_google.csv",
                       parse_dates=["Date"], index_col="Date")

    # Calculate daily returns
    daily_returns = data.pct_change()

    # Calculate rolling_annual_returns
    rolling_annual_returns = daily_returns.rolling(
        "360D").apply(multi_period_return)

    # Plot rolling_annual_returns
    rolling_annual_returns.mul(100).plot()
    plt.show()


sns.set()
# cumulative_sum_vs_diff()
cumulative_return_of_1000_invested_in_google_vs_apple1()
cumulative_return_of_1000_invested_in_google_vs_apple2()
