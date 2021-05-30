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


def interearthquake_time_estimates_for_parkfield(time_gap):
    # Compute the mean time gap: mean_time_gap
    mean_time_gap = np.mean(time_gap)

    # Standard deviation of the time gap: std_time_gap
    std_time_gap = np.std(time_gap)

    # Generate theoretical Exponential distribution of timings: time_gap_exp
    time_gap_exp = np.random.exponential(mean_time_gap, 10000)

    # Generate theoretical Normal distribution of timings: time_gap_norm
    time_gap_norm = np.random.normal(mean_time_gap, std_time_gap, 10000)

    # Plot theoretical CDFs
    _ = plt.plot(*dcst.ecdf(time_gap_exp))
    _ = plt.plot(*dcst.ecdf(time_gap_norm))

    # Plot Parkfield ECDF
    _ = plt.plot(*dcst.ecdf(time_gap, formal=True, min_x=-10, max_x=50))

    # Add legend
    _ = plt.legend(('Exp.', 'Norm.'), loc='upper left')

    # Label axes, set limits and show plot
    _ = plt.xlabel('time gap (years)')
    _ = plt.ylabel('ECDF')
    _ = plt.xlim(-10, 50)
    plt.show()


def when_will_the_next_big_parkfield_quake_be(time_gap):
    mean_time_gap = np.mean(time_gap)
    std_time_gap = np.std(time_gap)

    # Draw samples from the Exponential distribution: exp_samples
    exp_samples = np.random.exponential(mean_time_gap, size=100000)

    # Draw samples from the Normal distribution: norm_samples
    norm_samples = np.random.normal(mean_time_gap, std_time_gap, size=100000)

    today = 2021.4072810712728
    last_quake = 2004.74
    # No earthquake as of today, so only keep samples that are long enough
    exp_samples = exp_samples[exp_samples > today - last_quake]
    norm_samples = norm_samples[norm_samples > today - last_quake]

    # Compute the confidence intervals with medians
    conf_int_exp = np.percentile(exp_samples, [2.5, 50, 97.5]) + last_quake
    conf_int_norm = np.percentile(norm_samples, [2.5, 50, 97.5]) + last_quake

    # Print the results
    print('Exponential:', conf_int_exp)
    print('     Normal:', conf_int_norm)


sns.set()
mags, time_gap = load_data()
interearthquake_time_estimates_for_parkfield(time_gap)
when_will_the_next_big_parkfield_quake_be(time_gap)

