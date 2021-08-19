
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import partial
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import ShuffleSplit, KFold, TimeSeriesSplit
from util import percent_change, visualize_coefficients, visualize_predictions, visualize_predictions2
from c33_creating_features_over_time import engineering_multiple_rolling_features_at_once
from c41_creating_features_from_past import creating_features_from_past, auto_regressive_models


def cross_validation_with_shuffling(X, y, model):
    # Import ShuffleSplit and create the cross-validation object
    cv = ShuffleSplit(n_splits=10, random_state=1)

    # Iterate through CV splits
    results = []
    for tr, tt in cv.split(X, y):
        # Fit the model on training data
        model.fit(X[tr], y[tr])

        # Generate predictions on the test data, score the predictions, and collect
        prediction = model.predict(X[tt])
        score = r2_score(y[tt], prediction)
        results.append((prediction, score, tt))

    # Custom function to quickly visualize predictions
    visualize_predictions(results)


def cv_without_shuffling(X, y, model):
    cv = KFold(n_splits=10, shuffle=False)
    # Iterate through CV splits
    results = []
    for tr, tt in cv.split(X, y):
        # Fit the model on training data
        model.fit(X[tr], y[tr])

        # Generate predictions on the test data and collect
        prediction = model.predict(X[tt])
        results.append((prediction, tt))

    # Custom function to quickly visualize predictions
    visualize_predictions2(results)


def time_based_cross_validation(X, y, model):
    # Create time-series cross-validation object
    cv = TimeSeriesSplit(n_splits=10)

    # Iterate through CV splits
    fig, ax = plt.subplots()
    for ii, (tr, tt) in enumerate(cv.split(X, y)):
        # Plot the training data on each iteration, to see the behavior of the CV
        ax.plot(tr, ii + y[tr])

    ax.set(title='Training data on each CV iteration', ylabel='CV iteration')
    plt.show()


if __name__ == "__main__":
    sns.set()
    prices_perc = engineering_multiple_rolling_features_at_once()
    prices_perc_shifted = creating_features_from_past(prices_perc)
    X, y, model = auto_regressive_models(prices_perc_shifted, prices_perc)
    X = X.values
    y = y.values
    # cross_validation_with_shuffling(X, y, model)
    # cv_without_shuffling(X, y, model)
    time_based_cross_validation(X, y, model)