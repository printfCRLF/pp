import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dc_stat_think as dcst
from scipy import stats
import seaborn as sns


def load_data():
    file = 'data/park_bacterial_growth.csv'
    df = pd.read_csv(file, sep=',', comment='#')
    bac_area = df.iloc[:, 0].to_numpy()
    t = df.iloc[:,  1].to_numpy()
    return bac_area, t


def assessing_the_growth_rate(bac_area, t):
    # Compute logarithm of the bacterial area: log_bac_area
    log_bac_area = np.log(bac_area)

    # Compute the slope and intercept: growth_rate, log_a0
    growth_rate, log_a0 = np.polyfit(t, log_bac_area, 1)

    # Draw 10,000 pairs bootstrap replicates: growth_rate_bs_reps, log_a0_bs_reps
    growth_rate_bs_reps, log_a0_bs_reps = dcst.draw_bs_pairs_linreg(
        t, log_bac_area, size=10000
    )

    # Compute confidence intervals: growth_rate_conf_int
    growth_rate_conf_int = np.percentile(growth_rate_bs_reps, [2.5, 97.5])

    # Print the result to the screen
    print("""
    Growth rate: {0:.4f} 1/hour
    95% conf int: [{1:.4f}, {2:.4f}] 1/hour
    """.format(growth_rate, *growth_rate_conf_int))


def plotting_growth_curve(bac_area, t):
    log_bac_area = np.log(bac_area)
    growth_rate_bs_reps, log_a0_bs_reps = dcst.draw_bs_pairs_linreg(
        t, log_bac_area, size=10000)

    # Plot data points in a semilog-y plot with axis labeles
    _ = plt.semilogy(t, bac_area, marker='.', linestyle='none')

    # Generate x-values for the bootstrap lines: t_bs
    t_bs = np.array([0, 14])

    # Plot the first 100 bootstrap lines
    for i in range(100):
        y = np.exp(growth_rate_bs_reps[i] * t_bs + log_a0_bs_reps[i])
        _ = plt.semilogy(t_bs, y, linewidth=0.5, alpha=0.05, color='red')

    # Label axes and show plot
    _ = plt.xlabel('time (hr)')
    _ = plt.ylabel('area (sq. µm)')
    plt.show()


sns.set()
bac_area, t = load_data()
assessing_the_growth_rate(bac_area, t)
plotting_growth_curve(bac_area, t)
