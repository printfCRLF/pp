import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics import tsaplots


def autocorrelation_in_time_series(co2_levels):
    plt.style.use('fivethirtyeight')
    # Display the autocorrelation plot of your time series
    fig = tsaplots.plot_acf(co2_levels["co2"], lags=24)

    # Show plot
    plt.show()


def partial_autocorrelation_in_time_series(co2_levels): 
    # Display the partial autocorrelation plot of your time series
    fig = tsaplots.plot_pacf(co2_levels["co2"], lags=24)
    # Show plot
    plt.show()


if __name__ == "__main__":
    sns.set()
    co2_levels = pd.read_csv("data/ch2_co2_levels.csv",
                             parse_dates=["datestamp"], index_col="datestamp")
    co2_levels.fillna(method="bfill", inplace=True)
    autocorrelation_in_time_series(co2_levels)
    partial_autocorrelation_in_time_series(co2_levels)
    