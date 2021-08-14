import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data import load_co2_data


def sarima_model_diagnostics(co2):
    # Create model object
    model = SARIMAX(co2,
                    order=(1, 1, 1),
                    seasonal_order=(0, 1, 1, 12),
                    trend="c")
    # Fit model
    results = model.fit()

    # Plot common diagnostics
    results.plot_diagnostics()
    plt.show()

    return results


def sarima_forecase(results, co2):
    # Create forecast object
    forecast_object = results.get_forecast(steps=136)
    # Extract prediction mean
    mean = forecast_object.predicted_mean
    # Extract the confidence intervals
    conf_int = forecast_object.conf_int()
    # Extract the forecast dates
    dates = mean.index

    plt.figure()
    # Plot past CO2 levels
    plt.plot(co2.index, co2, label='past')
    # Plot the prediction means as line
    plt.plot(dates, mean, label='predicted')
    # Shade between the confidence intervals
    plt.fill_between(
        dates, conf_int.iloc[:, 0], conf_int.iloc[:, 1], alpha=0.2)
    # Plot legend and show figure
    plt.legend()
    plt.show()

    plt.figure()
    # Plot past CO2 levels
    plt.plot(co2.index, co2, label='past')
    # Plot the prediction means as line
    plt.plot(dates, mean, label='predicted')
    # Shade between the confidence intervals
    plt.fill_between(
        dates, conf_int.iloc[:, 0], conf_int.iloc[:, 1], alpha=0.2)
    # Plot legend and show figure
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sns.set()
    co2 = load_co2_data()
    results = sarima_model_diagnostics(co2)
    sarima_forecase(results, co2)
