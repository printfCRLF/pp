import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import util

times = np.array([0.,   1.,   2.,   3.,   4., 5.,
                  6.,   7.,   8.,   9.,  10.])
distances = np.array([0., 44.04512153, 107.16353484,
                      148.43674052, 196.39705633,  254.4358147,  300.])
measured_distances = np.array([
    0.24835708,  0.93086785,  2.32384427,  3.76151493,  3.88292331, 4.88293152,
    6.78960641,  7.38371736,  7.76526281,  9.27128002, 9.76829115])


def plotting_model_on_data():
    # Pass times and measured distances into model
    model_distances = util.model2(times, measured_distances)

    # Create figure and axis objects and call axis.plot() twice to plot data and model distances versus times
    fig, axis = plt.subplots()
    axis.plot(times, measured_distances, linestyle=" ",
              marker="o", color="black", label="Measured")
    axis.plot(times, model_distances, linestyle="-",
              marker=None, color="red", label="Modeled")

    # Add grid lines and a legend to your plot, and then show to display
    axis.grid(True)
    axis.legend(loc="best")
    plt.show()


def plot_data_and_model(xd, yd, xm, ym):
    """
    Purpose:
        Plot both the measured data and the model o the same figure.
        Measured data will be black point markers with no line
        Modeled data will be a solid red line with no point markers
    Args:
        xd (np.ndarray): numpy array of indendent variable, measured data
        yd (np.ndarray): numpy array of dendent variable, measured data
        xm (np.ndarray): numpy array of indendent variable, model data
        ym (np.ndarray): numpy array of dendent variable, model data
    Returns:
        fig (plt.figure): matplotlib figure object
    """
    fig, axis = plt.subplots()
    axis.plot(xd, yd, color="black", linestyle=" ",
              marker="o", label="Measured")
    axis.plot(xm, ym, color="red", linestyle="-", marker=None, label="Modeled")
    axis.axvline(0, color='black')
    axis.axhline(0, color='black')
    axis.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.yaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.yaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.set_xlim([-11, 11])
    axis.set_ylim([-11, 11])
    axis.grid(True, which="both")
    axis.legend(loc=2)
    return fig


def visually_estimating_slope_and_intercept():
    xd = np.array([2.,  2.5,  3.,  3.5,  4.,  4.5,  5.,  5.5,  6.,  6.5,  7.])
    yd = np.array([4.24835708,  4.43086785,  5.32384427,  6.26151493,  5.88292331,
                   6.38293152,  7.78960641,  7.88371736,  7.76526281,  8.77128002,
                   8.76829115])

    # Look at the plot data and guess initial trial values
    trial_slope = 1.0
    trial_intercept = 2.1

    # input thoses guesses into the model function to compute the model values.
    xm, ym = util.model3(trial_intercept, trial_slope)

    # Compare your your model to the data with the plot function
    fig = plot_data_and_model(xd, yd, xm, ym)
    plt.show()

    # Repeat the steps above until your slope and intercept guess makes the model line up with the data.
    final_slope = 1.0
    final_intercept = 2.1


plotting_model_on_data()
#visually_estimating_slope_and_intercept()
