import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_air_quality_nyc_data, load_stock_yahoo_data, load_co_cities_data


def create_time_series(data):
    # Inspect data
    print(data.info())
    # Convert the date column to datetime64
    data.date = pd.to_datetime(data.date)
    # Set date column as index
    data.set_index("date", inplace=True)
    # Inspect data
    print(data.info())
    # Plot data
    data.plot(subplots=True)
    plt.show()


def compare_annual_stock_price_trend(yahoo):
    # Create dataframe prices here
    prices = pd.DataFrame()

    # Select data for each year and concatenate with prices here
    for year in ["2013", "2014", "2015"]:
        price_per_year = yahoo.loc[year, ["price"]].reset_index(drop=True)
        price_per_year.rename(columns={"price": year}, inplace=True)
        prices = pd.concat([prices, price_per_year], axis=1)

    # Plot prices
    prices.plot()
    plt.show()


def set_and_change_time_series_frequency(co):
    # Inspect data
    print(co.info())
    # Set the frequency to calendar daily
    co = co.asfreq("D")
    # Plot the data
    co.plot(subplots=True)
    plt.show()

    # Set frequency to monthly
    co = co.asfreq("M")
    # Plot the data
    co.plot(subplots=True)
    plt.show()


sns.set()
# air_quality_nyc = load_air_quality_nyc_data()
# create_time_series(air_quality_nyc)

# yahoo = load_stock_yahoo_data()
# compare_annual_stock_price_trend(yahoo)

co = load_co_cities_data()
set_and_change_time_series_frequency(co)
