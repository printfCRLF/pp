import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, pearson_r
from data import illiteracy, fertility


def eda_of_literacy_fertility_data():
    _ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
    plt.margins(0.02)
    _ = plt.xlabel('percent illiterate')
    _ = plt.ylabel('fertility')
    plt.show()

    print(pearson_r(illiteracy, fertility))


def linear_regression():
    _ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
    plt.margins(0.02)
    _ = plt.xlabel('percent illiterate')
    _ = plt.ylabel('fertility')

    a, b = np.polyfit(illiteracy, fertility, 1)
    print('slope =', a, 'children per woman / percent illiterate')
    print('intercept =', b, 'children per woman')

    x = np.array([0, 100])
    y = a * x + b
    _ = plt.plot(x, y)
    plt.show()


def how_is_it_optimal():
    # fix the intercept 
    # try out the slope a_vals in a range to find the minimal  RSS (sum of square of residuals)
    a, b = np.polyfit(illiteracy, fertility, 1)
    a_vals = np.linspace(0, 0.1, 200)
    rss = np.empty_like(a_vals)
    for i, a in enumerate(a_vals):
        rss[i] = np.sum((fertility - a*illiteracy - b)**2)

    plt.plot(a_vals, rss, '-')
    plt.xlabel('slope (children per woman / percent illiterate)')
    plt.ylabel('sum of square of residuals')
    plt.show()



sns.set()
# eda_of_literacy_fertility_data()
linear_regression()
# how_is_it_optimal()
