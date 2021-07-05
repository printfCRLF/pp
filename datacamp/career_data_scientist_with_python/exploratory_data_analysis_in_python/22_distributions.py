import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from empiricaldist import Pmf, Cdf
from data import load_gss_data


def extract_education_levels(gss):
    # Select educ
    educ = gss['educ']

    # Bachelor's degree
    bach = (educ >= 16)

    # Associate degree
    assc = (educ >= 14) & (educ < 16)

    # High school (12 or fewer years of education)
    high = educ <= 12
    print(high.mean())

    return high, assc, bach


def plot_income_cdfs(gss, high, assc, bach):
    income = gss['realinc']

    # Plot the CDFs
    Cdf.from_seq(income[high]).plot(label='High school')
    Cdf.from_seq(income[assc]).plot(label='Associate')
    Cdf.from_seq(income[bach]).plot(label='Bachelor')

    # Label the axes
    plt.xlabel('Income (1986 USD)')
    plt.ylabel('CDF')
    plt.legend()
    plt.show()


def distribution_of_income(gss):
    # Extract realinc and compute its log
    income = gss['realinc']
    log_income = np.log10(income)

    # Compute mean and standard deviation
    mean = log_income.mean()
    std = log_income.std()
    print(mean, std)

    # Make a norm object
    from scipy.stats import norm
    dist = norm(mean, std)

    return log_income, dist


def comparing_cdfs(log_income, dist):
    # Evaluate the model CDF
    xs = np.linspace(2, 5.5)
    ys = dist.cdf(xs)

    # Plot the model CDF
    plt.clf()
    plt.plot(xs, ys, color='gray')

    # Create and plot the Cdf of log_income
    Cdf.from_seq(log_income).plot()

    # Label the axes
    plt.xlabel('log10 of realinc')
    plt.ylabel('CDF')
    plt.show()


def comparing_pdfs(log_income, dist):
    # Evaluate the normal PDF
    xs = np.linspace(2, 5.5)
    ys = dist.pdf(xs)

    # Plot the model PDF
    plt.clf()
    plt.plot(xs, ys, color='gray')

    # Plot the data KDE
    sns.kdeplot(log_income)

    # Label the axes
    plt.xlabel('log10 of realinc')
    plt.ylabel('PDF')
    plt.show()


sns.set()
gss = load_gss_data()
# high, assc, bach = extract_education_levels(gss)
# plot_income_cdfs(gss, high, assc, bach)
log_income, dist = distribution_of_income(gss)
comparing_cdfs(log_income, dist)
comparing_pdfs(log_income, dist)
