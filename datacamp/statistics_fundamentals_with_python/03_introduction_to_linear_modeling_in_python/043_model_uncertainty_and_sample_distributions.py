import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from data import sample_data

def bootstrap_and_standard_error():
    # Use the sample_data as a model for the population
    population_model = sample_data
    num_resamples = 100
    resample_size = 500
    bootstrap_means = np.empty(100)

    # Resample the population_model 100 times, computing the mean each sample
    for nr in range(num_resamples):
        bootstrap_sample = np.random.choice(
            population_model, size=resample_size, replace=True)
        bootstrap_means[nr] = np.mean(bootstrap_sample)

    # Compute and print the mean, stdev of the resample distribution of means
    distribution_mean = np.mean(bootstrap_means)
    standard_error = np.std(bootstrap_means)
    print('Bootstrap Distribution: center={:0.1f}, spread={:0.1f}'.format(
        distribution_mean, standard_error))

    # Plot the bootstrap resample distribution of means
    fig = plot_data_hist(bootstrap_means)


def plot_data_hist(y):
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(10, 6))
    data_opts = dict(rwidth=0.8, color='blue', alpha=0.5)
    bin_range = np.max(y) - np.min(y)
    bin_edges = np.linspace(np.min(y), np.max(y), 21)
    plt.hist(y, bins=bin_edges, **data_opts)
    axis.set_xlim(np.min(y) - 0.5*bin_range, np.max(y) + 0.5*bin_range)
    axis.grid("on")
    axis.set_ylabel("Resample Counts per Bin")
    axis.set_xlabel("Resample Means")
    axis.set_title("Resample Count = {}, \nMean = {:0.2f}, Std Error = {:0.2f}".format(
        len(y), np.mean(y), np.std(y)))
    fig.tight_layout()
    plt.show()
    return fig


def estimating_speed_and_confidence_visualize_bootstrap():
    df = pd.read_csv('data/hiking_data.csv')
    times = df['time'].to_numpy()
    distances = df['distance'].to_numpy()
    print(stats.describe(times))
    print(stats.describe(distances))


    # Resample each preloaded population, and compute speed distribution
    num_resamples = 1000
    resample_speeds = np.empty(num_resamples)    

    population_inds = np.arange(0, 99, dtype=int)
    for nr in range(num_resamples):
        sample_inds = np.random.choice(population_inds, size=100, replace=True)
        sample_inds.sort()
        sample_distances = distances[sample_inds]
        sample_times = times[sample_inds]
        a0, a1 = least_squares(sample_times, sample_distances)
        resample_speeds[nr] = a1

    # Compute effect size and confidence interval, and print
    speed_estimate = np.mean(resample_speeds)
    ci_90 = np.percentile(resample_speeds, [5, 95])
    print('Speed Estimate = {:0.2f}, 90% Confidence Interval: {:0.2f}, {:0.2f} '.format(speed_estimate, ci_90[0], ci_90[1]))
    print(stats.describe(resample_speeds))

    # Plot the histogram with the estimate and confidence interval
    fig, axis = plt.subplots()
    hist_bin_edges = np.linspace(0.0, 4.0, 21)
    axis.hist(resample_speeds, bins=hist_bin_edges, color='green', alpha=0.35, rwidth=0.8)
    axis.axvline(speed_estimate, label='Estimate', color='black')
    axis.axvline(ci_90[0], label=' 5th', color='blue')
    axis.axvline(ci_90[1], label='95th', color='blue')
    axis.legend()
    plt.show()


def least_squares(x, y):
    x_mean = np.sum(x)/len(x)
    y_mean = np.sum(y)/len(y)
    x_dev = x - x_mean
    y_dev = y - y_mean
    a1 = np.sum(x_dev * y_dev) / np.sum( np.square(x_dev) )
    a0 = y_mean - (a1 * x_mean)
    return a0, a1


# bootstrap_and_standard_error()
estimating_speed_and_confidence_visualize_bootstrap()

