import numpy as np


def multi_period_return(period_returns):
    return np.prod(period_returns + 1) - 1
