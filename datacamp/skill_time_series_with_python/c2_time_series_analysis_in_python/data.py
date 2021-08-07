import numpy as np
import pandas as pd


def get_interest_rate_data():
    rates = np.array([3.85,  4.14,  4.21,  4.65,  4.64,  5.7,  6.16,  7.88,  6.5,
                      5.89,  6.41,  6.9,  7.4,  7.76,  6.81,  7.78,  9.15, 10.33,
                      12.43, 13.98, 10.36, 11.82, 11.55,  9.,  7.23,  8.83,  9.14,
                      7.93,  8.08,  6.71,  6.7,  5.83,  7.84,  5.58,  6.43,  5.75,
                      4.65,  6.45,  5.12,  5.07,  3.83,  4.27,  4.24,  4.39,  4.71,
                      4.04,  2.25,  3.85,  3.3,  1.89,  1.78,  3.04,  2.17,  2.27,
                      2.45,  2.16])
    dates = pd.date_range(start="1962", end="2018", freq="A")
    interest_rate_data = pd.DataFrame(data={"US10Y": rates}, index=dates)
    return interest_rate_data
