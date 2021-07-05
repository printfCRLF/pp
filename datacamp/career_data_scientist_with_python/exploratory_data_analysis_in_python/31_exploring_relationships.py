import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from empiricaldist import Pmf, Cdf
from data import load_brfss_data


def pmf_of_age(brfss):
    # Extract age
    age = brfss["AGE"]

    # Plot the PMF
    pmf_age = Pmf.from_seq(age)
    pmf_age.bar()

    # Label the axes
    plt.xlabel('Age in years')
    plt.ylabel('PMF')
    plt.show()


def scatter_plot(brfss):
    # Select the first 1000 respondents
    brfss = brfss[:1000]

    # Extract age and weight
    age = brfss['AGE']
    weight = brfss['WTKG3']

    # Make a scatter plot
    plt.plot(age, weight, 'o', alpha=0.1)

    plt.xlabel('Age in years')
    plt.ylabel('Weight in kg')

    plt.show()


def jittering(brfss):
    # Select the first 1000 respondents
    brfss = brfss[:1000]

    # Add jittering to age
    age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
    # Extract weight
    weight = brfss['WTKG3']

    # Make a scatter plot
    plt.plot(age, weight, 'o', markersize=1, alpha=0.2)

    plt.xlabel('Age in years')
    plt.ylabel('Weight in kg')
    plt.show()


sns.set()
brfss = load_brfss_data()
pmf_of_age(brfss)
scatter_plot(brfss)
jittering(brfss)
