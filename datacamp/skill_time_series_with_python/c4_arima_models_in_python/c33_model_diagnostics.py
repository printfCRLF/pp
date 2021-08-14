import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data import load_earth_quake_data


def mean_absolute_error(earthquake):
    # Fit model
    model = SARIMAX(earthquake, order=(1, 0, 1))
    results = model.fit()

    # Calculate the mean absolute error from residuals
    mae = np.mean(np.abs(results.resid))

    # Print mean absolute error
    print(mae)

    # Make plot of time series for comparison
    earthquake.plot()
    plt.show()


def plot_diagnostics(df):
    # Create and fit model
    model = SARIMAX(df, order=(1, 1, 1))
    results = model.fit()

    # Create the 4 diagostics plots
    results.plot_diagnostics()
    plt.show()


if __name__ == "__main__":
    sns.set()
    earthquake = load_earth_quake_data()
    mean_absolute_error(earthquake)
    # plot_diagnostics(df)
