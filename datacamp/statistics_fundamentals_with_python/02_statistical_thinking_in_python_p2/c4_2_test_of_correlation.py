import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import draw_perm_reps, diff_of_means, pearson_r, ecdf, draw_bs_reps
from data import nht_dead, nht_live, illiteracy, fertility, control, treated


def hypothesis_test_on_pearson_correlation():
    # Compute observed correlation: r_obs
    r_obs = pearson_r(illiteracy, fertility)

    # Initialize permutation replicates: perm_replicates
    perm_replicates = np.empty(10000)

    # Draw replicates
    for i in range(10000):
        # Permute illiteracy measurments: illiteracy_permuted
        illiteracy_permuted = np.random.permutation(illiteracy)

        # Compute Pearson correlation
        perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

    # Compute p-value: p
    p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
    print('pearson correlation, p-val =', p)


def do_neonicotinoid_insecticides_have_unintended_consequences():
    # Compute x,y values for ECDFs
    x_control, y_control = ecdf(control)
    x_treated, y_treated = ecdf(treated)

    # Plot the ECDFs
    plt.plot(x_control, y_control, marker='.', linestyle='none')
    plt.plot(x_treated, y_treated, marker='.', linestyle='none')

    # Set the margins
    plt.margins(0.02)

    # Add a legend
    plt.legend(('control', 'treated'), loc='lower right')

    # Label axes and show plot
    plt.xlabel('millions of alive sperm per mL')
    plt.ylabel('ECDF')
    plt.show()


def bootstrap_hypothesis_test_on_bee_sperm_counts():
    # Compute the difference in mean sperm count: diff_means
    diff_means = np.mean(control) - np.mean(treated)

    # Compute mean of pooled data: mean_count
    mean_count = np.mean(np.concatenate((control, treated)))

    # Generate shifted data sets
    control_shifted = control - np.mean(control) + mean_count
    treated_shifted = treated - np.mean(treated) + mean_count

    # Generate bootstrap replicates
    bs_reps_control = draw_bs_reps(control_shifted,
                                   np.mean, size=10000)
    bs_reps_treated = draw_bs_reps(treated_shifted,
                                   np.mean, size=10000)

    # Get replicates of difference of means: bs_replicates
    bs_replicates = bs_reps_control - bs_reps_treated

    # Compute and print p-value: p
    p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
        / len(bs_replicates)
    print('bee_sperm_counts, p-value =', p)


hypothesis_test_on_pearson_correlation()
# p = 0.0
# it is extremely unlikely that you see a permutation replicates those pearson correlation value
# is larger then the observed pearson correlation value.
# therefore, we reject the null hypothesis and prove that the correlation from the observation

do_neonicotinoid_insecticides_have_unintended_consequences()
