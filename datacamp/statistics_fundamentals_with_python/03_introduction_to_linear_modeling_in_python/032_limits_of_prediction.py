
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from statsmodels.formula.api import ols


def interpolation_inbetween_times():
    # build and fit a model to the df_monthly data
    model_fit = ols('Close ~ DayCount', data=df_monthly).fit()

    # Use the model FIT to the MONTHLY data to make a predictions for both monthly and daily data
    df_monthly['Model'] = model_fit.predict(df_monthly.DayCount)
    df_daily['Model'] = model_fit.predict(df_daily.DayCount)

    # Plot the monthly and daily data and model, compare the RSS values seen on the figures
    fig_monthly = plot_model_with_data(df_monthly)
    fig_daily = plot_model_with_data(df_daily)


def plot_model_with_data(df, data_label='Data'):
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 6))
    RSS = np.sum(np.square(df.Model - df.Close))
    df.Close.plot(ax=axis, color="black", marker="o",
                  linestyle=" ", label=data_label)
    df.Model.plot(ax=axis, color="red", marker=" ",
                  linestyle="-", label="Model")
    axis.set_ylabel("DJIA")
    axis.set_title('RSS = {:0.1f}'.format(RSS))
    axis.grid(True, which="both")
    axis.legend()
    plt.show()
    return fig


def going_over_the_edge():
    # Compute the residuals, "data - model", and determine where [residuals < tolerance]
    residuals = np.abs(y_data - y_model)
    tolerance = 100
    x_good = x_data[residuals < tolerance]

    # Find the min and max of the "good" values, and plot y_data, y_model, and the tolerance range
    print('Minimum good x value = {}'.format(np.min(x_good)))
    print('Maximum good x value = {}'.format(np.max(x_good)))
    fig = plot_data_model_tolerance(x_data, y_data, y_model, tolerance)


def plot_data_model_tolerance(x_data, y_data, y_model, tolerance=100):
    """
    Purpose: 
        Plot data (x_data, y_data) and overplot model (x_data, y_model)
    Args:
        x_data (np.array): numpy array of values of independent variable
        y_data (np.array): numpy array of values of dependent variable
        y_model (np.array): numpy array of values of the modeled dependent variable
        tolerance (float): for plotting when np.abs(y_model - y_data) < tolerance
    Returns:
        fig (matplotlib.figure): matplotlib figure object
    """
    residuals = np.abs(y_model - y_data)
    x_good = x_data[residuals < tolerance]
    y_good = y_model[residuals < tolerance]
    x_min = np.min(x_good)
    x_max = np.max(x_good)
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 6))
    x = x_data
    y = y_data
    axis.plot(x[(x >= 0) & (x <= 10)], y[(x >= 0) & (x <= 10)],
              color="black", linestyle=" ", marker="o")
    axis.plot(x[x > 10], y[x > 10], color="blue", linestyle=" ", marker="o")
    axis.plot(x[x < 0], y[x < 0], color="blue", linestyle=" ", marker="o")
    axis.plot(x_data, y_model, color="red")
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    axis.set_ylim([-5*50, 15*50])
    axis.set_xlim([-15, 25])
    axis.xaxis.set_major_locator(MultipleLocator(5.0))
    axis.xaxis.set_minor_locator(MultipleLocator(1.0))
    axis.yaxis.set_major_locator(MultipleLocator(5.0*50))
    axis.yaxis.set_minor_locator(MultipleLocator(1.0*50))
    axis.set_ylabel('Altitude (meters)')
    axis.set_xlabel('Step Distance (Kilometers)')
    axis.set_title("Hiking  Trip")
    style_options = dict(color="green", alpha=0.35, linewidth=8)
    line = axis.plot(x_good, y_good, **style_options)
    plt.show()
    return fig


# interpolation_inbetween_times()
# going_over_the_edge()
