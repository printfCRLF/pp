import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


def time_series_decomposition(co2_levels):
    # Perform time series decompositon
    decomposition = sm.tsa.seasonal_decompose(co2_levels)
    # Print the seasonality component
    print(decomposition.seasonal)

    return decomposition


def plot_individual_components(decomposition):
    # Extract the trend component
    trend = decomposition.trend

    # Plot the values of the trend
    ax = trend.plot(figsize=(12, 6), fontsize=6)

    # Specify axis labels
    ax.set_xlabel('Date', fontsize=10)
    ax.set_title('Seasonal component the CO2 time-series', fontsize=10)
    plt.show()


if __name__ == "__main__":
    sns.set()
    co2_levels = pd.read_csv("data/ch2_co2_levels.csv",
                             parse_dates=["datestamp"], index_col="datestamp")
    co2_levels.fillna(method="bfill", inplace=True)
    decomposition = time_series_decomposition(co2_levels)
    plot_individual_components(decomposition)
