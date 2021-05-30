import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dc_stat_think as dcst
from scipy import stats
import seaborn as sns


def load_data():
    file = 'data/parkfield_earthquakes_1950-2017.csv'
    df = pd.read_csv(file, sep=',', comment='#')
    mags = df['mag']
    time_gap = np.array([24.06570842, 20.07665982, 21.01848049, 12.24640657, 32.05475702,
                         38.2532512])

    return mags, time_gap


def ks_stat(data1, data2):
    # Compute ECDF from data: x, y
    x, y = dcst.ecdf(data1)
    # Compute corresponding values of the target CDF
    cdf = dcst.ecdf_formal(x, data2)
    # Compute distances between concave corners and CDF
    D_top = y - cdf
    # Compute distance between convex corners and CDF
    D_bottom = cdf - y + 1/len(data1)
    return np.max((D_top, D_bottom))


def draw_ks_reps(n, f, args=(), size=10000, n_reps=10000):
    # Generate samples from target distribution
    x_f = f(*args, size=size)

    # Initialize K-S replicates
    reps = np.empty(n_reps)

    # Draw replicates
    for i in range(n_reps):
        # Draw samples for comparison
        x_samp = f(*args, size=n)

        # Compute K-S statistic
        reps[i] = dcst.ks_stat(x_samp, x_f)

    return reps


def the_ks_test_for_exponentiality(time_gap):
    mean_time_gap = np.mean(time_gap)

    # Draw target distribution: x_f
    x_f = np.random.exponential(mean_time_gap, 10000)

    # Compute K-S stat: d
    d = dcst.ks_stat(x_f, time_gap)

    # Draw K-S replicates: reps
    reps = dcst.draw_ks_reps(len(time_gap), np.random.exponential,
                             args=(mean_time_gap,), size=10000, n_reps=10000)

    # Compute and print p-value
    p_val = np.sum(reps >= d) / 10000
    print('p =', p_val)


_, time_gap = load_data()
the_ks_test_for_exponentiality(time_gap)
