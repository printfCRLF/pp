import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import draw_perm_reps, diff_of_means, pearson_r, ecdf, draw_bs_reps
from data import nht_dead, nht_live, illiteracy, fertility, control, treated


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


def a_time_on_website_analog():
    # Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
    nht_diff_obs = diff_of_means(nht_dead, nht_live)
    # Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
    perm_replicates = draw_perm_reps(nht_dead, nht_live, diff_of_means, 10000)
    # Compute and print the p-value: p
    p = np.sum(perm_replicates <= nht_diff_obs) / len(perm_replicates)
    print('no_hitter p-val =', p)


sns.set()
the_votes_for_the_civil_rights_acts()
# p = 0.0003.
# We permutate democratic votes with republicans vote as if they are the same,
# the p value shows that it is only 0.03% chance that we will see percentage of yea votes lower than 62.7%
# which means that the democratic party is racially biased.

a_time_on_website_analog()
# p = 0.0001
# In empirical observations, the nht_diff_obs is -345
# If the rule change does not make the average time between no-hitters longer, we have a 0.001% of chance to see average_time smaller than -345
# which is a very small chance, therefore, the rule change does make the average time between no-hitters longer
