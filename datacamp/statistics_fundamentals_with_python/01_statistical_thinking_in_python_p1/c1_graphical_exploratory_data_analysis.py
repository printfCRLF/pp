import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import seaborn as sns
from seaborn.relational import lineplot
from sklearn import datasets
from sklearn.decomposition import PCA
from data import load_iris_datasets


def plotting_histogram_of_iris_data(versicolor_petal_length):
    n_data = len(versicolor_petal_length)
    n_bins = np.sqrt(n_data)
    # The default "sqaure root rule" is a commonly-used rule of thumb
    # for choosing number of bins
    n_bins = int(n_bins)

    # Plot the histogram
    sns.set()
    plt.hist(versicolor_petal_length, bins=n_bins)
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('count')
    plt.show()


def bee_swarm_plot(df):
    sns.swarmplot(x='species', y='petal length (cm)', data=df)

    _ = plt.xlabel('species')
    _ = plt.ylabel('petal length (cm)')
    plt.show()


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, len(x)+1) / n
    return x, y


def plotting_ecdf(versicolor_petal_length):
    x_vers, y_vers = ecdf(versicolor_petal_length)
    middle_idx = int(len(versicolor_petal_length) / 2) - 1

    _ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
    _ = plt.xlabel('petal length(cm)')
    _ = plt.ylabel('ECDF')
    plt.margins(0.02)

    middle_x = x_vers[middle_idx]
    middle_y = y_vers[middle_idx]
    text = "({0}, {1})".format(middle_x, middle_y)
    _ = plt.axvline(middle_x, ymax=middle_y, linestyle="--")
    xmax = (middle_x - x_vers[0]) / (x_vers[-1] - x_vers[0])
    _ = plt.axhline(middle_y, xmax=xmax, linestyle="--")
    plt.annotate(text, (middle_x, middle_y))

    plt.show()


def comparison_of_ecdfs(setosa_petal_length, versicolor_petal_length, virginica_petal_length):
    x_set, y_set = ecdf(setosa_petal_length)
    x_vers, y_vers = ecdf(versicolor_petal_length)
    x_virg, y_virg = ecdf(virginica_petal_length)

    # Plot all ECDFs on the same plot
    _ = plt.plot(x_set, y_set, marker='.', linestyle='none')
    _ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
    _ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

    # Annotate the plot
    plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('ECDF')

    # Display the plot
    plt.show()


sns.set()
df, setosa_petal_length, versicolor_petal_length, virginica_petal_length = load_iris_datasets()

# plotting_histogram_of_iris_data(versicolor_petal_length)
# bee_swarm_plot(df)
plotting_ecdf(versicolor_petal_length)
# comparison_of_ecdfs(setosa_petal_length, versicolor_petal_length, virginica_petal_length)
