from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def compute_the_acf():
    HRB = pd.read_csv("data/financial_data/HRB.csv",
                      parse_dates=["Quarter"], index_col="Quarter")
    # Compute the acf array of HRB
    acf_array, confint = acf(HRB, nlags=20, alpha=0.05)
    print("acf", acf_array)
    print("confidence intervals", confint)

    # Plot the acf function
    fig, axes = plt.subplots(2, 1)
    HRB.plot(ax=axes[0], title="Quarterly earnings of HRB")
    plot_acf(HRB, lags=20, alpha=0.05, ax=axes[1])
    plt.show()


def are_we_confident_this_stock_is_mean_reverting():
    MSFT = pd.read_csv("data/financial_data/MSFT.csv",
                       parse_dates=["Date"], index_col="Date")
    returns = MSFT.resample("W").last().pct_change().dropna()
    # Compute and print the autocorrelation of MSFT weekly returns
    autocorrelation = returns['Adj Close'].autocorr()
    print("The autocorrelation of weekly MSFT returns is %4.2f" %
          (autocorrelation))

    # Find the number of observations by taking the length of the returns DataFrame
    nobs = len(returns)

    # Compute the approximate confidence interval
    conf = 1.96/sqrt(nobs)
    print("The approximate confidence interval is +/- %4.2f" % (conf))

    # Plot the autocorrelation function with 95% confidence intervals and 20 lags using plot_acf
    plot_acf(returns, alpha=0.05, lags=20)
    plt.show()

    # Notice that the autocorrelation with lag 1 is significantly negative, but none of the other lags are significantly different from zero


if __name__ == "__main__":
    # compute_the_acf()
    are_we_confident_this_stock_is_mean_reverting()
