import datetime
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARMA
from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def high_frequency_stock_prices():
    intraday = pd.read_csv(
        "data/financial_data/Sprint_intraday.txt", header=None, usecols=[0, 1])
    # Change the first date to zero
    intraday.iloc[0, 0] = 0
    # Change the column headers to 'DATE' and 'CLOSE'
    intraday.columns = ["DATE", "CLOSE"]
    # Examine the data types for each column
    print(intraday.dtypes)
    # Convert DATE column to numeric
    intraday['DATE'] = pd.to_numeric(intraday['DATE'])
    # Make the `DATE` column the new index
    intraday = intraday.set_index("DATE")

    return intraday


def cleaning_missing_data(intraday):
    # Notice that some rows are missing
    print("If there were no missing rows, there would be 391 rows of minute data")
    print("The actual length of the DataFrame is:", len(intraday))

    # Everything
    set_everything = set(range(391))
    # The intraday index as a set
    set_intraday = set(intraday.index)
    # Calculate the difference
    set_missing = set_everything - set_intraday
    # Print the difference
    print("Missing rows: ", set_missing)

    # Fill in the missing rows
    intraday = intraday.reindex(range(391), method="ffill")

    # From previous step
    intraday = intraday.reindex(range(391), method='ffill')

    # Change the index to the intraday times
    intraday.index = pd.date_range(
        start='2017-09-01 9:30', end='2017-09-01 16:00', freq="1min")

    # Plot the intraday time series
    intraday.plot(grid=True)
    plt.show()

    return intraday


def applying_an_ma_model(intraday):
    # Compute returns from prices and drop the NaN
    returns = intraday.pct_change()
    returns = returns.dropna()

    # Plot ACF of returns with lags up to 60 minutes
    plot_acf(returns, lags=60)
    plt.show()

    # Fit the data to an MA(1) model
    mod = ARMA(returns, order=(0, 1))
    res = mod.fit()
    print(res.params)


def equivalence_of_ar1_and_ma_infinity(intraday):
    # Build a list MA parameters
    ma = [0.8**i for i in range(30)]

    # Simulate the MA(30) model
    ar = np.array([1])
    AR_object = ArmaProcess(ar, ma)
    simulated_data = AR_object.generate_sample(nsample=5000)

    # Plot the ACF
    plot_acf(simulated_data, lags=30)
    plt.show()


if __name__ == "__main__":
    sns.set()
    intraday = high_frequency_stock_prices()
    intraday = cleaning_missing_data(intraday)
    applying_an_ma_model(intraday)
    equivalence_of_ar1_and_ma_infinity(intraday)
