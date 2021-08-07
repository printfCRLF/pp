from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def seasonal_adjustment_during_tax_season():
    HRB = pd.read_csv("data/financial_data/HRB.csv",
                      parse_dates=["Quarter"], index_col="Quarter")
    # Seasonally adjust quarterly earnings
    HRBsa = HRB.diff(4)
    # Print the first 10 rows of the seasonally adjusted series
    print(HRBsa.head(10))
    # Drop the NaN data in the first four rows
    HRBsa = HRBsa.dropna()
    # Plot the autocorrelation function of the seasonally adjusted series
    plot_acf(HRBsa)
    plt.show()


if __name__ == "__main__":
    sns.set()
    seasonal_adjustment_during_tax_season()
