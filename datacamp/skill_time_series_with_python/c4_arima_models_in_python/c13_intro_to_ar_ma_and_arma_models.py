import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima_model import ARMA


def generating_arma_data():
    np.random.seed(1)

    # Set coefficients
    ar_coefs = [1]
    ma_coefs = [1, -0.7]
    # Generate data
    y = arma_generate_sample(ar_coefs, ma_coefs, nsample=100, scale=0.5)
    plt.plot(y)
    plt.ylabel(r'$y_t$')
    plt.xlabel(r'$t$')
    plt.show()

    np.random.seed(2)
    # Set coefficients
    ar_coefs = [1, -0.3, -0.2]
    ma_coefs = [1]
    # Generate data
    y = arma_generate_sample(ar_coefs, ma_coefs, nsample=100, scale=0.5)
    plt.plot(y)
    plt.ylabel(r'$y_t$')
    plt.xlabel(r'$t$')
    plt.show()

    np.random.seed(3)
    # Set coefficients
    ar_coefs = [1, 0.2]
    ma_coefs = [1, 0.3, 0.4]
    # Generate data
    y = arma_generate_sample(ar_coefs, ma_coefs, nsample=100, scale=0.5)
    plt.plot(y)
    plt.ylabel(r'$y_t$')
    plt.xlabel(r'$t$')
    plt.show()


def fitting_prelude(y):
    # Instantiate the model
    model = ARMA(y, order=(1, 1))
    # Fit the model
    results = model.fit()


if __name__ == "__main__":
    sns.set()
    generating_arma_data()
    # fitting_prelude(y)
