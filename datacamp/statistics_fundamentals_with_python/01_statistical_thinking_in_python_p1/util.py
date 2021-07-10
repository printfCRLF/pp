import numpy as np


def ecdf(data):
    n = len(data)
    x = np.sort(data)
    # numpy.arange(start, stop, step)
    # Return evenly spaced values within a given interval.
    # Values are generated within the half-open interval [start, stop)

    # python's builtin range(start, stop) also returns [start, stop), but supports only integers

    # numpy.linspace(start, stop, num=50, endpoint=True, retstep) gives the option to include / exclude the endpoint.
    y = np.arange(1, len(x) + 1) / n
    return x, y
