from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def simulate_ma2_time_series():
    fig, axes = plt.subplots(3, 1)

    ar = np.array([1])
    ma = np.array([1, -0.9, -0.5])
    arma = ArmaProcess(ar, ma)
    simulated = arma.generate_sample(nsample=1000)
    axes[0].plot(simulated)
    axes[0].set_title("AR(1, 0), MA(2, [0.9, 0.8])")
    plot_acf(simulated, ax=axes[1])
    plot_pacf(simulated, ax=axes[2])
    plt.show()


def simulate_ma1_time_series():
    # Plot 1: MA parameter = -0.9
    plt.subplot(2, 1, 1)
    ar1 = np.array([1])
    ma1 = np.array([1, -0.9])
    MA_object1 = ArmaProcess(ar1, ma1)
    simulated_data_1 = MA_object1.generate_sample(nsample=1000)
    plt.plot(simulated_data_1)

    # Plot 2: MA parameter = +0.9
    plt.subplot(2, 1, 2)
    ar2 = np.array([1])
    ma2 = np.array([1, 0.9])
    MA_object2 = ArmaProcess(ar2, ma2)
    simulated_data_2 = MA_object2.generate_sample(nsample=1000)
    plt.plot(simulated_data_2)

    plt.show()

    return simulated_data_1, simulated_data_2


def compute_acf_for_several_ma_time_series(simulated_data_1, simulated_data_2):
    # Plot 1: MA parameter = -0.9
    plot_acf(simulated_data_1, lags=20)
    plt.show()

    # Plot 2: MA parameter = 0.9
    plot_acf(simulated_data_2, lags=20)
    plt.show()


if __name__ == "__main__":
    sns.set()
    simulate_ma2_time_series()
    # simulated_data_1, simulated_data_2 = simulate_ma1_time_series()
    # compute_acf_for_several_ma_time_series(simulated_data_1, simulated_data_2)
