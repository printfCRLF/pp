import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from util import ecdf, draw_bs_reps, draw_bs_pairs_linreg
from data import rainfall, nohitter_times, illiteracy, fertility

sns.set()
def visualizing_bootstrap_samples(): 
    for _ in range(50):
        bs_sample = np.random.choice(rainfall, size=len(rainfall))
        x, y = ecdf(bs_sample)
        _ = plt.plot(x, y, marker='.', linestyle='none',
                    color='gray', alpha=0.1)

    x, y = ecdf(rainfall)
    _ = plt.plot(x, y, marker='.')
    plt.margins(0.02)
    _ = plt.xlabel('yearly rainfall (mm)')
    _ = plt.ylabel('ECDF')
    plt.show()    

    
def standard_error_of_mean(): 
    bs_replicates = draw_bs_reps(rainfall, np.mean, size=10000)
    # SDSM, Standard deviation of the sample mean, is also called standard error, standard error of mean (stand error of proportion)
    sem = np.std(rainfall) / np.sqrt(len(rainfall))
    print(sem)

    bs_std = np.std(bs_replicates)
    print(bs_std)

    _ = plt.hist(bs_replicates, bins=50, density=True)
    _ = plt.xlabel('mean annual rainfall (mm)')
    _ = plt.ylabel('PDF')
    plt.show()

def replicates_of_variance(): 
    bs_replicates = draw_bs_reps(rainfall, np.var, 10000)
    bs_replicates = bs_replicates / 100

    _ = plt.hist(bs_replicates, bins=50, density=True)
    _ = plt.xlabel('variance of annual rainfall (sq. cm)')
    _ = plt.ylabel('PDF')
    plt.show()

def confidence_interval_on_rate_of_no_hitters(): 


    bs_replicates = draw_bs_reps(nohitter_times, np.mean, 10000)
    conf_int = np.percentile(bs_replicates, [2.5, 97.5])


    print('95% confidence interval =', conf_int, 'games')

    _ = plt.hist(bs_replicates, bins=50, density=True)
    _ = plt.xlabel(r'$\tau$ (games)')
    _ = plt.ylabel('PDF')
    plt.show()

def pairs_bootstrap_of_literacy_fertility(): 
    bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(illiteracy, fertility, 1000)
    print(np.percentile(bs_slope_reps, [2.5, 97.5]))

    _ = plt.hist(bs_slope_reps, bins=50, density=True)
    _ = plt.xlabel('slope')
    _ = plt.ylabel('PDF')
    plt.show()

def plotting_bootstrap_regressions(): 
    bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(illiteracy, fertility, 1000)
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

#visualizing_bootstrap_samples()
#standard_error_of_mean()
#replicates_of_variance()
#confidence_interval_on_rate_of_no_hitters()
#pairs_bootstrap_of_literacy_fertility()
plotting_bootstrap_regressions()

