import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data import load_earth_quake_data


def searching_over_model_order(df):
    # Create empty list to store search results
    order_aic_bic = []

    # Loop over p values from 0-2
    for p in range(3):
        # Loop over q values from 0-2
        for q in range(3):
            # create and fit ARMA(p,q) model
            model = SARIMAX(df, order=(p, 0, q))
            results = model.fit()

            # Append order and results tuple
            order_aic_bic.append((p, q, results.aic, results.bic))

    # Construct DataFrame from order_aic_bic
    order_df = pd.DataFrame(order_aic_bic,
                            columns=["p", "q", "AIC", "BIC"])

    # Print order_df in order of increasing AIC
    print(order_df.sort_values(by="AIC"))

    # Print order_df in order of increasing BIC
    print(order_df.sort_values(by="BIC"))


def aic_and_bic(earthquake):
    # Loop over p values from 0-2
    for p in range(3):
        # Loop over q values from 0-2
        for q in range(3):
            try:
                # create and fit ARMA(p,q) model
                model = SARIMAX(earthquake, order=(p, 0, q))
                results = model.fit()

                # Print order and results
                print(p, q, results.aic, results.bic)
            except:
                print(p, q, None, None)


if __name__ == "__main__":
    sns.set()

    warnings.filterwarnings('ignore', '.*CONVERGENCE.*')

    # searching_over_model_order(df)
    earthquake = load_earth_quake_data()
    aic_and_bic(earthquake)
