import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf


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


sns.set()
# generating_random_numbers_using_np_random()
# how_many_defaults()
will_the_bank_fail()
