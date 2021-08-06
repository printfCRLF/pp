import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_stock_google_data, load_stock_yahoo_data


def shifting_stock_prices_across_time(google):
    # Set data frequency to business daily
    google = google.asfreq('B')
    # Create 'lagged' and 'shifted'
    google['lagged'] = google.Close.shift(periods=-90)
    google['shifted'] = google.Close.shift(periods=90)

    # Plot the google price series
    google.plot()
    plt.show()


def calculating_stock_price_percentage_change(yahoo):
    yahoo["shifted"] = yahoo["price"].shift()

    yahoo["return1"] = yahoo["price"].div(yahoo["shifted"]).sub(1).mul(100)
    yahoo["return2"] = (yahoo["price"] / yahoo["shifted"] - 1) * 100
    yahoo["return3"] = yahoo["price"].pct_change().mul(100)

    yahoo["diff1"] = yahoo["price"].sub(yahoo["shifted"])
    yahoo["diff2"] = yahoo["price"].diff()
    print(yahoo.head())


def calculating_stock_price_difference(yahoo):
    # Created shifted_30 here
    yahoo['shifted_30'] = yahoo.price.shift(30)
    # Subtract shifted_30 from price
    yahoo['change_30'] = yahoo["price"] - yahoo["shifted_30"]
    # Get the 30-day price difference
    yahoo['diff_30'] = yahoo["price"].diff(periods=30)
    # Inspect the last five rows of price
    print(yahoo.tail())
    # Show the value_counts of the difference between change_30 and diff_30
    print(yahoo["diff_30"].sub(yahoo["change_30"]).value_counts())


def plotting_multi_period_returns(google):
    # Create daily_return
    google['daily_return'] = google['Close'].pct_change(periods=1).mul(100)
    # Create monthly_return
    google['monthly_return'] = google['Close'].pct_change(periods=30).mul(100)
    # Create annual_return
    google['annual_return'] = google["Close"].pct_change(periods=360).mul(100)

    # Plot the result
    google.plot(subplots=True)
    plt.show()

    display_histogram_for_returns(google)


def display_histogram_for_returns(google):
    columns = ["daily_return", "monthly_return", "annual_return"]
    fig, axes = plt.subplots(3, 1)

    for i, col in enumerate(columns):
        rets = google[col].dropna().to_numpy()
        low, high = np.percentile(rets, [2.5, 97.5])
        mask = (rets >= low) & (rets <= high)
        within_95 = rets[mask]
        axes[i].hist(x=within_95, bins=20)
        axes[i].set_title(col)

    plt.show()


if __name__ == "__main__":
    sns.set()
    google = load_stock_google_data()
    # shifting_stock_prices_across_time(google)

    yahoo = load_stock_yahoo_data()
    calculating_stock_price_percentage_change(yahoo)
    # calculating_stock_price_difference(yahoo)

    # plotting_multi_period_returns(google)
