import numpy as np
import matplotlib.pyplot as plt
import util
import pandas as pd
import matplotlib.ticker as ticker
from statsmodels.formula.api import ols
from scipy import optimize

x = np.array([0.0,  0.5,  1.0,  1.5,  2.0,
              2.5,  3.0,  3.5,  4.0,  4.5,
              5.0,  5.5,  6.0,  6.5,  7.0,
              7.5,  8.0,  8.5,  9.0,  9.5,  10.0, ])

y = np.array([161.78587909,  132.72560763,  210.81767421,  179.6837026,  181.98528167,
              234.67907351,  246.48971034,  221.58691239,  250.3924093,  206.43287615,
              303.75089312,  312.29865056,  323.8331032,  261.9686295,  316.64806585,
              337.55295912,  360.13633529,  369.72729852,  408.0289548,  348.82736117,  394.93384188, ])


def model(x, a0=150, a1=25):
    ym = a0 + (a1 * x)
    return ym


def compute_rss_and_plot_fit(a0=3 * 50, a1=0.5 * 50):
    xd, yd = util.load_data()
    ym = model(xd, a0, a1)
    rss = util.compute_rss(yd, ym)
    fig = util.plot_data_with_model(xd, yd, ym)
    title_text = "a0={:0.2f}, a1={:0.2f}: RSS = {:0.2f}".format(a0, a1, rss)
    fig.axes[0].set_title(title_text)
    plt.show()
    return fig, rss


def least_squares_with_numpy():
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_dev = x - x_mean
    y_dev = y - y_mean

    a1 = np.sum(x_dev * y_dev) / np.sum(np.square(x_dev))
    a0 = y_mean - (a1 * x_mean)

    y_model = model(x, a0, a1)
    fig, rss = compute_rss_and_plot_fit(a0, a1)


def model_func(x, a0, a1):
    return a0 + (a1*x)


def optimization_with_scipy():
    x_data, y_data = util.load_data()

    # call curve_fit, passing in the model function and data; then unpack the results
    param_opt, param_cov = optimize.curve_fit(model_func, x_data, y_data)
    a0 = param_opt[0]  # a0 is the intercept in y = a0 + a1*x
    a1 = param_opt[1]  # a1 is the slope     in y = a0 + a1*x

    # test that these parameters result in a model that fits the data
    fig, rss = compute_rss_and_plot_fit(a0, a1)


def least_squares_with_statsmodels():
    # Pass data and `formula` into ols(), use and `.fit()` the model to the data
    df = pd.DataFrame({'x_column': x, 'y_column': y})
    x_data, y_data = util.load_data()

    model_fit = ols(formula="y_column ~ x_column", data=df).fit()

    # Use .predict(df) to get y_model values, then over-plot y_data with y_model
    y_model = model_fit.predict(df)
    fig = util.plot_data_with_model(x_data, y_data, y_model)

    # Extract the a0, a1 values from model_fit.params
    a0 = model_fit.params['Intercept']
    a1 = model_fit.params['x_column']

    # Visually verify that these parameters a0, a1 give the minimum RSS
    fig, rss = compute_rss_and_plot_fit(a0, a1)


# least_squares_with_numpy()
# optimization_with_scipy()
least_squares_with_statsmodels()
