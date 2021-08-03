from c4_1_explore_and_clearn_company_listing_information import explore_and_clean_company_listing_info, select_and_inspect_index_component
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def calculating_number_of_shares_outstanding(listings, tickers):
    # Inspect listings and print tickers
    print(listings.info())
    print(tickers)

    # Select components and relevant columns from listings
    components = listings.loc[tickers, ["Market Capitalization", "Last Sale"]]
    # Print the first rows of components
    print(components.head())
    # Calculate the number of shares here
    no_shares = components["Market Capitalization"] / components["Last Sale"]
    # Print the sorted no_shares
    print(no_shares.sort_values(ascending=False))


def create_time_series_of_market_value():
    market_capitalization = np.array([70431.47689512,  25409.384,  13620.9228694,  31122.51001104,
                                      422138.53062606,  22223.00141568,  88840.59047748, 118927.21053531,
                                      123330.089602,  54609.8060916, 740024.467,  90180.88675596])
    last_sale = np.array([38.94, 173.68,  29.65,  84.94, 884.67,  30.72, 223.32, 161.61,
                          111.22,  10.84, 141.05, 103.74])

    number_of_shares = np.array([1808.717948,  146.3,  459.390316,  366.405816,  477.170618,
                                 723.404994,  397.817439,  735.890171, 1108.8841, 5037.80499,
                                 5246.54,  869.297154])

    stock_symbol = np.array(['RIO', 'ILMN', 'CPRT', 'EL', 'AMZN',
                             'PAA', 'GS', 'AMGN', 'MA', 'TEF', 'AAPL', 'UPS'])

    components = pd.DataFrame({"Market Capitalization": market_capitalization,
                               "Last Sale": last_sale,
                               "Number of Shares": number_of_shares
                               }, index=stock_symbol)

    stock_prices = pd.read_csv(
        "data/stock_data/stock_data.csv", parse_dates=["Date"], index_col="Date")
    stock_prices.fillna(method="ffill", inplace=True)

    # Select the number of shares
    no_shares = components["Number of Shares"]
    print(no_shares.sort_values())

    # Create the series of market cap per ticker
    market_cap = stock_prices.mul(no_shares)

    # Select first and last market cap here
    first_value = market_cap.iloc[0, :]
    last_value = market_cap.iloc[-1, :]

    # Concatenate and plot first and last market cap here
    pd.concat([first_value, last_value], axis=1).plot(kind="barh")
    plt.show()

    return components, market_cap


def calculate_and_plot_composite_index(market_cap_series):
    # Aggregate and print the market cap per trading day
    raw_index = market_cap_series.sum(axis=1)
    print(raw_index)

    # Normalize the aggregate market cap here
    index = raw_index.div(raw_index.iloc[0]).mul(100)
    print(index)

    # Plot the index here
    index.plot(title="Market-Cap Weighted Index")
    plt.show()

    return index


if __name__ == "__main__":
    # listings = explore_and_clean_company_listing_info()
    # tickers = select_and_inspect_index_component(listings)
    # calculating_number_of_shares_outstanding(listings, tickers)

    components, market_cap_series = create_time_series_of_market_value()
    calculate_and_plot_composite_index(market_cap_series)
