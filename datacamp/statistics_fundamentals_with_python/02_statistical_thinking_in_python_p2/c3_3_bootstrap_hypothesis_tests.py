import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, permutation_sample, draw_perm_reps, draw_bs_reps
from data import rain_june, rain_november, force_a, force_b, forces_concat, empirical_diff_means


def a_one_sample_bootstrap_hypothesis_test():
    # Make an array of translated impact forces: translated_force_b
    translated_force_b = force_b - np.mean(force_b) + 0.55

    # Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
    bs_replicates = draw_bs_reps(translated_force_b, np.mean, 10000)

    # Compute fraction of replicates that are less than the observed Frog B force: p
    p = np.sum(bs_replicates <= np.mean(force_b)) / 10000

    # Print the p-value
    print('p = ', p)


def a_two_sample_bootstrap_hypothesis_test_for_difference_of_means():
    # Compute mean of all forces: mean_force
    mean_force = np.mean(forces_concat)

    # Generate shifted arrays
    force_a_shifted = force_a - np.mean(force_a) + mean_force
    force_b_shifted = force_b - np.mean(force_b) + mean_force

    # Compute 10,000 bootstrap replicates from shifted arrays
    bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, size=10000)
    bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, size=10000)

    # Get replicates of difference of means: bs_replicates
    bs_replicates = bs_replicates_a - bs_replicates_b

    # Compute and print p-value: p
    p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates)
    print('p-value =', p)


sns.set()
# a_one_sample_bootstrap_hypothesis_test()
# a_two_sample_bootstrap_hypothesis_test_for_difference_of_means()
