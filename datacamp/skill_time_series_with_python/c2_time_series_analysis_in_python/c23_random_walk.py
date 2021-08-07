from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def generate_a_random_walk():
    # Generate 500 random steps with mean=0 and standard deviation=1
    steps = np.random.normal(loc=0, scale=1, size=500)

    # Set first element to 0 so that the first price will be the starting stock price
    steps[0] = 0

    # Simulate stock prices, P with a starting price of 100
    P = 100 + np.cumsum(steps)

    # Plot the simulated stock prices
    plt.plot(P)
    plt.title("Simulated Random Walk")
    plt.show()


def generate_a_random_walk_for_stock_returns():
    # Generate 500 random steps
    steps = np.random.normal(loc=0.001, scale=0.01, size=500) + 1

    # Set first element to 1
    steps[0] = 1

    # Simulate the stock price, P, by taking the cumulative product
    P = 100 * np.cumprod(steps)

    # Plot the simulated stock prices
    plt.plot(P)
    plt.title("Simulated Random Walk with Drift")
    plt.show()


def are_stock_prices_a_random_walk():
    AMZN = pd.read_csv("data/financial_data/AMZN.csv",
                       parse_dates=["Date"], index_col="Date")
    # Run the ADF test on the price series and print out the results
    results = adfuller(AMZN["Adj Close"])
    print(results)

    # Just print out the p-value
    print('The p-value of the test on prices is: ' + str(results[1]))

    # a low p-value (say less than 5%) means we can reject  the null hypothesis that the series is a random walk.


def how_about_stock_returns():
    AMZN = pd.read_csv("data/financial_data/AMZN.csv",
                       parse_dates=["Date"], index_col="Date")
    # Create a DataFrame for AMZN returns
    AMZN_ret = AMZN.pct_change()
    # Eliminate the NaN in the first row of returns
    AMZN_ret = AMZN_ret.dropna()
    # Run the ADF test on the return series and print out the p-value
    results = adfuller(AMZN_ret["Adj Close"])
    print("The p-value of the test on return is: ", str(results[1]))

    # it appears that the return do not follow a random walk


if __name__ == "__main__":
    sns.set()
    # generate_a_random_walk()
    # generate_a_random_walk_for_stock_returns()
    are_stock_prices_a_random_walk()
    how_about_stock_returns()
