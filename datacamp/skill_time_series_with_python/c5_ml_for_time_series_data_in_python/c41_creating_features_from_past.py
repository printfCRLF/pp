import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import partial
from sklearn.linear_model import Ridge
from c33_creating_features_over_time import engineering_multiple_rolling_features_at_once
from util import percent_change, visualize_coefficients


def creating_features_from_past(prices_perc):
    # These are the "time lags"
    shifts = np.arange(1, 11).astype(int)

    # Use a dictionary comprehension to create name: value pairs, one pair per shift
    shifted_data = {"lag_{}_day".format(day_shift): prices_perc.shift(
        day_shift) for day_shift in shifts}

    # Convert into a DataFrame for subsequent use
    prices_perc_shifted = pd.DataFrame(shifted_data)

    # Plot the first 100 samples of each
    ax = prices_perc_shifted.iloc[:100].plot(cmap=plt.cm.viridis)
    prices_perc.iloc[:100].plot(color='r', lw=2)
    ax.legend(loc='best')
    plt.show()

    return prices_perc_shifted


def auto_regressive_models(prices_perc_shifted, prices_perc):
    # Replace missing values with the median for each column
    X = prices_perc_shifted.fillna(np.nanmedian(prices_perc_shifted))
    y = prices_perc.fillna(np.nanmedian(prices_perc))

    # Fit the model
    model = Ridge()
    model.fit(X, y)

    # Visualize the output data up to "2011-01"
    fig, axs = plt.subplots(2, 1, figsize=(10, 5))
    y.loc[:'2011-01'].plot(ax=axs[0])

    # Run the function to visualize model's coefficients
    visualize_coefficients(model.coef_, prices_perc_shifted.columns, ax=axs[1])
    plt.show()

    return X, y, model


if __name__ == "__main__":
    sns.set()
    prices_perc = engineering_multiple_rolling_features_at_once()
    prices_perc_shifted = creating_features_from_past(prices_perc)
    auto_regressive_models(prices_perc_shifted, prices_perc)
