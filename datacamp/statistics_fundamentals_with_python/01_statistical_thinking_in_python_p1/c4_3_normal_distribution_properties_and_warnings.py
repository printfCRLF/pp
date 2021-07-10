import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf
from data import load_belmont_data


def are_belmont_stakes_normally_distributed(belmont_no_outliers):
    mu = np.mean(belmont_no_outliers)
    sigma = np.std(belmont_no_outliers)
    samples = np.random.normal(mu, sigma, size=10000)

    x_theor, y_theor = ecdf(samples)
    x, y = ecdf(belmont_no_outliers)

    _ = plt.plot(x_theor, y_theor)
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('Belmont winning time (sec.)')
    _ = plt.ylabel('CDF')
    plt.show()


def chances_are_faster_than_secretariat(belmont_no_outliers):
    mu = np.mean(belmont_no_outliers)
    sigma = np.std(belmont_no_outliers)
    samples = np.random.normal(mu, sigma, 1000000)
    prob = len(samples[samples < 144]) / len(samples)
    print('Probability of besting Secretariat:', prob)


sns.set()
belmont_no_outliers = load_belmont_data()
are_belmont_stakes_normally_distributed(belmont_no_outliers)
chances_are_faster_than_secretariat(belmont_no_outliers)
