import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, draw_bs_reps, draw_bs_pairs_linreg
from data import rainfall, nohitter_times, illiteracy, fertility


def standard_error_of_mean():
    # Take 10,000 bootstrap replicates of the mean: bs_replicates
    bs_replicates = draw_bs_reps(rainfall, np.mean, size=10000)

    # Compute and print SEM
    sem = np.std(rainfall) / np.sqrt(len(rainfall))
    print(sem)

    # Compute and print standard deviation of bootstrap replicates
    bs_std = np.std(bs_replicates)
    print(bs_std)

    # Make a histogram of the results
    _ = plt.hist(bs_replicates, bins=50, density=True)
    _ = plt.xlabel('mean annual rainfall (mm)')
    _ = plt.ylabel('PDF')

    # Show the plot
    plt.show()


def replicates_of_variance():
    # Generate 10,000 bootstrap replicates of the variance: bs_replicates
    bs_replicates = draw_bs_reps(rainfall, np.var, 10000)
    # Put the variance in units of square centimeters
    bs_replicates = bs_replicates / 100

    _ = plt.hist(bs_replicates, bins=50, density=True)
    _ = plt.xlabel('variance of annual rainfall (sq. cm)')
    _ = plt.ylabel('PDF')
    plt.show()

    var = np.var(rainfall)
    print('variance of the sample data', var)

    bs_replicates = draw_bs_reps(rainfall, np.var, 10000)
    var_bs = np.mean(bs_replicates)
    print('mean of variance of bootstrap replicates', var_bs)
    # The values aren't equal. bs_replicates is not normally distributed, as it has a longer tail to the right.


def confidence_interval_on_rate_of_no_hitters():
    # Draw bootstrap replicates of the mean no-hitter time (equal to tau): bs_replicates
    bs_replicates = draw_bs_reps(nohitter_times, np.mean, 10000)

    # Compute the 95% confidence interval: conf_int
    conf_int = np.percentile(bs_replicates, [2.5, 97.5])

    # Print the confidence interval
    print('95% confidence interval =', conf_int, 'games')

    # Plot the histogram of the replicates
    _ = plt.hist(bs_replicates, bins=50, density=True)
    _ = plt.xlabel(r'$\tau$ (games)')
    _ = plt.ylabel('PDF')

    # Show the plot
    plt.show()


sns.set()
# standard_error_of_mean()
# replicates_of_variance()
confidence_interval_on_rate_of_no_hitters()
