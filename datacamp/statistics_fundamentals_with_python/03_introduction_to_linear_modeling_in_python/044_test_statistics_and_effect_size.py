import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from data import sample_data


def plot_test_statistic(test_statistic, label=''):
    """
    Purpose: Plot the test statistic array as a histogram
    Args:
        test_statistic (np.array): an array of test statistic values, e.g. resample2 - resample1
    Returns:
        fig (plt.figure): matplotlib figure object
    """
    t_mean = np.mean(test_statistic)
    t_std = np.std(test_statistic)
    t_min = np.min(test_statistic)
    t_max = np.max(test_statistic)
    bin_edges = np.linspace(t_min, t_max, 21)
    data_opts = dict(rwidth=0.8, color='blue', alpha=0.5)
    fig, axis = plt.subplots(figsize=(12, 4))
    plt.hist(test_statistic, bins=bin_edges, **data_opts)
    axis.grid()
    axis.set_ylabel("Bin Counts")
    axis.set_xlabel("Distance Differences, late - early")
    title_form = "Test Statistic Distribution, \nMean = {:0.2f}, Std Error = {:0.2f}"
    axis.set_title(title_form.format(t_mean, t_std))
    plt.show()
    return fig


def shuffle_and_split(sample1, sample2):
    shuffled = np.concatenate((sample1, sample2))
    np.random.shuffle(shuffled)
    half_length = len(shuffled)//2
    sample1 = shuffled[0:half_length]
    sample2 = shuffled[half_length+1:]
    return sample1, sample2


def compute_test_statistic(sample1, sample2):
    resample1 = np.random.choice(sample1, size=500, replace=True)
    resample2 = np.random.choice(sample2, size=500, replace=True)
    test_statistic = resample2 - resample1
    return test_statistic


def plot_test_stats_and_pvalue(test_statistic, shuffle_statistic):
    """
    Purpose: Plot the test statistic array as a histogram
    Args:
        test_statistic (np.array): an array of test statistic values, e.g. resample2 - resample1
        shuffle_statistic (np.array): an array of test statistic values, from shuffled resamples
    Returns:
        fig (plt.figure): matplotlib figure object
    """
    t_mean = np.mean(test_statistic)
    t_std = np.std(test_statistic)
    t_min = np.min(test_statistic)
    t_max = np.max(test_statistic)
    effect_size = np.mean(test_statistic)
    p_value = len(
        shuffle_statistic[shuffle_statistic >= effect_size])/len(shuffle_statistic)
    # bin_edges = np.linspace(t_min, t_max, 21)
    bin_edges = np.linspace(-25, 25, 51)
    shuffle_opts = dict(rwidth=0.8, color='blue', alpha=0.35, label='Shuffled')
    test_opts = dict(rwidth=0.8, color='red', alpha=0.35, label='Unshuffled')
    fig, axis = plt.subplots(figsize=(12, 4))
    plt.hist(test_statistic, bins=bin_edges, **test_opts)
    plt.hist(shuffle_statistic, bins=bin_edges, **shuffle_opts)
    axis.axvline(effect_size, color='black', label='Effect Size')
    axis.axvspan(effect_size, +25, alpha=0.10, color='black', label='p-value')
    axis.grid()
    # axis.set_ylim(-5, +55)
    axis.set_xlim(-25, +25)
    axis.set_ylabel("Bin Counts")
    axis.set_xlabel("Test Statistic Values")
    title_form = ("Test Statistic Distibution, \n"
                  "Effect Size = {:0.2f}, p-value = {:0.02f}")
    axis.set_title(title_form.format(effect_size, p_value))
    axis.legend(loc='upper left')
    plt.show()
    return fig


df = pd.read_csv('data/hiking_data.csv')
sample_times = df['time'].to_numpy()
sample_distances = df['distance'].to_numpy()
print(stats.describe(sample_times))
print(stats.describe(sample_distances))

# group_duration_short = np.empty(500)
# group_duration_long = np.empty(500)


def test_statistics_and_effect_size():
    # Create two poulations, sample_distances for early and late sample_times.
    # Then resample with replacement, taking 500 random draws from each population.
    group_duration_short = sample_distances[sample_times < 5]
    group_duration_long = sample_distances[sample_times > 5]
    resample_short = np.random.choice(
        group_duration_short, size=500, replace=True)
    resample_long = np.random.choice(
        group_duration_long, size=500, replace=True)

    # Difference the resamples to compute a test statistic distribution, then compute its mean and stdev
    test_statistic = resample_long - resample_short
    effect_size = np.mean(test_statistic)
    standard_error = np.std(test_statistic)

    # Print and plot the results
    print('Test Statistic: mean={:0.2f}, stdev={:0.2f}'.format(
        effect_size, standard_error))
    fig = plot_test_statistic(test_statistic)
    return group_duration_short, group_duration_long


def null_hypothesis(group_duration_short, group_duration_long):
    # null hypothesis: "sort and long time durations have no effect on total distance traveled"

    # Shuffle the time-ordered distances, then slice the result into two populations.
    shuffle_bucket = np.concatenate(
        (group_duration_short, group_duration_long))
    np.random.shuffle(shuffle_bucket)
    slice_index = len(shuffle_bucket)//2
    shuffled_half1 = shuffle_bucket[0:slice_index]
    shuffled_half2 = shuffle_bucket[slice_index:]

    # Create new samples from each shuffled population, and compute the test statistic
    resample_half1 = np.random.choice(shuffled_half1, size=500, replace=True)
    resample_half2 = np.random.choice(shuffled_half2, size=500, replace=True)
    test_statistic = resample_half2 - resample_half1

    # Compute and print the effect size
    effect_size = np.mean(test_statistic)
    print('Test Statistic, after shuffling, mean = {}'.format(effect_size))


def visualizing_test_statistics(group_duration_short, group_duration_long):
    # From the unshuffled groups, compute the test statistic distribution
    resample_short = np.random.choice(
        group_duration_short, size=500, replace=True)
    resample_long = np.random.choice(
        group_duration_long, size=500, replace=True)
    test_statistic_unshuffled = resample_long - resample_short

    # Shuffle two populations, cut in half, and recompute the test statistic
    shuffled_half1, shuffled_half2 = shuffle_and_split(
        group_duration_short, group_duration_long)
    resample_half1 = np.random.choice(shuffled_half1, size=500, replace=True)
    resample_half2 = np.random.choice(shuffled_half2, size=500, replace=True)
    test_statistic_shuffled = resample_half2 - resample_half1

    # Plot both the unshuffled and shuffled results and compare
    fig = plot_test_statistic(test_statistic_unshuffled, label='Unshuffled')
    fig = plot_test_statistic(test_statistic_shuffled, label='Shuffled')


def visualizing_p_value(group_duration_short, group_duration_long):
    # Compute the test stat distribution and effect size for two population groups
    test_statistic_unshuffled = compute_test_statistic(
        group_duration_short, group_duration_long)
    effect_size = np.mean(test_statistic_unshuffled)

    # Randomize the two populations, and recompute the test stat distribution
    shuffled_half1, shuffled_half2 = shuffle_and_split(
        group_duration_short, group_duration_long)
    test_statistic_shuffled = compute_test_statistic(
        shuffled_half1, shuffled_half2)

    # Compute the p-value as the proportion of shuffled test stat values >= the effect size
    condition = test_statistic_shuffled >= effect_size
    p_value = len(
        test_statistic_shuffled[condition]) / len(test_statistic_shuffled)

    # Print p-value and overplot the shuffled and unshuffled test statistic distributions
    print("The p-value is = {}".format(p_value))
    fig = plot_test_stats_and_pvalue(
        test_statistic_unshuffled, test_statistic_shuffled)


group_duration_short, group_duration_long = test_statistics_and_effect_size()
null_hypothesis(group_duration_short, group_duration_long)
visualizing_test_statistics(group_duration_short, group_duration_long)
visualizing_p_value(group_duration_short, group_duration_long)
