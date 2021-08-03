import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def explore_and_clean_company_listing_info():
    listings = pd.read_csv("data/stock_data/listings.csv")
    listings["Exchange"] = "amex"
    # Inspect listings
    print(listings.info())

    # Move 'stock symbol' into the index
    listings.set_index("Stock Symbol", inplace=True)
    # Drop rows with missing 'sector' data
    listings.dropna(subset=["Sector"], inplace=True)
    # Select companies with IPO Year before 2019
    listings = listings[listings["IPO Year"] < 2019]
    # Inspect the new listings data
    print(listings.info())
    # Show the number of companies per sector
    print(listings.groupby("Sector").size().sort_values(ascending=False))

    return listings


def select_and_inspect_index_component(listings):
    # Select largest company for each sector
    components = listings.groupby(
        "Sector")["Market Capitalization"].nlargest(1)

    # Print components, sorted by market cap
    print(components.sort_values(ascending=False))

    # Select stock symbols and print the result
    tickers = components.index.get_level_values("Stock Symbol")
    print(tickers)

    # Print company name, market cap, and last price for each component
    info_cols = ["Company Name", "Market Capitalization", "Last Sale"]
    print(listings.loc[tickers, info_cols].sort_values(
        by="Market Capitalization", ascending=False))

    return tickers


def import_index_component_price_information():
    tickers = ['RIO', 'ILMN', 'CPRT', 'EL', 'AMZN',
               'PAA', 'GS', 'AMGN', 'MA', 'TEF', 'AAPL', 'UPS']

    # Import prices and inspect result
    stock_prices = pd.read_csv(
        "data/stock_data/stock_data.csv", parse_dates=["Date"], index_col="Date")
    print(stock_prices.info())

    # Calculate the returns
    price_return = (stock_prices.iloc[-1, ] /
                    stock_prices.iloc[0, ]).sub(1).mul(100)

    # Plot horizontal bar chart of sorted price_return
    price_return.sort_values().plot(kind="barh", title="Stock Price Returns")
    plt.show()


sns.set()
listings = explore_and_clean_company_listing_info()
select_and_inspect_index_component(listings)
# import_index_component_price_information()
