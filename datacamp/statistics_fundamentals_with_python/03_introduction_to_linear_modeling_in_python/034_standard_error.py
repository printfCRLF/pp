import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols


x_data = np.array([0.,  0.08333333,  0.16666667,  0.25,  0.33333333,
                   0.41666667,  0.5,  0.58333333,  0.66666667,  0.75,
                   0.83333333,  0.91666667,  1.,  1.08333333,  1.16666667,
                   1.25,  1.33333333,  1.41666667,  1.5,  1.58333333,
                   1.66666667,  1.75,  1.83333333,  1.91666667,  2.])

y_data = np.array([4.87303609,    2.33139743,    6.74881808,    9.28109413,
                   19.26288955,   13.92871724,   30.23443529,   26.88304596,
                   34.29045062,   36.75188887,   46.05299048,   39.6529112,
                   49.03274839,   53.0145036,   61.73464166,   59.2003262,
                   66.14938204,   68.19975808,   75.12664124,   80.91511231,
                   80.0314758,   90.93417113,   94.37143883,   97.34081635,
                   102.70256785])


def variation_around_the_trend():
    # Store x_data and y_data, as times and distances, in df, and use ols() to fit a model to it.
    df = pd.DataFrame(dict(times=x_data, distances=y_data))
    model_fit = ols(formula="distances ~ times", data=df).fit()

    # Extact the model parameters and their uncertainties
    a0 = model_fit.params['Intercept']
    e0 = model_fit.bse['Intercept']
    a1 = model_fit.params['times']
    e1 = model_fit.bse['times']

    # Print the results with more meaningful names
    print('Estimate    of the intercept = {:0.2f}'.format(a0))
    print('Uncertainty of the intercept = {:0.2f}'.format(e0))
    print('Estimate    of the slope = {:0.2f}'.format(a1))
    print('Uncertainty of the slope = {:0.2f}'.format(e1))


distances1 = np.array([16.24345364,   -1.95089747,    3.05161581,    1.77031378,
                       25.32074296,   -2.18205364,   42.44811764,   21.55459766,
                       36.52372429,   35.00629625,   56.28774604,   25.23192624,
                       46.77582796,   50.32612312,   69.67102776,   51.50108733,
                       64.94238459,   62.05474915,   75.42213747,   84.9948188,
                       72.32714156,   98.9472371,  100.68257387,  100.85827672,
                       109.00855949])

distances2 = np.array([16.24345364,  -5.2842308,  -3.61505086,  -8.22968622,
                       11.98740963, -18.8487203,  22.44811764,  -1.77873568,
                       9.85705763,   5.00629625,  22.9544127, -11.43474043,
                       6.77582796,   6.99278979,  23.00436109,   1.50108733,
                       11.60905126,   5.38808249,  15.42213747,  21.66148547,
                       5.66047489,  28.9472371,  27.34924054,  24.19161006,  29.00855949])

times = np.array([0.,  0.08333333,  0.16666667,  0.25,  0.33333333,
                  0.41666667,  0.5,  0.58333333,  0.66666667,  0.75,
                  0.83333333,  0.91666667,  1.,  1.08333333,  1.16666667,
                  1.25,  1.33333333,  1.41666667,  1.5,  1.58333333,
                  1.66666667,  1.75,  1.83333333,  1.91666667,  2.])

df = pd.DataFrame(
    {"distances1": distances1, "distances2": distances2, "times": times})


def variation_in_two_parts():
    # Build and fit two models, for columns distances1 and distances2 in df
    model_1 = ols(formula="distances1 ~ times", data=df).fit()
    model_2 = ols(formula="distances2 ~ times", data=df).fit()

    # Extract R-squared for each model, and the standard error for each slope
    se_1 = model_1.bse['times']
    se_2 = model_2.bse['times']
    rsquared_1 = model_1.rsquared
    rsquared_2 = model_2.rsquared

    # Print the results
    print(
        'Model 1: SE = {:0.3f}, R-squared = {:0.3f}'.format(se_1, rsquared_1))
    print(
        'Model 2: SE = {:0.3f}, R-squared = {:0.3f}'.format(se_2, rsquared_2))


variation_around_the_trend()
variation_in_two_parts()
