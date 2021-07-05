import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from empiricaldist import Pmf, Cdf
from data import load_brfss_data


def height_and_weight(brfss):
    # Drop rows with missing data
    data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

    # Make a box plot
    sns.boxplot(x="_HTMG10", y="WTKG3", data=data, whis=10)

    # Plot the y-axis on a log scale
    plt.yscale("log")

    # Remove unneeded lines and label axes
    sns.despine(left=True, bottom=True)
    plt.xlabel('Height in cm')
    plt.ylabel('Weight in kg')
    plt.show()


def distribution_of_income(brfss):
    # Extract income
    income = brfss["INCOME2"]

    # Plot the PMF
    Pmf.from_seq(income).bar()

    # Label the axes
    plt.xlabel('Income level')
    plt.ylabel('PMF')
    plt.show()


def income_and_height(brfss):
    # Drop rows with missing data
    data = brfss.dropna(subset=['INCOME2', 'HTM4'])

    # Make a violin plot
    sns.violinplot(x="INCOME2", y="HTM4", data=data, inner=None)

    # Remove unneeded lines and label axes
    sns.despine(left=True, bottom=True)
    plt.xlabel('Income level')
    plt.ylabel('Height in cm')
    plt.show()


brfss = load_brfss_data()
# height_and_weight(brfss)
# distribution_of_income(brfss)
income_and_height(brfss)
