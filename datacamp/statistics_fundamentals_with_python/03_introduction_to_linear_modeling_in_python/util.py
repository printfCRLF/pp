import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def model1(time, a0=0, a1=50):
    """
    Purpose: 
        For a given value of time, compute the model value for distance
    Args:
        time (float, np.ndarray): elapse time in units of hours
        a0 (float): default=0, coefficient for the Zeroth order term in the model, i.e. a0 + a1*x
        a1 (float): default=50, coefficient for the 1st order term in the model, i.e. a0 + a1*x
    Returns:
        distance (float, np.ndarray): model values corresponding to input time array, with the same length/size.
    """
    distance = a0 + (a1 * time)
    return distance


def model2(x, y, a0=0, a1=1):
    """
    Purpose: 
        For a given data set, input as two arrays, x and y, 
        compute the model value for all modeled values 'ym'
    Args:
        x (float, np.ndarray):
        y (float, np.ndarray): 
        a0 (float): default=0, coefficient for the Zeroth order term in the model, i.e. a0 + a1*x
        a1 (float): default=50, coefficient for the 1st order term in the model, i.e. a0 + a1*x
    Returns:
        ym (float, np.ndarray): model values corresponding to input x array, with the same length/size.
    """
    # Note to datacamp editors: the interface is intentionally like this for pedagogical reasons
    # we don't want the student believing that our model is just hard-coded ;-)
    # the student will call this function as "ym = model(x,y)" which will make more
    # sense to them than "ym = model(x)"; they won't see the a0, a1, but we know
    # they are their and it makes things more flexible for the teachers :)
    ym = a0 + (a1 * x)
    return ym


def model3(a0=2, a1=1):
    """
    Purpose: 
        For a given data set, input as two arrays, x and y, 
        compute the model value for all modeled values 'ym'
    Args:
        trial_intercept (float): default=0, coefficient for the Zeroth order term in the model, i.e. a0 + a1*x
        trial_slope (float): default=50, coefficient for the 1st order term in the model, i.e. a0 + a1*x
    Returns:
        xm (float, np.ndarray): model values for independent variable
        ym (float, np.ndarray): model values of depedent variable, with the same length/size as xm.
    """
    xm = np.linspace(-5, 15, 41)
    ym = a0 + (a1 * xm)
    return xm, ym


def plot_prediction(x, y):
    """
    Purpose:
        Create a plot of y versus x
    Args:
        x (np.array): array of values for the indepent variable, e.g. times
        y (np.array): array of values for the depedent variable, e.g. distances
    Returns:
        fig (matplotlib.figure): matplotlib figure object
    """
    font_options = {"family": "Arial", "size": 16}
    plt.rc("font", **font_options)
    fig, axis = plt.subplots()
    axis.plot(x, y, color="red", linestyle="-", marker="o")
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    axis.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.yaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.yaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.set_ylabel("Y")
    axis.set_xlabel("X")
    axis.set_title("Plot of modeled Y for given X")
    plt.show()
    return fig


def plot_data(x, y):
    """
    Purpose:
        Create a plot of y versus x
    Args:
        x (np.array): array of values for the indepent variable, e.g. times
        y (np.array): array of values for the depedent variable, e.g. distances
    Returns:
        fig (matplotlib.figure): matplotlib figure object
    """
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8,6))
    axis.plot(x, y, color="black", linestyle=" ", marker="o")
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    axis.set_ylim([-5*50, 15*50])
    axis.set_xlim([-5, 15])
    axis.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.yaxis.set_major_locator(ticker.MultipleLocator(5.0*50))
    axis.yaxis.set_minor_locator(ticker.MultipleLocator(1.0*50))
    axis.set_ylabel('Altitude (meters)')
    axis.set_xlabel('Step Distance (km)')
    axis.set_title("Hiking  Trip")
    return fig

def plot_data_with_model(xd, yd, ym, title=""):
    fig = plot_data(xd, yd)
    fig.axes[0].plot(xd, ym, color="red")
    fig.axes[0].set_title(title)
    plt.show()
    return fig


def load_data():
    num_pts = 21
    a0 = 3.0 * 50
    a1 = 0.5 * 50
    mu = 0
    sigma = 1
    ae = 0.5 * 50
    seed = 1234
    np.random.seed(seed)
    xmin = 0
    xmax = 10
    x1 = np.linspace(xmin, xmax, num_pts)
    e1 = np.array([np.random.normal(mu, sigma) for n in range(num_pts)])
    y1 = a0 + (a1 * x1) + ae * e1
    return x1, y1


def compute_rss(yd, ym):
    rss = np.sum(np.square(yd - ym))
    return rss


