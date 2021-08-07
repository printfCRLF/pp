import datetime
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARMA
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_ho_ng_prices_and_differences(HO, NG):
    # Plot the prices separately
    plt.subplot(2, 1, 1)
    plt.plot(7.25*HO, label='Heating Oil')
    plt.plot(NG, label='Natural Gas')
    plt.legend(loc='best', fontsize='small')

    # Plot the spread
    plt.subplot(2, 1, 2)
    plt.plot(7.25*HO-NG, label='Spread')
    plt.legend(loc='best', fontsize='small')
    plt.axhline(y=0, linestyle='--', color='k')
    plt.show()


def price_is_random_walk_but_not_difference(HO, NG):
    # Compute the ADF for HO and NG
    result_HO = adfuller(HO["Close"])
    print("The p-value for the ADF test on HO is ", result_HO[1])
    result_NG = adfuller(NG['Close'])
    print("The p-value for the ADF test on NG is ", result_NG[1])

    # Compute the ADF of the spread
    result_spread = adfuller(7.25 * HO["Close"] - NG["Close"])
    print("The p-value for the ADF test on the spread is ", result_spread[1])


def are_bitcoin_and_ethereum_cointegrated():
    BTC = pd.read_csv("data/my_data/Bitcoin Historical Data.csv",
                      parse_dates=["Date"], index_col="Date", usecols=[0, 1])
    BTC["Price"] = BTC["Price"].str.replace(',', '').astype(float)
    ETH = pd.read_csv("data/my_data/Ethereum Historical Data.csv",
                      parse_dates=["Date"], index_col="Date", usecols=[0, 1])
    ETH["Price"] = ETH["Price"].str.replace(',', '').astype(float)

    # Regress BTC on ETH
    ETH = sm.add_constant(ETH)
    result = sm.OLS(BTC, ETH).fit()

    # Compute ADF
    b = result.params[1]
    adf_stats = adfuller(BTC['Price'] - b*ETH['Price'])
    print("The p-value for the ADF test is ", adf_stats[1])


if __name__ == "__main__":
    sns.set()
    HO = pd.read_csv("data/financial_data/CME_HO1.csv",
                     parse_dates=["Date"], index_col="Date")
    NG = pd.read_csv("data/financial_data/CME_NG1.csv",
                     parse_dates=["Date"], index_col="Date")
    # plot_ho_ng_prices_and_differences(HO, NG)
    # price_is_random_walk_but_not_difference(HO, NG)

    are_bitcoin_and_ethereum_cointegrated()
