import time
from datetime import datetime as dt
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import dc_stat_think as dcst
import seaborn as sns
import datetime
from scipy import stats
import util


def load_data():
    file = 'data/oklahoma_earthquakes_1950-2017.csv'
    df = pd.read_csv(file, sep=',', comment='#', parse_dates=['time'])
    time_as_date = df['time']
    mags = df['mag']
    time = time_as_date.apply(util.toYearFraction)
    time = time.to_numpy()
    mags = mags.to_numpy()
    return time, mags


def eda(time, mags):
    # Get magnitudes before and after 2010
    mags_pre = mags[time < 2010]
    mags_post = mags[time >= 2010]

    # Generate ECDFs
    _ = plt.plot(*dcst.ecdf(mags_pre), marker='.', linestyle='none')
    _ = plt.plot(*dcst.ecdf(mags_post), marker='.', linestyle='none')

    # Label axes and show plot
    _ = plt.xlabel('magnitude')
    _ = plt.ylabel('ECDF')
    plt.legend(('1980 though 2009', '2010 through mid-2017'), loc='upper left')
    plt.show()


def hypothesis_test(time, mags): 
    mags_pre = mags[time < 2010]
    mags_post = mags[time >= 2010]
    mt = 3

    # Only magnitudes above completeness threshold
    mags_pre = mags_pre[mags_pre >= mt]
    mags_post = mags_post[mags_post >= mt]

    # Observed difference in mean magnitudes: diff_obs
    diff_obs = np.mean(mags_post) - np.mean(mags_pre)

    # Generate permutation replicates: perm_reps
    perm_reps = dcst.draw_perm_reps(mags_post, mags_pre, dcst.diff_of_means, size=10000)

    # Compute and print p-value
    p_val = np.sum(perm_reps < diff_obs) / 10000
    print('p =', p_val)    

sns.set()
time, mags = load_data()
#eda(time, mags)
hypothesis_test(time, mags)
