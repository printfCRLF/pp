# Import the dc_stat_think module as dcst
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dc_stat_think as dcst
from scipy import stats
import seaborn as sns


def load_data():
    file = 'data/gandhi_et_al_bouts.csv'
    df = pd.read_csv(file, sep=',', comment='#')
    is_wt = df['genotype'] == 'wt'
    is_mut = df['genotype'] == 'mut'
    is_het = df['genotype'] == 'het'
    bout_lengths_wt = df['bout_length'][is_wt].to_numpy()
    bout_lengths_mut = df['bout_length'][is_mut].to_numpy()
    bout_lengths_het = df['bout_length'][is_het].to_numpy()
    return bout_lengths_wt, bout_lengths_mut, bout_lengths_het


def plot_ecdf_for_active_bout_length(bout_lengths_wt, bout_lengths_mut):
    # Generate x and y values for plotting ECDFs
    x_wt, y_wt = dcst.ecdf(bout_lengths_wt)
    x_mut, y_mut = dcst.ecdf(bout_lengths_mut)

    # Plot the ECDFs
    _ = plt.plot(x_wt, y_wt, marker='.', linestyle='none')
    _ = plt.plot(x_mut, y_mut, marker='.', linestyle='none')

    # Make a legend, label axes, and show plot
    _ = plt.legend(('wt', 'mut'))
    _ = plt.xlabel('active bout length (min)')
    _ = plt.ylabel('ECDF')
    plt.show()


def parameter_estimation_active_bout_length(bout_lengths_wt, bout_lengths_mut):
    # Compute mean active bout length
    mean_wt = np.mean(bout_lengths_wt)
    mean_mut = np.mean(bout_lengths_mut)

    # Draw bootstrap replicates
    bs_reps_wt = dcst.draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
    bs_reps_mut = dcst.draw_bs_reps(bout_lengths_mut, np.mean, size=10000)

    # Compute 95% confidence intervals
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])

    # Print the results
    print("""
    wt:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
    mut: mean = {3:.3f} min., conf. int. = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))


def permutation_test_wild_type_vs_heterozygote(bout_lengths_het, bout_lengths_wt):
    # Compute the difference of means: diff_means_exp
    diff_means_exp = np.mean(bout_lengths_het) - np.mean(bout_lengths_wt)

    # Draw permutation replicates: perm_reps
    perm_reps = dcst.draw_perm_reps(bout_lengths_het, bout_lengths_wt,
                                    dcst.diff_of_means, size=10000)

    # Compute the p-value: p-val
    p_val = np.sum(perm_reps >= diff_means_exp) / len(perm_reps)

    fig, ax = plt.subplots()
    _ = ax.hist(perm_reps, bins="sqrt", density=True)
    _ = ax.set_xlabel("bout length")
    _ = ax.set_ylabel("Probability")
    _ = ax.axvline(diff_means_exp, color="red")

    plt.show()

    # Print the result
    print('p =', p_val)


def bootstrap_hypothesis_test(bout_lengths_het, bout_lengths_wt):
    diff_means_exp = np.mean(bout_lengths_het) - np.mean(bout_lengths_wt)

    # Concatenate arrays: bout_lengths_concat
    bout_lengths_concat = np.concatenate((bout_lengths_wt, bout_lengths_het))

    # Compute mean of all bout_lengths: mean_bout_length
    mean_bout_length = np.mean(bout_lengths_concat)

    # Generate shifted arrays
    wt_shifted = bout_lengths_wt - np.mean(bout_lengths_wt) + mean_bout_length
    het_shifted = bout_lengths_het - \
        np.mean(bout_lengths_het) + mean_bout_length

    # Compute 10,000 bootstrap replicates from shifted arrays
    bs_reps_wt = dcst.draw_bs_reps(wt_shifted, np.mean, size=10000)
    bs_reps_het = dcst.draw_bs_reps(het_shifted, np.mean, size=10000)

    # Get replicates of difference of means: bs_replicates
    bs_reps = bs_reps_het - bs_reps_wt

    fig, ax = plt.subplots()
    _ = ax.hist(bs_reps, bins="sqrt", density=True)
    _ = ax.set_xlabel("bout length")
    _ = ax.set_ylabel("Probability")
    _ = ax.axvline(diff_means_exp, color="red")
    plt.show()

    # Compute and print p-value: p
    p = np.sum(bs_reps >= diff_means_exp) / len(bs_reps)
    print('p-value =', p)


sns.set()
bout_lengths_wt, bout_lengths_mut, bout_lengths_het = load_data()
# plot_ecdf_for_active_bout_length(bout_lengths_wt, bout_lengths_mut)
# parameter_estimation_active_bout_length(bout_lengths_wt, bout_lengths_mut)
# permutation_test_wild_type_vs_heterozygote(bout_lengths_het, bout_lengths_wt)
bootstrap_hypothesis_test(bout_lengths_het, bout_lengths_wt)

# The permutation test has a pretty restrictive hypothesis, that the heterozygotic and wild type
# bout lengths are identically distributed.
# A bootstrap hypothesis test tests the hypothesis that the means are equal,
# making no assummptions about the distribution.
