import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_insurance_data


def building_a_pairgrid(df):
    # Create a PairGrid with a scatter plot for fatal_collisions and premiums
    g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
    g2 = g.map(plt.scatter)
    plt.show()

    # Create the same PairGrid but map a histogram on the diag
    g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
    g2 = g.map_diag(plt.hist)
    g3 = g2.map_offdiag(plt.scatter)

    plt.show()
    plt.clf()


def using_a_pairplot(df):
    # Create a pairwise plot of the variables using a scatter plot
    sns.pairplot(data=df, vars=["fatal_collisions",
                 "premiums"], kind='scatter')
    plt.show()

    # Plot the same data but use a different color palette and color code by Region
    sns.pairplot(data=df, vars=["fatal_collisions", "premiums"], kind='scatter',
                 hue='Region', palette='RdBu', diag_kws={'alpha': .5})
    plt.show()
    plt.clf()


def additional_pairplots(df):
    # Build a pairplot with different x and y variables
    sns.pairplot(data=df,
                 x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"],
                 y_vars=['premiums', 'insurance_losses'],
                 kind='scatter', hue='Region', palette='husl')
    plt.show()

    # plot relationships between insurance_losses and premiums
    sns.pairplot(data=df,
                 vars=["insurance_losses", "premiums"],
                 kind='reg', palette='BrBG', diag_kind='kde', hue='Region')
    plt.show()
    plt.clf()


df = load_insurance_data()
# building_a_pairgrid(df)
# using_a_pairplot(df)
additional_pairplots(df)
