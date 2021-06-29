import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_fy18_4050_data


def setting_default_style(df):
    # Plot the pandas histogram
    df['fmr_2'].plot.hist()
    plt.show()
    plt.clf()

    # Set the default seaborn style
    sns.set()
    # Plot the pandas histogram again
    df['fmr_2'].plot.hist()
    plt.show()
    plt.clf()


def comparing_styles(df):
    sns.set_style("dark")
    sns.distplot(df["fmr_2"])
    plt.show()
    plt.clf()

    sns.set_style("whitegrid")
    sns.distplot(df["fmr_2"])
    plt.show()
    plt.clf()


def removing_spines(df):
    # Set the style to white
    sns.set_style('white')

    # Create a regression plot
    sns.lmplot(data=df,
               x='pop2010',
               y='fmr_2')

    # Remove the spines
    sns.despine(left=True)

    # Show the plot and clear the figure
    plt.show()
    plt.clf()


housing_data = load_fy18_4050_data()
# setting_default_style(housing_data)
# comparing_styles(housing_data)
removing_spines(housing_data)
