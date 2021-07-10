import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf


def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    t1 = np.random.exponential(tau1, size)
    t2 = np.random.exponential(tau2, size)
    return t1 + t2


def distribution_of_no_hitters_and_cycles():
    waiting_times = successive_poisson(764, 715, 100000)

    _ = plt.hist(waiting_times, bins=100, density=True, histtype='step')
    _ = plt.xlabel('waiting time')
    _ = plt.ylabel('probability')
    plt.show()

    x, y = ecdf(waiting_times)
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('waiting time')
    _ = plt.ylabel('CDF')
    plt.show()


sns.set()
distribution_of_no_hitters_and_cycles()
