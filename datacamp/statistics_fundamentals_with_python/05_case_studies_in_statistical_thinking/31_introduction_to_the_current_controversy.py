import pandas as pd
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    swimtime_low_lanes = np.array(
        [24.66, 23.28, 27.2, 24.95, 32.34, 24.66, 26.17, 27.93, 23.35,
         22.93, 21.93, 28.33, 25.14, 25.19, 26.11, 31.31, 27.44, 21.85,
         27.48, 30.66, 21.74, 23.22, 27.93, 21.42, 24.79, 26.46])

    swimtime_high_lanes = np.array(
        [24.62, 22.9, 27.05, 24.76, 30.31, 24.54, 26.12, 27.71, 23.15,
         23.11, 21.62, 28.02, 24.73, 24.95, 25.83, 30.61, 27.04, 21.67,
         27.16, 30.23, 21.51, 22.97, 28.05, 21.65, 24.54, 26.06])

    return swimtime_low_lanes, swimtime_high_lanes


def ecdf_of_improvement_from_low_to_high_lanes(swimtime_low_lanes, swimtime_high_lanes):
    # Compute the fractional improvement of being in high lane: f
    f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes
    # Make x and y values for ECDF: x, y
    x, y = dcst.ecdf(f)
    # Plot the ECDFs as dots
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('f')
    _ = plt.ylabel('ECDF')

    plt.show()


def estimation_of_mean_improvement(swimtime_low_lanes, swimtime_high_lanes):
    f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes
    # Compute the mean difference: f_mean
    f_mean = np.mean(f)
    # Draw 10,000 bootstrap replicates: bs_reps
    bs_reps = dcst.draw_bs_reps(f, np.mean, 10000)

    # Compute 95% confidence interval: conf_int
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Print the result
    print("""
    mean frac. diff.: {0:.5f}
    95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]""".format(f_mean, *conf_int))


def hypothesis_test(swimtime_low_lanes, swimtime_high_lanes):
    f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes
    f_mean = np.mean(f)
    # Shift f: f_shift
    f_shift = f - f_mean

    # Draw 100,000 bootstrap replicates of the mean: bs_reps
    bs_reps = dcst.draw_bs_reps(f_shift, np.mean, 100000)

    # Compute and report the p-value
    p_val = np.sum(bs_reps >= f_mean) / 100000
    print('p =', p_val)


def did_the_2015_event_have_this_problem():
    swimtime_low_lanes_15 = np.array([27.66, 24.69, 23.29, 23.05, 26.87, 31.03, 22.04, 24.51, 21.86,
                                      25.64, 25.91, 24.77, 30.14, 27.23, 24.31, 30.2, 26.86])
    swimtime_high_lanes_15 = np.array([27.7, 24.64, 23.21, 23.09, 26.87, 30.74, 21.88, 24.5, 21.86,
                                       25.9, 26.2, 24.73, 30.13, 26.92, 24.31, 30.25, 26.76])

    # Compute f and its mean
    f = (swimtime_low_lanes_15 - swimtime_high_lanes_15) / swimtime_low_lanes_15
    x, y = dcst.ecdf(f)
    # Plot the ECDFs as dots
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('f')
    _ = plt.ylabel('ECDF')
    plt.show()
    
    f_mean = np.mean(f)

    # Draw 10,000 bootstrap replicates
    bs_reps = dcst.draw_bs_reps(f, np.mean, size=10000)

    # Compute 95% confidence interval
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Shift f
    f_shift = f - f_mean

    # Draw 100,000 bootstrap replicates of the mean
    bs_reps = dcst.draw_bs_reps(f_shift, np.mean, size=100000)

    # Compute the p-value
    p_val = np.sum(bs_reps >= f_mean) / 100000

    # Print the results
    print("""
    mean frac. diff.: {0:.5f}
    95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]
    p-value: {3:.5f}""".format(f_mean, *conf_int, p_val))


sns.set()
#swimtime_low_lanes, swimtime_high_lanes = load_data()
#ecdf_of_improvement_from_low_to_high_lanes(
#    swimtime_low_lanes, swimtime_high_lanes)
#estimation_of_mean_improvement(swimtime_low_lanes, swimtime_high_lanes)
#hypothesis_test(swimtime_low_lanes, swimtime_high_lanes)
did_the_2015_event_have_this_problem()