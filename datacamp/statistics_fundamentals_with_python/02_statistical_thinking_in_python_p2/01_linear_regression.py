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
    a, b = np.polyfit(illiteracy, fertility, 1)
    a_vals = np.linspace(0, 0.1, 200)
    rss = np.empty_like(a_vals)
    for i, a in enumerate(a_vals):
        rss[i] = np.sum((fertility - a*illiteracy - b)**2)

    plt.plot(a_vals, rss, '-')
    plt.xlabel('slope (children per woman / percent illiterate)')
    plt.ylabel('sum of square of residuals')
    plt.show()


def linear_regression_on_appropriate_anscombe_data(): 
    x = [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.]
    y = [8.04, 6.95,  7.58,  8.81,  8.33,  9.96,  7.24,  4.26, 10.84, 4.82,  5.68]

    a, b = np.polyfit(x, y, 1)
    print(a, b)

    x_theor = np.array([3, 15])
    y_theor = x_theor * a + b

    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.plot(x_theor, y_theor, marker='.', linestyle='none')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def linear_regression_on_all_anscombe_data(): 
    anscombe_x = [[10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.],
        [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.],
        [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.],
        [ 8.,  8.,  8.,  8.,  8.,  8.,  8., 19.,  8.,  8.,  8.]]

    anscombe_y = [[ 8.04,  6.95,  7.58,  8.81,  8.33,  9.96,  7.24,  4.26, 10.84, 4.82,  5.68],
    [9.14, 8.14, 8.74, 8.77, 9.26, 8.1 , 6.13, 3.1 , 9.13, 7.26, 4.74],
    [ 7.46,  6.77, 12.74,  7.11,  7.81,  8.84,  6.08,  5.39,  8.15, 6.42,  5.73],
    [ 6.58,  5.76,  7.71,  8.84,  8.47,  7.04,  5.25, 12.5 ,  5.56, 7.91,  6.89]]

    for x, y in zip(anscombe_x , anscombe_y ):
        a, b = np.polyfit(x, y, 1)
        print('slope:', a, 'intercept:', b)

#eda_of_literacy_fertility_data()
#linear_regression()
how_is_it_optimal()
#linear_regression_on_appropriate_anscombe_data()
#linear_regression_on_all_anscombe_data()



