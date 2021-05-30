import pandas as pd
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    lanes = np.arange(1, 9)
    f_13 = np.array([-0.01562214, -0.0146381, -0.00977673, -0.00525713,  0.00204104,
                     0.00381014,  0.0075664,  0.01525869])
    f_15 = np.array([-0.00516018, -0.00392952, -0.00099284,  0.00059953, -0.002424,
                     -0.00451099,  0.00047467,  0.00081962])
    return lanes, f_13, f_15


def eda_mean_differences_between_odd_and_even_splits(lanes, f_13, f_15):
    # Plot the the fractional difference for 2013 and 2015
    _ = plt.plot(lanes, f_13, marker='.', markersize=12, linestyle='none')
    _ = plt.plot(lanes, f_15, marker='.', markersize=12, linestyle='none')

    # Add a legend
    _ = plt.legend((2013, 2015))

    # Label axes and show plot
    _ = plt.xlabel('lane')
    _ = plt.ylabel('frac. diff. (odd-even)')
    plt.show()


def how_does_current_effect_depend_on_lane_position(lanes, f_13):
    # Compute the slope and intercept of the frac diff/lane curve
    slope, intercept = np.polyfit(lanes, f_13, deg=1)
    _ = plt.plot(lanes, f_13, marker='.', markersize=12, linestyle='none')
    _ = plt.xlabel('lane')
    _ = plt.ylabel('frac. diff. (odd-even)')

    # Compute bootstrap replicates
    bs_reps_slope, bs_reps_int = dcst.draw_bs_pairs_linreg(
        lanes, f_13, size=10000)

    # Compute 95% confidence interval of slope
    conf_int = np.percentile(bs_reps_slope, [2.5, 97.5])

    # Print slope and confidence interval
    print("""
    slope: {0:.5f} per lane
    95% conf int: [{1:.5f}, {2:.5f}] per lane""".format(slope, *conf_int))

    # x-values for plotting regression lines
    x = np.array([1, 8])

    # Plot 100 bootstrap replicate lines
    for i in range(100):
        _ = plt.plot(x, bs_reps_slope[i] * x + bs_reps_int[i],
                     color='red', alpha=0.2, linewidth=0.5)

    # Update the plot
    plt.draw()
    plt.show()


def hypothesis_testing(lanes, f_13):
    # Compute observed correlation: rho
    rho = dcst.pearson_r(lanes, f_13)

    # Initialize permutation reps: perm_reps_rho
    perm_reps_rho = np.empty(10000)

    # Make permutation reps
    for i in range(10000):
        # Scramble the lanes array: scrambled_lanes
        scrambled_lanes = np.random.permutation(lanes)

        # Compute the Pearson correlation coefficient
        perm_reps_rho[i] = dcst.pearson_r(scrambled_lanes, f_13)

    # Compute and print p-value
    p_val = np.sum(perm_reps_rho >= rho) / 10000
    print('p =', p_val)


sns.set()
lanes, f_13, f_15 = load_data()
eda_mean_differences_between_odd_and_even_splits(lanes, f_13, f_15)
how_does_current_effect_depend_on_lane_position(lanes, f_13)
hypothesis_testing(lanes, f_13)
