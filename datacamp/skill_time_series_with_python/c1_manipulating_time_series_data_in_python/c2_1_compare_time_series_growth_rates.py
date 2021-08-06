import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


def compare_performances_of_several_asset_classes():
    prices = pd.read_csv("data/stock_data/asset_classes.csv",
                         parse_dates=["DATE"], index_col="DATE")

    # Inspect prices here
    print(prices.info())
    # Select first prices
    first_prices = prices.iloc[0]
    # Create normalized
    normalized = prices.div(first_prices).mul(100)

    # Plot normalized
    normalized.plot()
    plt.show()


def comparing_stock_prices_with_a_benchmark():
    stocks = pd.read_csv("data/stock_data/nyse.csv",
                         parse_dates=["date"], index_col="date")
    dow_jones = pd.read_csv("data/stock_data/dow_jones.csv",
                            parse_dates=["date"], index_col="date")

    # Concatenate data and inspect result here
    data = pd.concat([stocks, dow_jones], axis=1)
    print(data.info())

    # Normalize and plot your data here
    first_value = data.iloc[0]
    data.div(first_value).mul(100).plot()

    plt.show()


def plot_performance_difference_vs_index():
    # Create tickers
    tickers = ["AAPL", "MSFT"]

    # Import stock data here
    stocks = pd.read_csv("data/stock_data/msft_aapl.csv", parse_dates=[
                         "date"], index_col="date")

    # Import index here
    sp500 = pd.read_csv("data/stock_data/sp500.csv",
                        parse_dates=["date"], index_col="date")

    # Concatenate stocks and index here
    data = pd.concat([stocks, sp500], axis=1).dropna()

    # Normalize data
    normalized = data.div(data.iloc[0]).mul(100)

    # Subtract the normalized index from the normalized stock prices, and plot the result
    normalized[tickers].sub(normalized["SP500"], axis=0).plot()
    plt.show()
    relative_pfm = normalized[tickers].sub(normalized["SP500"], axis=0)
    relative_pfm.columns = ["AAPL_REL", "MSFT_REL"]
    joined = pd.concat([normalized, relative_pfm], axis=1)
    print(joined.head())


if __name__ == "__main__":
    # compare_performances_of_several_asset_classes()
    # comparing_stock_prices_with_a_benchmark()
    plot_performance_difference_vs_index()
