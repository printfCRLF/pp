import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import partial
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import ShuffleSplit, KFold, TimeSeriesSplit, cross_val_score
from util import percent_change, visualize_coefficients, visualize_predictions, bootstrap_interval, bootstrap_interval2, my_pearsonr
from c33_creating_features_over_time import engineering_multiple_rolling_features_at_once
from c41_creating_features_from_past import creating_features_from_past, auto_regressive_models


def calculating_variability_in_model_coefficients(model, X, y):
    # feature_names = np.array(['AAPL_lag_1_day', 'YHOO_lag_1_day', 'NVDA_lag_1_day', 'AAPL_lag_2_day',
    #                           'YHOO_lag_2_day', 'NVDA_lag_2_day', 'AAPL_lag_3_day', 'YHOO_lag_3_day',
    #                           'NVDA_lag_3_day', 'AAPL_lag_4_day', 'YHOO_lag_4_day', 'NVDA_lag_4_day'])
    feature_names = np.array([
        'YHOO_lag_1_day', 'YHOO_lag_2_day', 'YHOO_lag_3_day', 'YHOO_lag_4_day', 'YHOO_lag_5_day',
        'YHOO_lag_6_day', 'YHOO_lag_7_day', 'YHOO_lag_8_day', 'YHOO_lag_9_day', 'YHOO_lag_10_day'])

    # Iterate through CV splits
    n_splits = 100
    cv = TimeSeriesSplit(n_splits=100)

    # Create empty array to collect coefficients
    coefficients = np.zeros([n_splits, X.shape[1]])

    for ii, (tr, tt) in enumerate(cv.split(X, y)):
        # Fit the model on training data and collect the coefficients
        model.fit(X[tr], y[tr])
        coefficients[ii] = model.coef_

    # Calculate a confidence interval around each coefficient
    bootstrapped_interval = bootstrap_interval(coefficients)

    # Plot it
    fig, ax = plt.subplots()
    ax.scatter(feature_names, bootstrapped_interval[0], marker='_', lw=3)
    ax.scatter(feature_names, bootstrapped_interval[1], marker='_', lw=3)
    ax.set(title='95% confidence interval for model coefficients')
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()

    return cv


def visualizing_model_score_variability_over_time(times_scores, model, X, y, cv):
    # Generate scores for each split to see how the model performs over time
    scores = cross_val_score(model, X, y, cv=cv, scoring=my_pearsonr)

    # Convert to a Pandas Series object
    scores_series = pd.Series(scores, index=times_scores, name='score')

    # Bootstrap a rolling confidence interval for the mean score
    scores_lo = scores_series.rolling(20).aggregate(
        partial(bootstrap_interval2, percentiles=2.5))
    scores_hi = scores_series.rolling(20).aggregate(
        partial(bootstrap_interval2, percentiles=97.5))

    # Plot the results
    fig, ax = plt.subplots()
    scores_lo.plot(ax=ax, label="Lower confidence interval")
    scores_hi.plot(ax=ax, label="Upper confidence interval")
    ax.legend()
    plt.show()


def accouting_for_non_stationarity(times_scores, model, X, y):
    # Pre-initialize window sizes
    window_sizes = [25, 50, 75, 100]

    # Create an empty DataFrame to collect the stores
    all_scores = pd.DataFrame(index=times_scores)

    # Generate scores for each split to see how the model performs over time
    for window in window_sizes:
        # Create cross-validation object using a limited lookback window
        cv = TimeSeriesSplit(n_splits=100, max_train_size=window)

        # Calculate scores across all CV splits and collect them in a DataFrame
        this_scores = cross_val_score(model, X, y, cv=cv, scoring=my_pearsonr)
        all_scores['Length {}'.format(window)] = this_scores

    # Visualize the scores
    ax = all_scores.rolling(10).mean().plot(cmap=plt.cm.coolwarm)
    ax.set(title='Scores for multiple windows', ylabel='Correlation (r)')
    plt.show()


if __name__ == "__main__":
    sns.set()
    prices_perc = engineering_multiple_rolling_features_at_once()
    prices_perc_shifted = creating_features_from_past(prices_perc)
    X, y, model = auto_regressive_models(prices_perc_shifted, prices_perc)
    X = X.values
    y = y.values

    times = np.array([
        '2010-04-05', '2010-04-28', '2010-05-21', '2010-06-16', '2010-07-12', '2010-08-04', '2010-08-27', '2010-09-22',
        '2010-10-15', '2010-11-09', '2010-12-03', '2010-12-29', '2011-01-24', '2011-02-16', '2011-03-14', '2011-04-06',
        '2011-05-02', '2011-05-25', '2011-06-20', '2011-07-14', '2011-08-08', '2011-08-31', '2011-09-26', '2011-10-19',
        '2011-11-11', '2011-12-07', '2012-01-03', '2012-01-27', '2012-02-22', '2012-03-16', '2012-04-11', '2012-05-04',
        '2012-05-30', '2012-06-22', '2012-07-18', '2012-08-10', '2012-09-05', '2012-09-28', '2012-10-23', '2012-11-19',
        '2012-12-13', '2013-01-09', '2013-02-04', '2013-02-28', '2013-03-25', '2013-04-18', '2013-05-13', '2013-06-06',
        '2013-07-01', '2013-07-25', '2013-08-19', '2013-09-12', '2013-10-07', '2013-10-30', '2013-11-22', '2013-12-18',
        '2014-01-14', '2014-02-07', '2014-03-05', '2014-03-28', '2014-04-23', '2014-05-16', '2014-06-11', '2014-07-07',
        '2014-07-30', '2014-08-22', '2014-09-17', '2014-10-10', '2014-11-04', '2014-11-28', '2014-12-23', '2015-01-20',
        '2015-02-12', '2015-03-10', '2015-04-02', '2015-04-28', '2015-05-21', '2015-06-16', '2015-07-10', '2015-08-04',
        '2015-08-27', '2015-09-22', '2015-10-15', '2015-11-09', '2015-12-03', '2015-12-29', '2016-01-25', '2016-02-18',
        '2016-03-14', '2016-04-07', '2016-05-02', '2016-05-25', '2016-06-20', '2016-07-14', '2016-08-08', '2016-08-31',
        '2016-09-26', '2016-10-19', '2016-11-11', '2016-12-07'])
    times_scores = pd.DatetimeIndex(times)

    cv = calculating_variability_in_model_coefficients(model, X, y)
    visualizing_model_score_variability_over_time(
        times_scores, model, X, y, cv)
    accouting_for_non_stationarity(times_scores, model, X, y)
