import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf


def sampling_out_of_binomial_distribution():
    n_defaults = np.random.binomial(100, 0.05, size=10000)
    x, y = ecdf(n_defaults)

    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('number of defaults out of 100 loans')
    _ = plt.ylabel('CDF')
    plt.show()


def plotting_the_binomial_pmf():
    n_defaults = np.random.binomial(100, 0.05, size=10000)
    bins = np.arange(0, max(n_defaults) + 1.5) - 0.5
    _ = plt.hist(n_defaults, density=True, bins=bins)

    _ = plt.xlabel('number of defaults out of 100 loans')
    _ = plt.ylabel('probability')
    plt.show()


sns.set()
# sampling_out_of_binomial_distribution()
plotting_the_binomial_pmf()
