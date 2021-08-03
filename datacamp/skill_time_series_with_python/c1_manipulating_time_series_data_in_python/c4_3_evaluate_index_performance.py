import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from c4_2_build_a_market_cap_weighted_index import create_time_series_of_market_value, calculate_and_plot_composite_index


def calculate_contribution_of_each_stock_to_index(components, index):
    # Calculate and print the index return here
    index_return = ((index.iloc[-1] / index.iloc[0]) - 1) * 100
    print(index_return)

    # Select the market capitalization
    market_cap = components["Market Capitalization"]

    # Calculate the total market cap
    total_market_cap = market_cap.sum()

    # Calculate the component weights, and print the result
    weights = market_cap / total_market_cap
    print(weights.sort_values())

    # Calculate and plot the contribution by component
    weights.mul(index_return).sort_values().plot(kind="barh")
    plt.show()


def compare_index_performance_against_benchmark_1(index):
    # Convert index series to dataframe here
    data = index.to_frame("Index")

    # Normalize djia series and add as new column to data
    djia = pd.read_csv("data/stock_data/djia2.csv",
                       parse_dates=["DATE"], index_col="DATE")
    djia = djia.div(djia.iloc[0]).mul(100)
    data['DJIA'] = djia

    # Show total return for both index and djia
    print(data.iloc[-1].div(data.iloc[0]).sub(1).mul(100))

    # Plot both series
    data.plot()
    plt.show()

    return data


def compare_index_performance_against_benchmark_2(data):
    # Inspect data
    print(data.info())
    print(data.head())

    # Create multi_period_return function here
    def multi_period_return(r):
        return (np.prod(r + 1) - 1) * 100

    # Calculate rolling_return_360
    rolling_return_360 = data.pct_change().rolling("360D").apply(multi_period_return)

    # Plot rolling_return_360 here
    rolling_return_360.plot(title="Rolling 360D Return")
    plt.show()


if __name__ == "__main__":
    components, market_cap_series = create_time_series_of_market_value()
    index = calculate_and_plot_composite_index(market_cap_series)
    calculate_contribution_of_each_stock_to_index(components, index)

    data = compare_index_performance_against_benchmark_1(index)
    compare_index_performance_against_benchmark_2(data)
