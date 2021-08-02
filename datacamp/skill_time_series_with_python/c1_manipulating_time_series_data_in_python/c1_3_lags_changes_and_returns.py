import pandas as pd
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


def calculating_stock_price_change(yahoo):
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


sns.set()
google = load_stock_google_data()
# shifting_stock_prices_across_time(google)

# yahoo = load_stock_yahoo_data()
# calculating_stock_price_change(yahoo)

plotting_multi_period_returns(google)
