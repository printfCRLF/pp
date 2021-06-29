import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_school_data


def strip_plot_and_swarm_plot(df):
    # Create the stripplot
    sns.stripplot(data=df, x='Award_Amount', y='Model Selected', jitter=True)
    plt.show()

    # Create and display a swarmplot with hue set to the Region
    sns.swarmplot(data=df, x='Award_Amount', y='Model Selected', hue='Region')
    plt.show()


def boxplot_violinplot_lvplot(df):
    # Create a boxplot
    sns.boxplot(data=df, x='Award_Amount', y='Model Selected')
    plt.show()
    plt.clf()

    # Create a violinplot with the husl palette
    sns.violinplot(data=df, x='Award_Amount',
                   y='Model Selected', palette='husl')
    plt.show()
    plt.clf()

    # Create a lvplot with the Paired palette and the Region column as the hue
    sns.lvplot(data=df, x='Award_Amount', y='Model Selected',
               palette='Paired', hue='Region')
    plt.show()
    plt.clf()


def barplots_pointplots_countplots(df):
    # Show a countplot with the number of models used with each region a different color
    sns.countplot(data=df, y="Model Selected", hue="Region")
    plt.show()
    plt.clf()

    # Create a pointplot and include the capsize in order to show caps on the error bars
    sns.pointplot(data=df, y='Award_Amount', x='Model Selected', capsize=.1)
    plt.show()
    plt.clf()

    # Create a barplot with each Region shown as a different color
    sns.barplot(data=df, y='Award_Amount', x='Model Selected', hue='Region')
    plt.show()
    plt.clf()


df = load_school_data()
# strip_plot_and_swarm_plot(df)
# boxplot_violinplot_lvplot(df)
barplots_pointplots_countplots(df)
