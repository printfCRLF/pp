from statsmodels.tsa.stattools import adfuller
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def augmented_dicky_fuller_test():
    earthquake = pd.read_csv('data/earthquakes.xls',
                             parse_dates=['date'], index_col='date')

    # Run test
    result = adfuller(earthquake["earthquakes_per_year"])
    # Print test statistic
    print(result[0])
    # Print p-value
    print(result[1])
    # Print critical values
    print(result[4])

    return earthquake


def taking_the_difference(city):
    # Run the ADF test on the time series
    result = adfuller(city["city_population"])

    # Plot the time series
    fig, ax = plt.subplots()
    city.plot(ax=ax)
    plt.show()

    # Print the test statistic and the p-value
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])

    # Calculate the first difference of the time series
    city_stationary = city.diff().dropna()

    # Run ADF test on the differenced time series
    result = adfuller(city_stationary['city_population'])

    # Plot the differenced time series
    fig, ax = plt.subplots()
    city_stationary.plot(ax=ax)
    plt.show()

    # Print the test statistic and the p-value
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])

    # Calculate the second difference of the time series
    city_stationary = city.diff().diff().dropna()

    # Run ADF test on the differenced time series
    result = adfuller(city_stationary['city_population'])

    # Plot the differenced time series
    fig, ax = plt.subplots()
    city_stationary.plot(ax=ax)
    plt.show()

    # Print the test statistic and the p-value
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])


def other_transforms():
    amazon = pd.read_csv("data/amazon_close.xls",
                         parse_dates=['date'], index_col='date')
    # Calculate the first difference and drop the nans
    amazon_diff = amazon.diff()
    amazon_diff = amazon_diff.dropna()

    # Run test and print
    result_diff = adfuller(amazon_diff['close'])
    print(result_diff)

    # Calculate log-return and drop nans
    amazon_log = np.log(amazon_diff.pct_change())
    amazon_log = amazon_log.dropna()

    # Run test and print
    result_log = adfuller(amazon_log['close'])
    print(result_log)


if __name__ == "__main__":
    sns.set()
    earthquake = augmented_dicky_fuller_test()
    # taking_the_difference(city)
    other_transforms()
