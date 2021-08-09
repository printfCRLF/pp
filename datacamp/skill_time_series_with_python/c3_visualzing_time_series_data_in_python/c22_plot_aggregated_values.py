import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def display_rolling_averages(co2_levels):
    # Compute the 52 weeks rolling mean of the co2_levels DataFrame
    ma = co2_levels.rolling(window=52).mean()

    # Compute the 52 weeks rolling standard deviation of the co2_levels DataFrame
    mstd = co2_levels.rolling(window=52).std()

    # Add the upper bound column to the ma DataFrame
    ma['upper'] = ma['co2'] + (2 * mstd["co2"])

    # Add the lower bound column to the ma DataFrame
    ma['lower'] = ma['co2'] - (2 * mstd["co2"])

    # Plot the content of the ma DataFrame
    ax = ma.plot(linewidth=0.8, fontsize=6)

    # Specify labels, legend, and show the plot
    ax.set_xlabel('Date', fontsize=10)
    ax.set_ylabel('CO2 levels in Mauai Hawaii', fontsize=10)
    ax.set_title(
        'Rolling mean and variance of CO2 levels\nin Mauai Hawaii from 1958 to 2001', fontsize=10)
    plt.show()


def display_aggregated_value(co2_levels):
    # Get month for each dates in the index of co2_levels
    index_month = co2_levels.index.month
    # Compute the mean CO2 levels for each month of the year
    mean_co2_levels_by_month = co2_levels.groupby(index_month).mean()
    # Plot the mean CO2 levels for each month of the year
    mean_co2_levels_by_month.plot(fontsize=6)
    # Specify the fontsize on the legend
    plt.legend(fontsize=10)
    # Show plot
    plt.show()


if __name__ == "__main__":
    sns.set()
    co2_levels = pd.read_csv("data/ch2_co2_levels.csv",
                             parse_dates=["datestamp"], index_col="datestamp")
    co2_levels.fillna(method="bfill", inplace=True)

    display_rolling_averages(co2_levels)
    display_aggregated_value(co2_levels)
