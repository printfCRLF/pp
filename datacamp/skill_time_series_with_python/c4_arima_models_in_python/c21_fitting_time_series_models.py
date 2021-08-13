import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima_model import ARMA


def fitting_arma_models(sample):
    # Instantiate the model
    model = ARMA(sample["timeseries_1"], order=(2, 0))
    # Fit the model
    results = model.fit()
    # Print summary
    print(results.summary())

    # Instantiate the model
    model = ARMA(sample["timeseries_2"], order=(0, 3))
    # Fit the model
    results = model.fit()
    # Print summary
    print(results.summary())


def fitting_an_arma_model():
    earthquake = pd.read_csv('data/earthquakes.xls', usecols=[0, 2],
                             parse_dates=['date'], index_col='date')

    # Instantiate the model
    model = ARMA(earthquake, order=(3, 1))
    # Fit the model
    results = model.fit()
    # Print model fit summary
    print(results.summary())


def fitting_an_armax_model(hospital):
    # Instantiate the model
    model = ARMA(hospital["wait_times_hrs"], order=(
        2, 1), exog=hospital["nurse_count"])
    # Fit the model
    results = model.fit()
    # Print model fit summary
    print(results.summary())


if __name__ == "__main__":
    sns.set()
    # fitting_arma_models(sample)
    fitting_an_arma_model()
    # fitting_an_armax_model(hospital)
