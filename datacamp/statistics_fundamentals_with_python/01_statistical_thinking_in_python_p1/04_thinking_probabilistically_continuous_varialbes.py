import numpy as np
import matplotlib.pyplot as plt 
from util import ecdf

samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

belmont_no_outliers = [148.51, 146.65, 148.52, 150.7 , 150.42, 150.88, 151.57, 147.54,
       149.65, 148.74, 147.86, 148.75, 147.5 , 148.26, 149.71, 146.56,
       151.19, 147.88, 149.16, 148.82, 148.96, 152.02, 146.82, 149.97,
       146.13, 148.1 , 147.2 , 146.  , 146.4 , 148.2 , 149.8 , 147.  ,
       147.2 , 147.8 , 148.2 , 149.  , 149.8 , 148.6 , 146.8 , 149.6 ,
       149.  , 148.2 , 149.2 , 148.  , 150.4 , 148.8 , 147.2 , 148.8 ,
       149.6 , 148.4 , 148.4 , 150.2 , 148.8 , 149.2 , 149.2 , 148.4 ,
       150.2 , 146.6 , 149.8 , 149.  , 150.8 , 148.6 , 150.2 , 149.  ,
       148.6 , 150.2 , 148.2 , 149.4 , 150.8 , 150.2 , 152.2 , 148.2 ,
       149.2 , 151.  , 149.6 , 149.6 , 149.4 , 148.6 , 150.  , 150.6 ,
       149.2 , 152.6 , 152.8 , 149.6 , 151.6 , 152.8 , 153.2 , 152.4 ,
       152.2 ];

def the_normal_pdf(): 
    _ = plt.hist(samples_std1, density=True, histtype='step', bins=100)
    _ = plt.hist(samples_std3, density=True, histtype='step', bins=100)
    _ = plt.hist(samples_std10, density=True, histtype='step', bins=100)

    _ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
    plt.ylim(-0.01, 0.42)
    plt.show()

def the_normal_cdf(): 
    x_std1, y_std1 = ecdf(samples_std1)
    x_std3, y_std3 = ecdf(samples_std3)
    x_std10, y_std10 = ecdf(samples_std10)

    _ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
    _ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')
    _ = plt.plot(x_std10, y_std10, marker='.', linestyle='none')

    _ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
    plt.show()

def are_belmont_stakes_normally_distributed(): 
    mu = np.mean(belmont_no_outliers)
    sigma = np.std(belmont_no_outliers)
    samples = np.random.normal(mu, sigma, size=10000)

    x_theor, y_theor = ecdf(samples)
    x, y = ecdf(belmont_no_outliers)

    _ = plt.plot(x_theor, y_theor)
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('Belmont winning time (sec.)')
    _ = plt.ylabel('CDF')
    plt.show()

def chances_are_faster_than_secretariat(): 
    mu = np.mean(belmont_no_outliers)
    sigma = np.std(belmont_no_outliers)
    samples = np.random.normal(mu, sigma, 1000000)
    prob = len(samples[samples < 144]) / len(samples)
    print('Probability of besting Secretariat:', prob)

def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    t1 = np.random.exponential(tau1, size)
    t2 = np.random.exponential(tau2, size)
    return t1 + t2

def distribution_of_no_hitters_and_cycles(): 
    waiting_times = successive_poisson(764, 715, 100000)

    _ = plt.hist(waiting_times, bins=100, density=True, histtype='step')
    _ = plt.xlabel('waiting time')
    _ = plt.ylabel('probability')
    plt.show()

    x, y = ecdf(waiting_times)
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('waiting time')
    _ = plt.ylabel('CDF')
    plt.show()


#the_normal_pdf()
the_normal_cdf()
#are_belmont_stakes_normally_distributed()
#chances_are_faster_than_secretariat()
#distribution_of_no_hitters_and_cycles()
