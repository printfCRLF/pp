import pandas as pd
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    file = 'data/2015_FINA.csv'
    df = pd.read_csv(file, sep=',', comment='#')
    is_men = df['gender'] == 'M'
    is_freestyle = df['stroke'] == 'FREE'
    is_distance_200 = df['distance'] == 200
    is_split_4 = df['split'] == 4
    is_round_pre = df['round'] == 'PRE'
    mens_200_free_heats = df['swimtime'][is_men &
                                         is_freestyle & is_distance_200 & is_split_4 & is_round_pre]
    return mens_200_free_heats


def graphical_eda_of_means_200_free_heats(mens_200_free_heats):
    # Generate x and y values for ECDF: x, y
    x, y = dcst.ecdf(mens_200_free_heats)

    # Plot the ECDF as dots
    _ = plt.plot(x, y, marker='.', linestyle='none')

    # Label axes and show plot
    _ = plt.xlabel('time (s)')
    _ = plt.ylabel('ECDF')
    plt.show()


def time_with_confidence_interval(mens_200_free_heats):
    # Compute mean and median swim times
    mean_time = np.mean(mens_200_free_heats)
    median_time = np.median(mens_200_free_heats)

    # Draw 10,000 bootstrap replicates of the mean and median
    bs_reps_mean = dcst.draw_bs_reps(mens_200_free_heats, np.mean, size=10000)
    bs_reps_median = dcst.draw_bs_reps(
        mens_200_free_heats, np.median, size=10000)

    # Compute the 95% confidence intervals
    conf_int_mean = np.percentile(bs_reps_mean, [2.5, 97.5])
    conf_int_median = np.percentile(bs_reps_median, [2.5, 97.5])

    # Print the result to the screen
    print("""
    mean time: {0:.2f} sec.
    95% conf int of mean: [{1:.2f}, {2:.2f}] sec.

    median time: {3:.2f} sec.
    95% conf int of median: [{4:.2f}, {5:.2f}] sec.
    """.format(mean_time, *conf_int_mean, median_time, *conf_int_median))


sns.set()
mens_200_free_heats = load_data()
graphical_eda_of_means_200_free_heats(mens_200_free_heats)
time_with_confidence_interval(mens_200_free_heats)
