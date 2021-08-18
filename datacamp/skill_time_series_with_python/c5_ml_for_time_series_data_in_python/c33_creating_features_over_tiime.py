import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import percent_change
from functools import partial


def engineering_multiple_rolling_features_at_once():
    df = pd.read_csv("data/prices.csv", parse_dates=["date"], index_col="date")
    mask = df["symbol"].isin(["EBAY"])
    df = df[mask]
    prices = df.pivot_table(values="close", index=df.index, columns="symbol")
    prices_perc = prices.rolling(20).apply(percent_change)["EBAY"]

    # Define a rolling window with Pandas, excluding the right-most datapoint of the window
    prices_perc_rolling = prices_perc.rolling(
        20, min_periods=5, closed='right')

    # Define the features you'll calculate for each window
    features_to_calculate = [np.min, np.max, np.mean, np.std]

    # Calculate these features for your rolling window object
    features = prices_perc_rolling.aggregate(features_to_calculate)

    # Plot the results
    ax = features.loc[:"2011-01"].plot()
    prices_perc.loc[:"2011-01"].plot(ax=ax, color='k', alpha=.2, lw=3)
    ax.legend(loc=(1.01, .6))
    plt.show()

    return prices_perc


def percentiles_and_partial_functions(prices_perc):
    percentiles = [1, 10, 25, 50, 75, 90, 99]

    # Use a list comprehension to create a partial function for each quantile
    percentile_functions = [partial(np.percentile, q=percentile)
                            for percentile in percentiles]

    # Calculate each of these quantiles on the data using a rolling window
    prices_perc_rolling = prices_perc.rolling(
        20, min_periods=5, closed='right')
    features_percentiles = prices_perc_rolling.aggregate(percentile_functions)

    # Plot a subset of the result
    ax = features_percentiles.loc[:"2011-01"].plot(cmap=plt.cm.viridis)
    ax.legend(percentiles, loc=(1.01, .5))
    plt.show()


def using_date_info():
    # Extract date features from the data, add them as columns
    prices_perc['day_of_week'] = prices_perc.index.dayofweek
    prices_perc['week_of_year'] = prices_perc.index.weekofyear
    prices_perc['month_of_year'] = prices_perc.index.month

    # Print prices_perc
    print(prices_perc)


if __name__ == "__main__":
    sns.set()
    prices_perc = engineering_multiple_rolling_features_at_once()
    percentiles_and_partial_functions(prices_perc)
