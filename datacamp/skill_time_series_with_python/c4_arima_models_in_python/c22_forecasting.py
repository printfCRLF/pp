import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA


def generating_one_step_ahead_predictions(results):
    # Generate predictions
    one_step_forecast = results.get_prediction(start=-30)

    # Extract prediction mean
    mean_forecast = one_step_forecast.predicted_mean

    # Get confidence intervals of  predictions
    confidence_intervals = one_step_forecast.conf_int()

    # Select lower and upper confidence limits
    lower_limits = confidence_intervals.loc[:, 'lower close']
    upper_limits = confidence_intervals.loc[:, 'upper close']

    # Print best estimate  predictions
    print(mean_forecast)

    return mean_forecast, lower_limits, upper_limits


def plotting_one_step_ahead_prediction(amazon, mean_forecast, lower_limits, upper_limits):
    # plot the amazon data
    plt.plot(amazon.index, amazon, label='observed')

    # plot your mean predictions
    plt.plot(mean_forecast.index, mean_forecast, color='r', label='forecast')

    # shade the area between your confidence limits
    plt.fill_between(mean_forecast.index, lower_limits,
                     upper_limits, color='pink')

    # set labels, legends and show plot
    plt.xlabel('Date')
    plt.ylabel('Amazon Stock Price - Close USD')
    plt.legend()
    plt.show()


def generating_dynamic_forecasts(results):
    # Generate predictions
    dynamic_forecast = results.get_prediction(start=-30, dynamic=True)

    # Extract prediction mean
    mean_forecast = dynamic_forecast.predicted_mean

    # Get confidence intervals of predictions
    confidence_intervals = dynamic_forecast.conf_int()

    # Select lower and upper confidence limits
    lower_limits = confidence_intervals.loc[:, 'lower close']
    upper_limits = confidence_intervals.loc[:, 'upper close']

    # Print best estimate predictions
    print(mean_forecast)


def plotting_dynamic_forecasts(amazon, mean_forecast, lower_limits, upper_limits):
    # plot the amazon data
    plt.plot(amazon.index, amazon, label='observed')

    # plot your mean forecast
    plt.plot(mean_forecast.index, mean_forecast, color='r', label='forecast')

    # shade the area between your confidence limits
    plt.fill_between(mean_forecast.index, lower_limits,
                     upper_limits, color='pink')

    # set labels, legends and show plot
    plt.xlabel('Date')
    plt.ylabel('Amazon Stock Price - Close USD')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sns.set()
    results = {}
    amazon, mean_forecast, lower_limits, upper_limits = generating_one_step_ahead_predictions(
        results)
    plotting_one_step_ahead_prediction(
        amazon, mean_forecast, lower_limits, upper_limits)
    generating_dynamic_forecasts(results)
    plotting_dynamic_forecasts(amazon, mean_forecast,
                               lower_limits, upper_limits)
