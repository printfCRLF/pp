import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf


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

# No-hitter is a rare event in the game of baseball. There has been only 251 no-hitter games
# through 1901 to 2015 over 200,000 games.


def was_2015_anomalous():
    # There are, on average 255/115 no-hitter games per season
    n_nohitters = np.random.poisson(251/115, size=10000)
    n_large = np.sum(n_nohitters >= 7)
    p_large = n_large / 10000
    print('Probability of seven or more no-hitters:', p_large)


# relationship_between_binomial_and_poisson_distribution()
# relationship_between_binomial_and_poisson_distribution2()
was_2015_anomalous()
