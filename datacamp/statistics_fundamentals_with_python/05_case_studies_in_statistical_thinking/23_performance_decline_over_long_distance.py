import pandas as pd
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    split_number = np.arange(3, 15)

    splits = np.array([[35.04, 36.39, 35.92, 36.23, 36.67, 36.76, 36.48, 36.85, 36.92,
                        36.68, 36.97, 36.98],
                       [34.14, 34.22, 33.67, 33.88, 34.15, 33.91, 34.41, 33.92, 34.36,
                        34.38, 34.6, 34.45],
                       [31.8, 31.91, 31.95, 32.04, 31.95, 31.65, 31.57, 31.39, 31.61,
                        31.43, 31.46, 31.47],
                       [33.16, 32.9, 32.68, 32.84, 33.55, 33.74, 33.71, 33.6, 33.71,
                        33.12, 33.14, 32.79],
                       [32.97, 32.83, 32.99, 32.94, 33.19, 33.6, 33.72, 33.74, 33.82,
                        33.67, 33.86, 33.59],
                       [34.6, 34.57, 34.62, 34.96, 35.1, 35.22, 35.63, 35.56, 35.43,
                        35.67, 35.26, 35.42],
                       [32.18, 32.17, 32.15, 32.16, 32.31, 32.27, 32.32, 32.23, 32.42,
                        32.34, 32.32, 32.27],
                       [32.4, 32.14, 32.46, 32.43, 32.58, 32.46, 32.6, 32.42, 32.79,
                        32.33, 32.47, 32.63],
                       [32.67, 32.54, 32.48, 32.42, 32.55, 32.45, 32.94, 33.03, 33.12,
                        33.47, 33.42, 33.48],
                       [33.76, 34.95, 34.76, 35.45, 34.99, 36.11, 35.27, 35.82, 35.48,
                        36.12, 35.2, 36.07],
                       [32.57, 32.7, 32.53, 32.73, 32.84, 32.7, 32.75, 33.07, 33.01,
                        33.11, 33.17, 33.02],
                       [35.04, 34.69, 34.24, 34.07, 34.47, 34.39, 34.98, 34.56, 35.3,
                        34.9, 35.03, 34.08],
                       [32.61, 32.97, 33.09, 33.19, 33.72, 33.92, 34.12, 33.82, 34.07,
                        34.22, 34.26, 34.07],
                       [31.01, 31.49, 31.38, 31.47, 31.58, 31.56, 31.68, 31.68, 32.09,
                        31.83, 32.25, 31.67],
                       [32.29, 32.36, 32.43, 32.56, 32.84, 32.73, 32.77, 32.78, 32.91,
                        33.15, 33.19, 33.32],
                       [31.92, 32.14, 31.87, 32.02, 31.84, 32.47, 32.17, 32.73, 32.45,
                        33.16, 33.01, 33.08],
                       [32.1, 32.47, 32.32, 32.84, 32.38, 32.93, 32.36, 32.96, 32.72,
                        33.35, 32.95, 33.77],
                       [35.97, 35.96, 36.09, 36., 36.59, 36.55, 36.4, 36.58, 36.89,
                        36.69, 36.81, 36.73],
                       [31.69, 31.56, 31.76, 31.43, 31.69, 31.77, 31.88, 31.66, 31.96,
                        31.87, 31.66, 31.73],
                       [31.71, 32.23, 31.89, 32.31, 32.01, 32.62, 32.12, 33., 32.63,
                        33.14, 32.55, 33.39],
                       [31.99, 31.94, 31.82, 32.02, 31.71, 32., 31.79, 31.87, 31.97,
                        32.15, 32.09, 32.3],
                       [31.88, 31.78, 31.67, 31.68, 31.97, 31.7, 31.71, 31.87, 31.91,
                        32., 31.83, 32.13],
                       [32.49, 32.32, 32.77, 32.8, 32.87, 32.85, 32.89, 33., 33.12,
                        32.86, 33.05, 32.75],
                       [31.99, 31.93, 31.76, 31.85, 31.95, 31.82, 31.64, 31.49, 31.78,
                        31.67, 32.28, 31.85],
                       [32.19, 32.32, 32.55, 32.74, 32.59, 32.94, 32.75, 33.09, 32.91,
                        33.53, 33.06, 33.],
                       [32.37, 32.62, 32.38, 33.07, 32.91, 33.45, 32.97, 33.38, 33.24,
                        33.33, 32.93, 32.53],
                       [32.8, 33.38, 33.18, 33.78, 33.78, 34.32, 34.1, 34.88, 33.97,
                        34.96, 34.44, 34.93],
                       [34.9, 35.03, 35.25, 35.42, 35.88, 35.63, 35.63, 35.66, 35.45,
                        35.66, 35.39, 35.34],
                       [32.67, 32.3, 32.4, 32.48, 32.52, 32.59, 32.73, 32.67, 32.97,
                        32.7, 32.87, 32.82],
                       [32.68, 33.02, 32.8, 32.94, 33.28, 33.46, 33.2, 33.42, 33.14,
                        33.36, 33.38, 33.31],
                       [33.96, 33.93, 33.62, 33.76, 33.31, 33.7, 33.02, 33.66, 33.57,
                        33.37, 33.91, 33.92],
                       [32.36, 32.6, 32.12, 32.67, 32.56, 32.91, 32.84, 33.17, 32.95,
                        33.44, 33.25, 33.59],
                       [31.69, 31.81, 31.99, 31.99, 32.01, 31.77, 31.67, 31.62, 31.66,
                        31.82, 31.63, 31.72],
                       [36.95, 37.44, 36.96, 37.12, 37.51, 37.07, 37.49, 36.66, 36.84,
                        37.11, 37.55, 37.6],
                       [32.61, 32.92, 32.74, 32.88, 33.16, 33.21, 33.2, 33.13, 33.04,
                        33.09, 33.31, 33.45],
                       [31.01, 31.5, 31.29, 31.59, 31.77, 31.67, 31.79, 31.94, 32.,
                        31.98, 32.1, 32.03],
                       [33.66, 33.92, 33.99, 34.21, 33.99, 34.16, 34.22, 34.44, 34.11,
                        34.37, 34.43, 34.33],
                       [32.91, 33.59, 33.56, 33.96, 34.83, 34.98, 35.43, 35.09, 35.94,
                        35.99, 36.16, 35.74],
                       [33.23, 34.1, 33.87, 34.28, 34.23, 34.37, 34.19, 34.38, 34.23,
                        34.48, 34.34, 34.4],
                       [32.34, 32.3, 32.13, 32.4, 32.74, 32.57, 32.81, 32.92, 32.89,
                        32.92, 33.01, 32.73],
                       [30.77, 31.1, 31.2, 31.36, 31.31, 31.44, 31.31, 31.7, 31.75,
                        31.64, 31.86, 31.97],
                       [31.9, 31.98, 32.04, 31.98, 31.97, 31.83, 32.04, 31.92, 32.02,
                        31.96, 32.07, 31.99],
                       [32.39, 32.13, 32.24, 32.28, 32.17, 32.22, 32.1, 32.25, 32.4,
                        32.55, 32.64, 32.48]])

    return split_number, splits


def eda_plot_all_your_data(split_number, splits):
    # Plot the splits for each swimmer
    for splitset in splits:
        _ = plt.plot(split_number, splitset, linewidth=1, color='lightgray')

    # Compute the mean split times
    mean_splits = np.mean(splits, axis=0)

    # Plot the mean split times
    plt.plot(split_number, mean_splits, marker='.', linewidth=3, markersize=12)

    # Label axes and show plot
    _ = plt.xlabel('split number')
    _ = plt.ylabel('split time (s)')
    plt.show()


def linear_regression_of_average_split_time(split_number, splits):
    mean_splits = np.mean(splits, axis=0)

    # Perform regression
    slowdown, split_3 = np.polyfit(split_number, mean_splits, deg=1)

    # Compute pairs bootstrap
    bs_reps, _ = dcst.draw_bs_pairs_linreg(
        split_number, mean_splits, size=10000)

    # Compute confidence interval
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Plot the data with regressions line
    _ = plt.plot(split_number, mean_splits, marker='.', linestyle='none')
    _ = plt.plot(split_number, slowdown * split_number + split_3, '-')

    # Label axes and show plot
    _ = plt.xlabel('split number')
    _ = plt.ylabel('split time (s)')
    plt.show()

    # Print the slowdown per split
    print("""
    mean slowdown: {0:.3f} sec./split
    95% conf int of mean slowdown: [{1:.3f}, {2:.3f}] sec./split""".format(
        slowdown, *conf_int))


def hypothesis_are_they_slowing_down(split_number, splits):
    mean_splits = np.mean(splits, axis=0)
    # Observed correlation
    rho = dcst.pearson_r(split_number, mean_splits)

    # Initialize permutation reps
    perm_reps_rho = np.empty(10000)

    # Make permutation reps
    for i in range(10000):
        # Scramble the split number array
        scrambled_split_number = np.random.permutation(split_number)

        # Compute the Pearson correlation coefficient
        perm_reps_rho[i] = dcst.pearson_r(scrambled_split_number, mean_splits)

    # Compute and print p-value
    p_val = np.sum(perm_reps_rho >= rho) / len(perm_reps_rho)
    print('p =', p_val)


sns.set()
split_number, splits = load_data()
#eda_plot_all_your_data(split_number, splits)
#linear_regression_of_average_split_time(split_number, splits)
hypothesis_are_they_slowing_down(split_number, splits)
