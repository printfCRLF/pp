import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def a_thin_application_of_time_series():
    diet = pd.read_csv("my_data/google_search_diet.csv",
                       parse_dates=["Date"], index_col="Date")

    # Plot the entire time series diet and show gridlines
    diet.plot(grid=True)
    plt.show()

    diet2019 = diet["2019"]
    # Plot diet2019 data
    diet2019.plot(grid=True)
    plt.show()


def merging_time_series_with_different_dates():
    stocks = pd.read_csv("data/my_data/SP500.csv",
                         parse_dates=["DATE"], index_col="DATE")
    bonds = pd.read_csv("data/my_data/THREEFY10.csv",
                        parse_dates=["DATE"], index_col="DATE")
    # Convert the stock index and bond index into sets
    set_stock_dates = set(stocks.index)
    set_bond_dates = set(bonds.index)

    # Take the difference between the sets and print
    print(set_stock_dates - set_bond_dates)

    # Merge stocks and bonds DataFrames using join()
    stocks_and_bonds = stocks.join(bonds, how="inner")
    stocks_and_bonds.columns = ["SP500", "US10Y"]
    stocks_and_bonds["SP500"] = pd.to_numeric(
        stocks_and_bonds["SP500"], errors="coerce")
    stocks_and_bonds["US10Y"] = pd.to_numeric(
        stocks_and_bonds["US10Y"], errors="coerce")
    return stocks_and_bonds


if __name__ == "__main__":
    sns.set()
    # a_thin_application_of_time_series()
    stocks_and_bonds = merging_time_series_with_different_dates()
    print(stocks_and_bonds.head())
    print(stocks_and_bonds.info())
