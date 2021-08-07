import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_lag_one_autocorrelation():
    s1 = pd.Series([1, 3, 4.5, 8, 8.2, 10, 9])
    s2 = pd.Series([5, 3.3, 5.3, 3, 7, 3, 5])

    s1_shifted = s1.shift()
    s2_shifted = s2.shift()

    fig, axes = plt.subplots(2, 1, sharex=True)
    axes[0].plot(s1, color="red")
    axes[0].plot(s1_shifted, color="blue")
    axes[0].set_title("Positive autocorrelation - trending")

    axes[1].plot(s2, color="red")
    axes[1].plot(s2_shifted, color="blue")
    axes[1].set_title(
        "Negative autocorrelation - mean-reverting")

    plt.show()


def popular_strategy_using_autocorrelation():
    MSFT = pd.read_csv("data/financial_data/MSFT.csv",
                       parse_dates=["Date"], index_col="Date")
    periods = {"weekly": "W", "monthly": "M", "yearly": "A"}
    fig, axes = plt.subplots(3, 1, sharex=True)

    for i, (key, value) in enumerate(periods.items()):
        resampled = MSFT.resample(rule=value).last()
        returns = resampled.pct_change()

        # Compute and print the autocorrelation of returns
        autocorrelation = returns["Adj Close"].autocorr()
        print(f"The autocorrelation of {key} returns is %4.2f" % (
            autocorrelation))

        resampled.plot(
            ax=axes[i], title=f"MSFT {key}, autocorrelation is %4.2f" % (autocorrelation))

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
    # plot_lag_one_autocorrelation()
    popular_strategy_using_autocorrelation()
    # are_interest_rate_auto_correlated()
