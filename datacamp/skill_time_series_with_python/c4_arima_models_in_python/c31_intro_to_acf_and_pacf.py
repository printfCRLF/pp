import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def ar_or_ma(df):
    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot the ACF of df
    plot_acf(df, lags=10, zero=False, ax=ax1)

    # Plot the PACF of df
    plot_pacf(df, lags=10, zero=False, ax=ax2)

    plt.show()


def order_of_earthquake():
    earthquake = pd.read_csv('data/earthquakes.xls', usecols=[0, 2],
                             parse_dates=['date'], index_col='date')
    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    # Plot ACF and PACF
    plot_acf(earthquake, lags=15, zero=False, ax=ax1)
    plot_pacf(earthquake, lags=15, zero=False, ax=ax2)
    # Show plot
    plt.show()

    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot ACF and PACF
    plot_acf(earthquake, lags=10, zero=False, ax=ax1)
    plot_pacf(earthquake, lags=10, zero=False, ax=ax2)

    # Show plot
    plt.show()

    # Instantiate model
    model = SARIMAX(earthquake, order=(1, 0, 0))

    # Train model
    results = model.fit()
    print(results.summary())


if __name__ == "__main__":
    sns.set()
    # ar_or_ma()
    order_of_earthquake()
