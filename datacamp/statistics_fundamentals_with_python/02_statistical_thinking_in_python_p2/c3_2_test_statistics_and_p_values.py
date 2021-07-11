import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, permutation_sample, draw_perm_reps, draw_bs_reps
from data import rain_june, rain_november, force_a, force_b, forces_concat, empirical_diff_means


def eda_before_hypothesis_testing():
    _ = sns.swarmplot('ID', 'impact_force', data=df)

    # Label axes
    _ = plt.xlabel('frog')
    _ = plt.ylabel('impact force (N)')

    # Show the plot
    plt.show()


def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""
    diff = np.mean(data_1) - np.mean(data_2)
    return diff


def permutation_test_on_frog_data():
    # Compute difference of mean impact force from experiment: empirical_diff_means
    empirical_diff_means = diff_of_means(force_a, force_b)
    # Draw 10,000 permutation replicates: perm_replicates
    perm_replicates = draw_perm_reps(force_a, force_b,
                                     diff_of_means, size=10000)

    # Compute p-value: p
    p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

    # Print the result
    print('p-value =', p)
    # The avareage strike force of Frog A(Adult) was 0.71 Newtons, and that of Frog B(Juvenile) was 0.42N, for a difference of 0.29N
    # there is p chance that you would get the difference of means observaed in the experiment if the frogs were exactly the same.


sns.set()
permutation_test_on_frog_data()
