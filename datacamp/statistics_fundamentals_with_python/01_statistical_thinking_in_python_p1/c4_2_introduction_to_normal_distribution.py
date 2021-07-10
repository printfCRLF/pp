import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf


def the_normal_pdf(samples_std1, samples_std3, samples_std10):
    _ = plt.hist(samples_std1, density=True, histtype='step', bins=100)
    _ = plt.hist(samples_std3, density=True, histtype='step', bins=100)
    _ = plt.hist(samples_std10, density=True, histtype='step', bins=100)

    _ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
    plt.ylim(-0.01, 0.42)
    plt.show()


def the_normal_cdf(samples_std1, samples_std3, samples_std10):
    x_std1, y_std1 = ecdf(samples_std1)
    x_std3, y_std3 = ecdf(samples_std3)
    x_std10, y_std10 = ecdf(samples_std10)

    _ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
    _ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')
    _ = plt.plot(x_std10, y_std10, marker='.', linestyle='none')

    _ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
    plt.show()


sns.set()
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

the_normal_pdf(samples_std1, samples_std3, samples_std10)
the_normal_cdf(samples_std1, samples_std3, samples_std10)
