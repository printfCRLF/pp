import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from c4_2_build_a_market_cap_weighted_index import create_time_series_of_market_value, calculate_and_plot_composite_index


def visualize_your_index_constituent_correlations():
    stock_prices = pd.read_csv("data/stock_data/stock_data.csv",
                               parse_dates=["Date"], index_col="Date")

    # Inspect stock_prices here
    print(stock_prices.info())

    # Calculate the daily returns
    returns = stock_prices.pct_change()

    # Calculate and print the pairwise correlations
    correlations = returns.corr()
    print(correlations)

    # Plot a heatmap of daily return correlations
    sns.heatmap(correlations, annot=True)
    plt.title("Daily Return Correlations")
    plt.show()


def save_to_excel_worksheets(index):
    stock_prices = pd.read_csv("data/stock_data/stock_data.csv",
                               parse_dates=["Date"], index_col="Date")
    index = index.to_frame("Index")
    # Inspect index and stock_prices
    print(index.info())
    print(stock_prices.info())

    # Join index to stock_prices, and inspect the result
    data = stock_prices.join(index)
    print(data.info())

    # Create index & stock price returns
    returns = data.pct_change()

    # Export data and data as returns to excel
    with pd.ExcelWriter('data/stock_data/data.xls') as writer:
        data.to_excel(excel_writer=writer, sheet_name="data")
        returns.to_excel(excel_writer=writer, sheet_name="returns")


if __name__ == "__main__":
    visualize_your_index_constituent_correlations()
    components, market_cap_series = create_time_series_of_market_value()
    index = calculate_and_plot_composite_index(market_cap_series)
    save_to_excel_worksheets(index)
