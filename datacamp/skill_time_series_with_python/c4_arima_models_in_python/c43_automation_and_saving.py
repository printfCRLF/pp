import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data import load_australia_employment_data
import pmdarima as pm
import joblib


def automated_model_selection(df1, df2, df3):
    # Create auto_arima model
    model1 = pm.auto_arima(df1, seasonal=True, m=7, d=0, D=1,
                           max_p=2, max_q=2,
                           trace=True, error_action='ignore', suppress_warnings=True)
    print(model1.summary())

    # Create model
    model2 = pm.auto_arima(df2, d=1, seasonal=False, trend="c",
                           max_p=2, max_q=2,
                           trace=True, error_action='ignore', suppress_warnings=True)
    print(model2.summary())

    # Create model for SARIMAX(p,1,q)(P,1,Q)7
    model3 = pm.auto_arima(df3, seasonal=True, m=7, d=1, D=1,
                           start_p=1, start_q=1,
                           max_p=1, max_q=1,
                           max_P=1, max_Q=1,
                           trace=True, error_action='ignore', suppress_warnings=True)
    print(model3.summary())


def saving_and_updating_models(model, df_new):
    # Set model name
    filename = "candy_model.pkl"
    # Pickle it
    joblib.dump(model, filename)
    # Load the model back in
    loaded_model = joblib.load(filename)
    # Update the model
    loaded_model.update(df_new)


if __name__ == "__main__":
    sns.set()
    # automated_model_selection(df1, df2, df3)
    # saving_and_updating_models(model, df_new)
