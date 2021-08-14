import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from data import load_milk_production_data, load_water_data


def seasonal_decompose_step(milk_production):
    # Perform additive decomposition
    decomp = seasonal_decompose(milk_production, period=12)
    # Plot decomposition
    decomp.plot()
    plt.show()


def seasonal_acf_and_pacf(water):
    # Create figure and subplot
    fig, ax1 = plt.subplots()
    # Plot the ACF on ax1
    plot_acf(water, lags=25, zero=False,  ax=ax1)
    # Show figure
    plt.show()


def detrend_by_subtracting_rolling_mean(water):
    # Subtract the rolling mean
    water_2 = water - water.rolling(15).mean()
    # Drop the NaN values
    water_2 = water_2.dropna()
    # Create figure and subplots
    fig, ax1 = plt.subplots()
    # Plot the ACF
    plot_acf(water_2['water_consumers'], lags=25, zero=False, ax=ax1)
    # Show figure
    plt.show()


if __name__ == "__main__":
    sns.set()
    # milk_production = load_milk_production_data()
    # seasonal_decompose_step(milk_production)
    water = load_water_data()
    seasonal_acf_and_pacf(water)
    detrend_by_subtracting_rolling_mean(water)
