import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, permutation_sample, draw_perm_reps, draw_bs_reps
from data import rain_june, rain_november, force_a, force_b, forces_concat, empirical_diff_means


def visualizing_permutation_sampling():
    for i in range(50):
        perm_sample_1, perm_sample_2 = permutation_sample(
            rain_june, rain_november)
        x_1, y_1 = ecdf(perm_sample_1)
        x_2, y_2 = ecdf(perm_sample_2)
        # Plot ECDFs of permutation sample
        _ = plt.plot(x_1, y_1, marker='.', linestyle='none',
                     color='red', alpha=0.02)
        _ = plt.plot(x_2, y_2, marker='.', linestyle='none',
                     color='blue', alpha=0.02)

    # Create and plot ECDFs from original data
    x_1, y_1 = ecdf(rain_june)
    x_2, y_2 = ecdf(rain_november)
    _ = plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
    _ = plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')
    plt.margins(0.02)
    _ = plt.xlabel('monthly rainfall (mm)')
    _ = plt.ylabel('ECDF')
    plt.show()


sns.set()
visualizing_permutation_sampling()
