import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX


def differencing_and_fitting_arma_model():
    amazon = pd.read_csv("data/amazon_close.xls",
                         parse_dates=['date'], index_col='date')

    # Take the first difference of the data
    amazon_diff = amazon.diff().dropna()
    # Create ARMA(2,2) model
    arma = SARIMAX(amazon_diff, order=(2, 0, 2))
    # Fit model
    arma_results = arma.fit()
    # Print fit summary
    print(arma_results.summary())

    return amazon, arma_results


def unrolling_arma_forecast(amazon, arma_results):
    # Make arma forecast of next 10 differences
    arma_diff_forecast = arma_results.get_forecast(steps=10).predicted_mean

    # Integrate the difference forecast
    arma_int_forecast = np.cumsum(arma_diff_forecast)

    # Make absolute value forecast
    arma_value_forecast = arma_int_forecast + amazon.iloc[-1, 0]

    # Print forecast
    print(arma_value_forecast)


def fitting_an_arima_model(amazon):
    # Create ARIMA(2,1,2) model
    arima = SARIMAX(amazon, order=(2, 1, 2))

    # Fit ARIMA model
    arima_results = arima.fit()

    # Make ARIMA forecast of next 10 values
    arima_value_forecast = arima_results.get_forecast(steps=10).predicted_mean

    # Print forecast
    print(arima_value_forecast)


if __name__ == "__main__":
    sns.set()
    amazon, arma_results = differencing_and_fitting_arma_model()
    unrolling_arma_forecast(amazon, arma_results)
    fitting_an_arima_model(amazon)
