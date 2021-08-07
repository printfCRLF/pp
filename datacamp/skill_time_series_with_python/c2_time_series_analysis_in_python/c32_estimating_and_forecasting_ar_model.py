import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf
from data import get_interest_rate_data


def estimating_an_ar_model():
    ar = np.array([1, -0.9])
    ma = np.array([1])
    ar_process = ArmaProcess(ar, ma)
    simulated_data = ar_process.generate_sample(nsample=1000)

    # Fit an AR(1) model to the first simulated data
    mod = ARMA(simulated_data, order=(1, 0))
    res = mod.fit()

    # Print out summary information on the fit
    print(res.summary())

    # Print out the estimate for the constant and for phi
    print("When the true phi=0.9, the estimate of phi (and the constant) are:")
    print(res.params)

    return simulated_data, res


def forecasting_with_an_ar_model(res):
    res.plot_predict(start=990, end=1010)
    plt.show()


def forecast_interest_data(interest_rate_data):
    # Forecast interest rates using an AR(1) model
    mod = ARMA(interest_rate_data, order=(1, 0))
    res = mod.fit()

    # Plot the original series and the forecasted series
    res.plot_predict(start=0, end="2022")
    plt.legend(fontsize=8)
    plt.show()


def compare_ar_model_with_random_walk(interest_rate_data, simulated_data):
    # Plot the interest rate series and the simulated random walk series side-by-side
    fig, axes = plt.subplots(2, 1)

    # Plot the autocorrelation of the interest rate series in the top plot
    fig = plot_acf(interest_rate_data, alpha=1, lags=12, ax=axes[0])

    # Plot the autocorrelation of the simulated random walk series in the bottom plot
    fig = plot_acf(simulated_data, alpha=1, lags=12, ax=axes[1])

    # Label axes
    axes[0].set_title("Interest Rate Data")
    axes[1].set_title("Simulated Random Walk Data")
    plt.show()


if __name__ == "__main__":
    sns.set()
    simulated_data, res = estimating_an_ar_model()
    # forecasting_with_an_ar_model(res)

    interest_rate_data = get_interest_rate_data()
    forecast_interest_data(interest_rate_data)
    compare_ar_model_with_random_walk(interest_rate_data, simulated_data)
