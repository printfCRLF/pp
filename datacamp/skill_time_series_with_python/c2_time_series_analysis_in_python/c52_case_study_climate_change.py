import datetime
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def is_temperature_a_random_walk():
    temp_NY = pd.read_csv("data/NOAA_TAVG.csv",
                          parse_dates=["DATE"], index_col="DATE", usecols=[0, 1])
    # Convert the index to a datetime object
    temp_NY.index = pd.to_datetime(temp_NY.index, format="%Y")

    # Plot average temperatures
    temp_NY.plot()
    plt.show()

    # Compute and print ADF p-value
    result = adfuller(temp_NY['TAVG'])
    print("The p-value for the ADF test is ", result[1])

    return temp_NY


def look_at_autocorrelations(temp_NY):
    # Take first difference of the temperature Series
    chg_temp = temp_NY.diff()
    chg_temp = chg_temp.dropna()

    # Plot the ACF and PACF on the same page
    fig, axes = plt.subplots(2, 1)

    # Plot the ACF
    plot_acf(chg_temp, lags=20, ax=axes[0])

    # Plot the PACF
    plot_pacf(chg_temp, lags=20, ax=axes[1])
    plt.show()

    return chg_temp


def which_arma_model_is_best(chg_temp):
    # Fit the data to an AR(1) model and print AIC:
    mod_ar1 = ARMA(chg_temp, order=(1, 0))
    res_ar1 = mod_ar1.fit()
    print("The AIC for an AR(1) is: ", res_ar1.aic)

    # Fit the data to an AR(2) model and print AIC:
    mod_ar2 = ARMA(chg_temp, order=(2, 0))
    res_ar2 = mod_ar2.fit()
    print("The AIC for an AR(2) is: ", res_ar2.aic)

    # Fit the data to an ARMA(1,1) model and print AIC:
    mod_arma11 = ARMA(chg_temp, order=(1, 1))
    res_arma11 = mod_arma11.fit()
    print("The AIC for an ARMA(1,1) is: ", res_arma11.aic)


def dont_throw_out_winter_coat_yet(temp_NY):
    # Forecast temperatures using an ARIMA(1,1,1) model
    mod = ARIMA(temp_NY, order=(1, 1, 1))
    res = mod.fit()

    # Plot the original series and the forecasted series
    res.plot_predict(start='1872-01-01', end='2046-01-01')
    plt.show()


if __name__ == "__main__":
    sns.set()
    temp_NY = is_temperature_a_random_walk()
    chg_temp = look_at_autocorrelations(temp_NY)
    which_arma_model_is_best(chg_temp)
    dont_throw_out_winter_coat_yet(temp_NY)
