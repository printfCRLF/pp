import numpy as np


def generating_a_single_permutation():
    # Concatenate the two arrays donations_A and donations_B into data
    len_A, len_B = len(donations_A), len(donations_B)
    data = np.concatenate([donations_A, donations_B])

    # Get a single permutation of the concatenated length
    perm = np.random.permutation(len(donations_A) + len(donations_B))

    # Calculate the permutated datasets and difference in means
    permuted_A = data[perm[:len(donations_A)]]
    permuted_B = data[perm[len(donations_A):]]
    diff_in_means = np.mean(permuted_A) - np.mean(permuted_B)
    print("Difference in the permuted mean values = {}.".format(diff_in_means))


def hypothesis_testing_difference_of_means():
    # Generate permutations equal to the number of repetitions
    perm = np.array([np.random.permutation(
        len(donations_A) + len(donations_B)) for i in range(reps)])
    permuted_A_datasets = data[perm[:, :len(donations_A)]]
    permuted_B_datasets = data[perm[:, len(donations_A):]]

    # Calculate the difference in means for each of the datasets
    samples = np.mean(permuted_A_datasets, axis=1) - \
        np.mean(permuted_B_datasets, axis=1)

    # Calculate the test statistic and p-value
    test_stat = np.mean(donations_A) - np.mean(donations_B)
    p_val = 2*np.sum(samples >= np.abs(test_stat))/reps
    print("p-value = {}".format(p_val))


def hypothesis_testing_non_standard_statistics():
    # Calculate the difference in 80th percentile and median for each of the permuted datasets (A and B)
    samples_percentile = np.percentile(
        permuted_A_datasets, 80, axis=1) - np.percentile(permuted_B_datasets, 80, axis=1)
    samples_median = np.median(
        permuted_A_datasets, axis=1) - np.median(permuted_B_datasets, axis=1)

    # Calculate the test statistic from the original dataset and corresponding p-values
    test_stat_percentile = np.percentile(
        donations_A, 80) - np.percentile(donations_B, 80)
    test_stat_median = np.median(donations_A) - np.median(donations_B)
    p_val_percentile = 2*np.sum(samples_percentile >=
                                np.abs(test_stat_percentile))/reps
    p_val_median = 2*np.sum(samples_median >= np.abs(test_stat_median))/reps

    print("80th Percentile: test statistic = {}, p-value = {}".format(
        test_stat_percentile, p_val_percentile))
    print("Median: test statistic = {}, p-value = {}".format(test_stat_median, p_val_median))
