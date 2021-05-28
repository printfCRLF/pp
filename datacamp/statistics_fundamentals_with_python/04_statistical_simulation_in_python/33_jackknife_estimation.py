import numpy as np
from data import wrench_lengths


def basic_jackknife_estimation_mean():
    # Leave one observation out from wrench_lengths to get the jackknife sample and store the mean length
    mean_lengths, n = [], len(wrench_lengths)
    index = np.arange(n)

    for i in range(n):
        jk_sample = wrench_lengths[index != i]
        mean_lengths.append(np.mean(jk_sample))

    # The jackknife estimate is the mean of the mean lengths from each sample
    mean_lengths_jk = np.mean(np.array(mean_lengths))
    print("Jackknife estimate of the mean = {}".format(mean_lengths_jk))


def jackknife_confidence_interval_for_the_median():
    n, index = 100, np.arange(100)
    # Leave one observation out to get the jackknife sample and store the median length
    median_lengths = []
    for i in range(n):
        jk_sample = wrench_lengths[index != i]
        median_lengths.append(np.median(jk_sample))

    median_lengths = np.array(median_lengths)

    # Calculate jackknife estimate and it's variance
    jk_median_length = np.mean(median_lengths)
    jk_var = (n-1)*np.var(median_lengths)

    # Assuming normality, calculate lower and upper 95% confidence intervals
    jk_lower_ci = jk_median_length - 1.96 * np.sqrt(jk_var)
    jk_upper_ci = jk_median_length + 1.96 * np.sqrt(jk_var)
    print("Jackknife 95% CI lower = {}, upper = {}".format(
        jk_lower_ci, jk_upper_ci))


#basic_jackknife_estimation_mean()
jackknife_confidence_interval_for_the_median()
