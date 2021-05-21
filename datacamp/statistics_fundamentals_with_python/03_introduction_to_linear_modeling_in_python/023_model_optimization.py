import numpy as np
import matplotlib.pyplot as plt
import util
import pandas as pd
from statsmodels.formula.api import ols
import matplotlib.ticker as ticker


x_data, y_data = util.load_data()


def model(x, a0=150, a1=25):
    """
    Purpose: 
        For a given measured data x, compute the model prediction for y
        The form of the model is y = a0 + a1*x
    Args:
        x (float, np.ndarray): independent variable, e.g. time
        a0 (float): default=150, coefficient for the Zeroth order term in the model, i.e. a0
        a1 (float): default=25, coefficient for the 1st order term in the model, i.e. a1*x
    Returns:
        y (float, np.ndarray): model values predicted for corresponding input x.
    """
    y = a0 + (a1 * x)
    return y


def residual_sum_of_the_square():
    # Model the data with specified values for parameters a0, a1
    y_model = model(x_data, a0=150, a1=25)

    # Compute the RSS value for this parameterization of the model
    rss = np.sum(np.square(y_data - y_model))
    print("RSS = {}".format(rss))


def compute_rss_and_plot_fit(a0, a1):
    xd, yd = util.load_data()
    ym = model(xd, a0, a1)
    residuals = ym - yd
    rss = np.sum(np.square(residuals))
    summary = "Parameters a0={}, a1={} yield RSS={:0.2f}".format(a0, a1, rss)
    fig = util.plot_data_with_model(xd, yd, ym, summary)
    return rss, summary


def minimizing_the_residuals():
    rss, summary = compute_rss_and_plot_fit(a0=150, a1=25)
    print(summary)


def visualizing_the_rss_minima():
    a1_array = np.linspace(15, 35, 101)
    rss_list = []
    for a1_trial in a1_array:
        y_model = model(x_data, a0=150, a1=a1_trial)
        rss_value = util.compute_rss(y_data, y_model)
        rss_list.append(rss_value)

    rss_array = np.array(rss_list)
    best_rss = np.min(rss_array)
    best_a1 = a1_array[np.where(rss_array == best_rss)]
    print(f"The minimum RSS = {best_rss}, came from a1 = {best_a1}")

    fig = plot_rss_vs_a1(a1_array, rss_array)


def plot_rss_vs_a1(a1_array, rss_array):
    """
    Purpose:
        Plot RSS values (y-axis) versus a1 parameters values (x-axis)
         Also plot a point where the minimum RSS value occurs, and the 
         corresponding a1 value whose model resulted in that minimum RSS.
    Args:
        a1_array (np.array): an array of trial values for a1 (model slope)
        rss_array (np.array): an array of computed RSS values resulting from the a1_array
    Returns:
        fig (matplotlib.figure): figure object on which the data is plotted
    """
    font_options = {"family": "Arial", "size": 16}
    plt.rc("font", **font_options)
    fig, axis = plt.subplots(figsize=(12, 4))
    min_rss = np.min(rss_array)
    best_slope = a1_array[np.where(rss_array == min_rss)]
    axis.plot(a1_array, rss_array, marker="o", color="black")
    axis.plot(
        best_slope, min_rss, marker="o", markersize=12, linestyle=" ", color="red"
    )
    axis.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.grid(True, which="major")
    axis.set_ylabel("RSS")
    axis.set_xlabel("Slope $a_1$")
    axis.set_ylim([0, 100000])
    axis.set_title(
        "Minimum RSS = {:.02f} \n came from $a_1$={}".format(
            min_rss, best_slope[0])
    )
    plt.show()
    return fig


# residual_sum_of_the_square()
# minimizing_the_residuals()
visualizing_the_rss_minima()
