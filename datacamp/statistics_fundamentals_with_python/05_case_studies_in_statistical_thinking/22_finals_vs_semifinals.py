import pandas as pd
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    file = 'data/2015_FINA.csv'
    df = pd.read_csv(file, sep=',', comment='#')
    is_female = df['gender'] == 'F'
    is_short_distance = df['distance'].isin([50, 100, 200])
    is_final = df['round'] == 'FIN'
    data = df[['eventid', 'split', 'swimtime']][is_female &
                                                is_short_distance & is_final]
    final_times = np.array([52.52,  24.12,  52.82,  24.36,  57.67, 116.41,  58.26,  27.66,
                            125.81,  58.75,  27.92, 126.78,  25.93,  24.44,  27.26,  58.22,
                            128.66,  24.39,  57.69, 143.61, 128.51,  30.74,  59.02,  27.11,
                            57.85,  66.55, 142.76,  57.48,  25.37, 116.27,  54.76, 126.51,
                            27.58, 130.2, 142.76,  57.05,  25.34,  58.86,  27.73,  25.78,
                            142.76,  25.85,  24.51,  59.78,  27.99,  57.94, 126.78, 128.49,
                            28.17, 116.19, 126.84, 127.76, 129.53,  67.1,  31.12, 115.32,
                            67.6,  66.42,  30.11, 125.56,  66.43, 141.15, 143.19,  66.36,
                            30.14, 116.79,  53.58,  53.17,  24.22,  25.64,  26.2, 116.16,
                            127.64,  65.66,  30.13,  59.66, 143.59,  55.64,  52.7,  24.96,
                            24.31,  67.17,  30.05,  31.14,  53.93,  24.57, 142.44, 115.16,
                            59.4, 115.49,  54., 126.34,  30.2, 126.95,  59.99, 126.4])
    semi_times = np.array([53.,  24.32,  52.84,  24.22,  57.59, 116.95,  58.56,  27.7,
                           126.56,  59.05,  27.83, 127.57,  25.81,  24.38,  27.41,  58.05,
                           128.99,  24.52,  57.52, 142.82, 128.16,  31.03,  59.33,  27.18,
                           57.63,  66.28, 143.06,  57.36,  25.79, 116.44,  53.91, 127.08,
                           27.67, 127.69, 141.99,  57.04,  25.27,  58.84,  27.63,  25.88,
                           142.9,  25.71,  24.5,  59.71,  27.88,  57.77, 126.64, 129.16,
                           28.01, 116.51, 126.18, 127.05, 129.04,  67.11,  30.9, 116.23,
                           66.95,  66.21,  30.78, 126.36,  66.64, 142.15, 142.88,  65.64,
                           29.98, 116.91,  53.38,  53.78,  24.23,  25.9,  25.91, 116.56,
                           128.74,  65.6,  30.14,  59.55, 142.72,  55.74,  52.78,  25.06,
                           24.31,  66.76,  30.39,  30.64,  53.81,  24.47, 142.04, 116.76,
                           59.42, 116.37,  53.92, 127.79,  30.25, 127.52,  59.63, 127.57])
    return final_times, semi_times


def eda_final_vs_semifinals(semi_times, final_times):
    # Compute fractional difference in time between finals and semis
    f = (semi_times - final_times) / semi_times

    # Generate x and y values for the ECDF: x, y
    x, y = dcst.ecdf(f)

    # Make a plot of the ECDF
    _ = plt.plot(x, y, marker='.', linestyle='none')

    # Label axes and show plot
    _ = plt.xlabel('f')
    _ = plt.ylabel('ECDF')
    plt.show()


def parameter_estimates(semi_times, final_times):
    f = (semi_times - final_times) / semi_times
    # Mean fractional time difference: f_mean
    f_mean = np.mean(f)

    # Get bootstrap reps of mean: bs_reps
    bs_reps = dcst.draw_bs_reps(f, np.mean, size=10000)

    # Compute confidence intervals: conf_int
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Report
    print("""
    mean frac. diff.: {0:.5f}
    95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]""".format(f_mean, *conf_int))


def swap_random(a, b):
    """Randomly swap entries in two arrays."""
    # Indices to swap
    swap_inds = np.random.random(size=len(a)) < 0.5

    # Make copies of arrays a and b for output
    a_out = np.copy(a)
    b_out = np.copy(b)

    # Swap values
    b_out[swap_inds] = a[swap_inds]
    a_out[swap_inds] = b[swap_inds]

    return a_out, b_out


def do_women_swim_in_the_same_way(semi_times, final_times):
    f = (semi_times - final_times) / semi_times
    # Mean fractional time difference: f_mean
    f_mean = np.mean(f)

    # Set up array of permutation replicates
    perm_reps = np.empty(1000)

    for i in range(1000):
        # Generate a permutation sample
        semi_perm, final_perm = swap_random(semi_times, final_times)

        # Compute f from the permutation sample
        f = (semi_perm - final_perm) / semi_perm

        # Compute and store permutation replicate
        perm_reps[i] = np.mean(f)

    # Compute and print p-value
    print('p =', np.sum(perm_reps >= f_mean) / 1000)


sns.set()
final_times, semi_times = load_data()
eda_final_vs_semifinals(semi_times, final_times)
parameter_estimates(semi_times, final_times)
do_women_swim_in_the_same_way(semi_times, final_times)
