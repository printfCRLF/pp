from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def cannot_forecast_white_noise():
    returns = np.random.normal(loc=0.02, scale=0.05, size=1000)

    # Print out the mean and standard deviation of returns
    mean = np.mean(returns)
    std = np.std(returns)
    print("The mean is %5.3f and the standard deviation is %5.3f" % (mean, std))

    fig, axes = plt.subplots(2, 1)
    # Plot returns series
    axes[0].plot(returns)
    axes[0].set_title("Returns from a normal distribution")

    # Plot autocorrelation function of white noise returns
    plot_acf(returns, lags=20, ax=axes[1])
    plt.show()

    plot_acf


if __name__ == "__main__":
    cannot_forecast_white_noise()
