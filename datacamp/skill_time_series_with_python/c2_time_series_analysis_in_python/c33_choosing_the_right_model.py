from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARMA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def estimate_order_of_model_pacf():
    # Simulate AR(1) with phi=+0.6
    ma = np.array([1])
    ar = np.array([1, -0.6])
    AR_object = ArmaProcess(ar, ma)
    simulated_data_1 = AR_object.generate_sample(nsample=5000)

    # Plot PACF for AR(1)
    plot_pacf(simulated_data_1, lags=20)
    plt.show()

    # Simulate AR(2) with phi1=+0.6, phi2=+0.3
    ma = np.array([1])
    ar = np.array([1, -0.6, -0.3])
    AR_object = ArmaProcess(ar, ma)
    simulated_data_2 = AR_object.generate_sample(nsample=5000)

    # Plot PACF for AR(2)
    plot_pacf(simulated_data_2, lags=20)
    plt.show()


def estimate_order_of_model_information_criteria():
    ma = np.array([1])
    ar = np.array([1, -0.6, -0.3])
    AR_object = ArmaProcess(ar, ma)
    simulated_data_2 = AR_object.generate_sample(nsample=5000)

    # Fit the data to an AR(p) for p = 0,...,6 , and save the BIC
    BIC = np.zeros(7)
    for p in range(7):
        mod = ARMA(simulated_data_2, order=(p, 0))
        res = mod.fit()
    # Save BIC for AR(p)
        BIC[p] = res.bic

    # Plot the BIC as a function of p
    plt.plot(range(1, 7), BIC[1:7], marker='o')
    plt.xlabel('Order of AR Model')
    plt.ylabel('Bayesian Information Criterion')
    plt.show()


if __name__ == "__main__":
    sns.set()
    # estimate_order_of_model_pacf()
    estimate_order_of_model_information_criteria()
