import pandas as pd
import numpy as np


def has_docstring(func):
    """Check to see if the function `func` has a docstring

    Args: 
        func (callable): A function.

    Returns: 
        bool
    """
    return func.__doc__ is not None


def load_and_plot_data(filename):
    """Load a data frame and plot each column.

    Args:
      filename (str): Path to a CSV file of data.

    Returns:
      pandas.DataFrame
    """
    df = pd.load_csv(filename, index_col=0)
    df.hist()
    return df


def as_2D(arr):
    """Reshape an array to 2 dimensions"""
    return np.array(arr).reshape(1, -1)


def log_product(arr):
    return np.exp(np.sum(np.log(arr)))


def reviewing_your_coworkers_code():
    # Call has_docstring() on the load_and_plot_data() function
    ok = has_docstring(load_and_plot_data)
    if not ok:
        print("load_and_plot_data() doesn't have a docstring!")
    else:
        print("load_and_plot_data() looks ok")

    # Call has_docstring() on the as_2D() function
    ok = has_docstring(as_2D)
    if not ok:
        print("as_2D() doesn't have a docstring!")
    else:
        print("as_2D() looks ok")

    # Call has_docstring() on the log_product() function
    ok = has_docstring(log_product)
    if not ok:
        print("log_product() doesn't have a docstring!")
    else:
        print("log_product() looks ok")


reviewing_your_coworkers_code()
