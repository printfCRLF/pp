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
    return mags


def eda(mags):
    # Make the plot
    _ = plt.plot(*dcst.ecdf(mags), marker='.', linestyle='none')

    # Label axes and show plot
    _ = plt.xlabel('magnitude')
    _ = plt.ylabel('ECDF')
    plt.show()


def b_value(mags, mt, perc=[2.5, 97.5], n_reps=None):
    """Compute the b-value and optionally its confidence interval."""
    # Extract magnitudes above completeness threshold: m
    m = mags[mags >= mt]

    # Compute b-value: b
    b = (np.mean(m) - mt) * np.log(10)

    # Draw bootstrap replicates
    if n_reps is None:
        return b
    else:
        m_bs_reps = dcst.draw_bs_reps(m, np.mean, size=n_reps)

        # Compute b-value from replicates: b_bs_reps
        b_bs_reps = (m_bs_reps - mt) * np.log(10)

        # Compute confidence interval: conf_int
        conf_int = np.percentile(b_bs_reps, perc)

        return b, conf_int


def the_b_value_for_parkfield(mags):
    # Compute b-value and 95% confidence interval
    b, conf_int = b_value(mags, 3, perc=[2.5, 97.5], n_reps=10000)

    # Generate samples to for theoretical ECDF
    m_theor = np.random.exponential(b/np.log(10), size=100000) + 3

    # Plot the theoretical CDF
    _ = plt.plot(*dcst.ecdf(m_theor))

    # Plot the ECDF (slicing mags >= mt)
    _ = plt.plot(*dcst.ecdf(mags[mags >= 3]), marker='.', linestyle='none')

    # Pretty up and show the plot
    _ = plt.xlabel('magnitude')
    _ = plt.ylabel('ECDF')
    _ = plt.xlim(2.8, 6.2)
    plt.show()

    # Report the results
    print("""
    b-value: {0:.2f}
    95% conf int: [{1:.2f}, {2:.2f}]""".format(b, *conf_int))

dcst.draw_perm_reps
# sns.set()
# mags = load_data()
# eda(mags)
# the_b_value_for_parkfield(mags)

