import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from util import ecdf, permutation_sample, draw_perm_reps, draw_bs_reps
from data import rain_june, rain_november, force_a, force_b, forces_concat, empirical_diff_means


def visualizing_permutation_sampling(): 
    for i in range(50):
        perm_sample_1, perm_sample_2 = permutation_sample(rain_june, rain_november)
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


#visualizing_permutation_sampling()
permutation_test_on_frog_data()
