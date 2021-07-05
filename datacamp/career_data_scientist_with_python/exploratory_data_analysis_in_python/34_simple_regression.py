import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress
from empiricaldist import Pmf, Cdf
from data import load_brfss_data


def income_and_vegetables(brfss):
    # Extract the variables
    subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
    xs = subset["INCOME2"]
    ys = subset["_VEGESU1"]

    # Compute the linear regression
    res = linregress(xs, ys)
    print(res)

    return xs, ys, res


def fit_a_line(xs, ys, res):
    # Plot the scatter plot
    plt.clf()
    x_jitter = xs + np.random.normal(0, 0.15, len(xs))
    plt.plot(x_jitter, ys, 'o', alpha=0.2)

    # Plot the line of best fit
    fx = np.array([xs.min(), xs.max()])
    fy = res.intercept + res.slope * fx
    plt.plot(fx, fy, '-', alpha=0.7)

    plt.xlabel('Income code')
    plt.ylabel('Vegetable servings per day')
    plt.ylim([0, 6])
    plt.show()


brfss = load_brfss_data()
xs, ys, res = income_and_vegetables(brfss)
fit_a_line(xs, ys, res)
