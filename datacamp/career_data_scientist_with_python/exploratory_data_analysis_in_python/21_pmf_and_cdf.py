import matplotlib.pyplot as plt
import seaborn as sns
from empiricaldist import Pmf, Cdf
from data import load_gss_data


def make_a_pmf(gss):
    # Select the age column
    age = gss['age'].values

    # Make a PMF of age
    pmf_age = Pmf.from_seq(age)

    # Plot the PMF
    pmf_age.bar()

    # Label the axes
    plt.xlabel('Age')
    plt.ylabel('PMF')
    plt.show()


def make_a_cdf(gss):
    # Select the age column
    age = gss['age'].values

    # Compute the CDF of age
    cdf_age = Cdf.from_seq(age)

    # Calculate the CDF of 30
    print(cdf_age[30.0])


def compute_iqr(gss):
    income = gss["realinc"].values
    cdf_income = Cdf.from_seq(income)

    # Calculate the 75th percentile
    percentile_75th = cdf_income.inverse(0.75)

    # Calculate the 25th percentile
    percentile_25th = cdf_income.inverse(0.25)

    # Calculate the interquartile range
    iqr = percentile_75th - percentile_25th

    # Print the interquartile range
    print(iqr)


def plot_a_cdf(gss):
    # Select realinc
    income = gss["realinc"].values

    # Make the CDF
    cdf_income = Cdf.from_seq(income)

    # Plot it
    cdf_income.plot()

    # Label the axes
    plt.xlabel('Income (1986 USD)')
    plt.ylabel('CDF')
    plt.show()


sns.set()
gss = load_gss_data()
# make_a_pmf(gss)
# make_a_cdf(gss)
# compute_iqr(gss)
plot_a_cdf(gss)
