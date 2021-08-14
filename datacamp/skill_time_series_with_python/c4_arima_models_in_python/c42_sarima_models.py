import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data import load_australia_employment_data


def fitting_sarima_models(df1, df2, df3):
    # Create a SARIMAX model
    model = SARIMAX(df1, order=(1, 0, 0), seasonal_order=(1, 1, 0, 7))
    # Fit the model
    results = model.fit()
    # Print the results summary
    print(results.summary())

    # Create a SARIMAX model
    model = SARIMAX(df2, order=(2, 1, 1), seasonal_order=(1, 0, 0, 4))
    # Fit the model
    results = model.fit()
    # Print the results summary
    print(results.summary())

    # Create a SARIMAX model
    model = SARIMAX(df3, order=(1, 1, 0), seasonal_order=(0, 1, 1, 12))
    # Fit the model
    results = model.fit()
    # Print the results summary
    print(results.summary())


def choosing_sarima_order(aus_employment):
    # Take the first and seasonal differences and drop NaNs
    aus_employment_diff = aus_employment.diff().diff(12).dropna()

    # Create the figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    # Plot the ACF on ax1
    plot_acf(aus_employment_diff, lags=11, zero=False, ax=ax1)
    # Plot the PACF on ax2
    plot_pacf(aus_employment_diff, lags=11, zero=False, ax=ax2)
    plt.show()

    # Make list of lags
    lags = [12, 24, 36, 48, 60]
    # Create the figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    # Plot the ACF on ax1
    plot_acf(aus_employment_diff, lags=lags, zero=False, ax=ax1)
    # Plot the PACF on ax2
    plot_pacf(aus_employment_diff, lags=lags, zero=False, ax=ax2)
    plt.show()


def sarima_vs_arima_forecasts(aus_employment):
    arima = SARIMAX(aus_employment, order=(3, 1, 2))
    arima_results = arima.fit()
    sarima = SARIMAX(aus_employment, order=(
        1, 1, 1), seasonal_order=(1, 1, 1, 12))
    sarima_results = sarima.fit()
    # Create ARIMA mean forecast
    arima_pred = arima_results.get_forecast(steps=25)
    arima_mean = arima_pred.predicted_mean

    # Create SARIMA mean forecast
    sarima_pred = sarima_results.get_forecast(steps=25)
    sarima_mean = sarima_pred.predicted_mean

    # Plot mean ARIMA and SARIMA predictions and observed
    plt.plot(aus_employment.index[-25:], sarima_mean, label='SARIMA')
    plt.plot(aus_employment.index[-25:], arima_mean, label='ARIMA')
    plt.plot(aus_employment[-25:], label='observed')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sns.set()
    # fitting_sarima_models(df1, df2, df3)
    aus_employment = load_australia_employment_data()
    # choosing_sarima_order(aus_employment)
    sarima_vs_arima_forecasts(aus_employment)
