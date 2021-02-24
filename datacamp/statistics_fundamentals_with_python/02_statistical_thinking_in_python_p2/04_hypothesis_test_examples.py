import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from util import draw_perm_reps, diff_of_means, pearson_r, ecdf, draw_bs_reps
from data import nht_dead, nht_live, illiteracy, fertility, control, treated

sns.set(),

def the_votes_for_the_civil_rights_acts(): 
    # Construct arrays of data: dems, reps
    dems = np.array([True] * 153 + [False] * 91)        # 62.7%
    reps = np.array([True] * 136 + [False] * 35)        # 79.5%

    def frac_yea_dems(dems, reps):
        """Compute fraction of Democrat yea votes."""
        frac = np.sum(dems) / len(dems)
        return frac

    # Acquire permutation samples: perm_replicates
    perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, 10000)

    # Compute and print p-value: p
    p = np.sum(perm_replicates <= 153/244) / len(perm_replicates)
    print('civial rights act, p-value =', p)    

the_votes_for_the_civil_rights_acts()
#p = 0.0003. 
# We permutate democratic votes with republicans vote as if they are the same, 
# the p value shows that it is only 0.03% chance that we will see percentage of yea votes lower than 62.7%
# which means that the democratic party is racially biased. 

def a_time_on_website_analog(): 
    # Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
    nht_diff_obs = diff_of_means(nht_dead, nht_live)
    # Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
    perm_replicates = draw_perm_reps(nht_dead, nht_live, diff_of_means, 10000)
    # Compute and print the p-value: p
    p = np.sum(perm_replicates <= nht_diff_obs) / len(perm_replicates)
    print('no_hitter p-val =', p)    

a_time_on_website_analog()
#p = 0.0001
#In empirical observations, the nht_diff_obs is -345
#If the rule change does not make the average time between no-hitters longer, we have a 0.001% of chance to see average_time smaller than -345
#which is a very small chance, therefore, the rule change does make the average time between no-hitters longer

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

hypothesis_test_on_pearson_correlation()
# p = 0.0
# it is extremely unlikely that you see a permutation replicates those pearson correlation value
# is larger then the observed pearson correlation value. 
# therefore, we reject the null hypothesis and prove that the correlation from the observation

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

do_neonicotinoid_insecticides_have_unintended_consequences()

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


