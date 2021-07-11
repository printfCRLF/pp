import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, draw_bs_reps, draw_bs_pairs_linreg
from data import rainfall, nohitter_times, illiteracy, fertility


def pairs_bootstrap_of_literacy_fertility():
    bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(
        illiteracy, fertility, 1000)
    print(np.percentile(bs_slope_reps, [2.5, 97.5]))

    _ = plt.hist(bs_slope_reps, bins=50, density=True)
    _ = plt.xlabel('slope')
    _ = plt.ylabel('PDF')
    plt.show()


def plotting_bootstrap_regressions():
    bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(
        illiteracy, fertility, 1000)
    x = np.array([0, 100])

    for i in range(100):
        _ = plt.plot(x,
                     bs_slope_reps[i]*x + bs_intercept_reps[i],
                     linewidth=0.5, alpha=0.2, color='red')

    _ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
    _ = plt.xlabel('illiteracy')
    _ = plt.ylabel('fertility')
    plt.margins(0.02)
    plt.show()


sns.set()
pairs_bootstrap_of_literacy_fertility()
plotting_bootstrap_regressions()
