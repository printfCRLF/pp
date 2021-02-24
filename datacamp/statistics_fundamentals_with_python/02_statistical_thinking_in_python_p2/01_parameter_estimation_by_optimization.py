import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from util import ecdf
from data import nohitter_times

sns.set()
def how_often_do_we_get_no_hitters():
    np.random.seed(42)
    tau = np.mean(nohitter_times)
    inter_nohitter_time = np.random.exponential(tau, 100000)

    _ = plt.hist(inter_nohitter_time,
                bins=50, normed=True, histtype='step')
    _ = plt.xlabel('Games between no-hitters')
    _ = plt.ylabel('PDF')
    plt.show()

def do_the_data_follow_our_story(): 
    x, y = ecdf(nohitter_times)
    np.random.seed(42)
    tau = np.mean(nohitter_times)
    inter_nohitter_time = np.random.exponential(tau, 100000)
    x_theor, y_theor = ecdf(inter_nohitter_time)

    plt.plot(x_theor, y_theor)
    plt.plot(x, y, marker='.', linestyle='none')
    plt.margins(0.02)
    plt.xlabel('Games between no-hitters')
    plt.ylabel('CDF')
    plt.show()

def how_is_this_parameter_optimal(): 
    x, y = ecdf(nohitter_times)
    np.random.seed(42)
    tau = np.mean(nohitter_times)
    inter_nohitter_time = np.random.exponential(tau, 100000)
    x_theor, y_theor = ecdf(inter_nohitter_time)

    plt.plot(x_theor, y_theor)
    plt.plot(x, y, marker='.', linestyle='none')
    plt.margins(0.02)
    plt.xlabel('Games between no-hitters')
    plt.ylabel('CDF')

    samples_half = np.random.exponential(tau/2, 10000)
    samples_double = np.random.exponential(tau*2, 10000)
    x_half, y_half = ecdf(samples_half)
    x_double, y_double = ecdf(samples_double)

    _ = plt.plot(x_half, y_half)
    _ = plt.plot(x_double, y_double)
    _ = plt.legend(['theory', 'empirical', 'tau/2', 'tau*2'], loc='lower right')
    plt.show()

#how_often_do_we_get_no_hitters()
#do_the_data_follow_our_story()
how_is_this_parameter_optimal()


