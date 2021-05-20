import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from util import ecdf 

sns.set()

def generating_random_numbers_using_np_random():
    np.random.seed(42)
    random_numbers = np.empty(100000)

    for i in range(100000): 
        random_numbers[i] = np.random.random()
    
    _ = plt.hist(random_numbers)
    plt.show()

def perform_bernoulli_trials(n, p): 
    """Perform n Bernoulli trials with success probability p 
    and return number of successes."""
    n_success = 0
    for i in range(n): 
        random_number = np.random.random()
        if random_number < p:
            n_success += 1
    
    return n_success

def how_many_defaults(): 
    np.random.seed()
    n_defaults = np.empty(1000)
    for i in range(1000): 
        n_defaults[i] = perform_bernoulli_trials(100, 0.05)
    
    _ = plt.hist(n_defaults, density=True)
    _ = plt.xlabel('number of defaults out of 100 loans')
    _ = plt.ylabel('probability')
    plt.show()

def will_the_bank_fail(): 
    np.random.seed()
    n_defaults = np.empty(1000)
    for i in range(1000): 
        n_defaults[i] = perform_bernoulli_trials(100, 0.05)

    x, y = ecdf(n_defaults)

    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('number of defaults')
    _ = plt.ylabel('ECDF')
    plt.show()

    n_lose_money = np.sum(n_defaults >= 10)
    print('Number of 100-loan simulations with 10 or more defaults', n_lose_money)
    print('Probability of losing money =', n_lose_money / len(n_defaults))

def sampling_out_of_binomial_distribution(): 
    n_defaults = np.random.binomial(100, 0.05, size=10000)
    x, y = ecdf(n_defaults)

    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel('number of defaults out of 100 loans')
    _ = plt.ylabel('CDF')
    plt.show()

def plotting_the_binomial_pmf(): 
    n_defaults = np.random.binomial(100, 0.05, size=10000)
    bins = np.arange(0, max(n_defaults) + 1.5) - 0.5
    _ = plt.hist(n_defaults, density=True, bins=bins)

    _ = plt.xlabel('number of defaults out of 100 loans')
    _ = plt.ylabel('probability')
    plt.show()

def relationship_between_binomial_and_poisson_distribution(): 
    samples_poisson = np.random.poisson(10, size=10000)
    print('Poisson:     ', np.mean(samples_poisson), np.std(samples_poisson))

    n = [20, 100, 1000]
    p = [0.5, 0.1, 0.01]

    for i in range(3): 
        samples_binomial = np.random.binomial(n[i], p[i], size=10000)
        mean = np.mean(samples_binomial)
        std = np.std(samples_binomial)
        print(f'n = {i} Binomial: {mean} {std}')

def relationship_between_binomial_and_poisson_distribution2(): 
    samples_poisson = np.random.poisson(2.5, size=10000)
    print('Poisson:     ', np.mean(samples_poisson), np.std(samples_poisson))

    # poisson distribution can approximate binomial distribution if n > 20 and p <= 0.05
    n = [5, 10, 20, 100]
    p = [0.5, 0.25, 0.125, 0.025]

    for i in range(4): 
        samples_binomial = np.random.binomial(n[i], p[i], size=10000)
        mean = np.mean(samples_binomial)
        std = np.std(samples_binomial)
        print(f'n = {i} Binomial: {mean} {std}')


def was_2015_anomalous(): 
    n_nohitters = np.random.poisson(251/115, size=10000)
    n_large = np.sum(n_nohitters >= 7)
    p_large = n_large / 10000
    print('Probability of seven or more no-hitters:', p_large)


#generating_random_numbers_using_np_random()
#how_many_defaults()
#will_the_bank_fail()
#sampling_out_of_binomial_distribution()
plotting_the_binomial_pmf()
#relationship_between_binomial_and_poisson_distribution()
#relationship_between_binomial_and_poisson_distribution2()
#was_2015_anomalous()
