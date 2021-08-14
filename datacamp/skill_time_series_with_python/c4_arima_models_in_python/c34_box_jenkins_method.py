import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data import load_savings_data


def identification(savings):
    # Plot time series
    savings.plot()
    plt.show()
    # Run Dicky-Fuller test
    result = adfuller(savings)
    # Print test statistic
    print("test statistics - critical value: ", result[0])
    # Print p-value
    print("test statistics - p-value: ", result[1])


def identification2(savings):
    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    # Plot the ACF of savings on ax1
    plot_acf(savings, lags=10, zero=False, ax=ax1)
    # Plot the PACF of savings on ax2
    plot_pacf(savings, lags=10, zero=False, ax=ax2)
    plt.show()


def estimation(savings):
    for p in range(4):
        for q in range(4):
            try:
                # Create and fit ARMA(p,q) model
                model = SARIMAX(savings, order=(p, 0, q), trend="c")
                results = model.fit(full_output=False, disp=False)
                # Print p, q, AIC, BIC
                print(p, q, results.aic, results.bic)
            except:
                print(p, q, None, None)


def diagnostics(savings):
    # Create and fit model
    model = SARIMAX(savings, order=(1, 0, 2), trend="c")
    results = model.fit()
    # Create the 4 diagostics plots
    results.plot_diagnostics()
    plt.show()
    # Print summary
    print(results.summary())


if __name__ == "__main__":
    sns.set()
    savings = load_savings_data()
    # identification(savings)
    # identification2(savings)
    # estimation(savings)
    diagnostics(savings)
