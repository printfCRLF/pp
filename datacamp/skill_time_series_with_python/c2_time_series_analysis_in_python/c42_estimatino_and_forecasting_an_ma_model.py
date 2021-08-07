from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def estimating_an_ma_model():
    ar1 = np.array([1])
    ma1 = np.array([1, -0.9])
    MA_object1 = ArmaProcess(ar1, ma1)
    simulated_data_1 = MA_object1.generate_sample(nsample=1000)

    # Fit an MA(1) model to the first simulated data
    mod = ARMA(simulated_data_1, order=(0, 1))
    res = mod.fit()

    # Print out summary information on the fit
    print(res.summary())

    # Print out the estimate for the constant and for theta
    print("When the true theta=-0.9, the estimate of theta (and the constant) are:")
    print(res.params)

    return res


def forecasting_with_ma_model(res):
    res.plot_predict(start=990, end=1010)
    plt.show()


if __name__ == "__main__":
    sns.set()
    res = estimating_an_ma_model()
    forecasting_with_ma_model(res)
