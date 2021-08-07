from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import ArmaProcess
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def simulate_ar1_time_series():
    # Plot 1:  AR parameter = +0.9
    plt.subplot(2, 1, 1)
    ar1 = np.array([1, -0.9])
    ma1 = np.array([1])
    AR_object1 = ArmaProcess(ar1, ma1)
    simulated_data_1 = AR_object1.generate_sample(nsample=1000)
    plt.plot(simulated_data_1)

    # Plot 1:  AR parameter = -0.9
    plt.subplot(2, 1, 2)
    ar2 = np.array([1, 0.9])
    ma2 = np.array([1])
    AR_object2 = ArmaProcess(ar2, ma2)
    simulated_data_2 = AR_object2.generate_sample(nsample=1000)
    plt.plot(simulated_data_2)

    plt.show()


def compare_the_acf_for_several_ar_time_series():
    ar_parameters = [0.9, -0.9, 0.3]
    fig, axes = plt.subplots(3, 1, sharex=True)

    for i, p in enumerate(ar_parameters):
        ar = np.array([1, -p])
        ma = np.array([1])
        ar_object = ArmaProcess(ar, ma)
        simulated_data = ar_object.generate_sample(nsample=1000)

        plot_acf(simulated_data, ax=axes[i])
        axes[i].set_title("AR parameter φ = %4.2f" % (p))

    fig.suptitle("Comparison of ACF")
    plt.show()


if __name__ == "__main__":
    sns.set()
    # simulate_ar1_time_series()
    compare_the_acf_for_several_ar_time_series()
