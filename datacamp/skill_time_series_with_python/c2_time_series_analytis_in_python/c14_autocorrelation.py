import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def popular_strategy_using_autocorrelation():
    MSFT = pd.read_csv("data/financial_data/MSFT.csv",
                       parse_dates=["Date"], index_col="Date")
    # Convert the daily data to weekly data
    MSFT = MSFT.resample(rule="W").last()

    # Compute the percentage change of prices
    returns = MSFT.pct_change()

    # Compute and print the autocorrelation of returns
    autocorrelation = returns["Adj Close"].autocorr()
    print("The autocorrelation of weekly returns is %4.2f" % (autocorrelation))

    MSFT.plot()
    plt.show()


def are_interest_rate_auto_correlated():
    daily_rates = pd.read_csv("data/my_data/THREEFY10.csv",
                              parse_dates=["DATE"], index_col="DATE")
    daily_rates.rename(columns={"THREEFY10": "US10Y"}, inplace=True)

    daily_rates["US10Y"] = pd.to_numeric(
        daily_rates["US10Y"], errors="coerce").dropna()
    # Compute the daily change in interest rates
    daily_diff = daily_rates.diff()

    # Compute and print the autocorrelation of daily changes
    autocorrelation_daily = daily_diff["US10Y"].autocorr()
    print("The autocorrelation of daily interest rate changes is %4.2f" %
          (autocorrelation_daily))

    # Convert the daily data to annual data
    yearly_rates = daily_rates.resample(rule="A").last()

    # Repeat above for annual data
    yearly_diff = yearly_rates.diff()
    autocorrelation_yearly = yearly_diff["US10Y"].autocorr()
    print("The autocorrelation of annual interest rate changes is %4.2f" %
          (autocorrelation_yearly))

    daily_rates.plot()
    plt.show()


if __name__ == "__main__":
    sns.set()
    # popular_strategy_using_autocorrelation()
    are_interest_rate_auto_correlated()
