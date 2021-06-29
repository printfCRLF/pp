import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_college_data


def building_a_facetgrid(df):
    # Create FacetGrid with Degree_Type and specify the order of the rows using row_order
    g2 = sns.FacetGrid(df, row="Degree_Type",
                       row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

    # Map a pointplot of SAT_AVG_ALL onto the grid
    g2.map(sns.pointplot, 'SAT_AVG_ALL')

    # Show the plot
    plt.show()
    plt.clf()


def using_a_factorplot(df):
    # Create a factor plot that contains boxplots of Tuition values
    sns.factorplot(data=df, x='Tuition', kind='box', row='Degree_Type')
    plt.show()
    plt.clf()

    # Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type
    sns.factorplot(data=df, x='SAT_AVG_ALL', kind='point', row='Degree_Type',
                   row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

    plt.show()
    plt.clf()


def using_a_lmplot(df):
    degree_ord = ['Graduate', 'Bachelors', 'Associates']
    # Create a FacetGrid varying by column and columns ordered with the degree_order variable
    g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)
    # Map a scatter plot of Undergrad Population compared to PCTPELL
    g.map(plt.scatter, 'UG', 'PCTPELL')
    plt.show()
    plt.clf()

    # Re-create the plot above as an lmplot
    sns.lmplot(data=df, x='UG', y='PCTPELL',
               col="Degree_Type", col_order=degree_ord)
    plt.show()
    plt.clf()

    inst_ord = ['Public', 'Private non-profit']
    # Create an lmplot that has a column for Ownership, a row for Degree_Type and hue based on the WOMENONLY column
    sns.lmplot(data=df, x='SAT_AVG_ALL', y='Tuition',
               col="Ownership", row='Degree_Type', row_order=['Graduate', 'Bachelors'],
               hue='WOMENONLY', col_order=inst_ord)

    plt.show()
    plt.clf()


college_data = load_college_data()
# building_a_facetgrid(college_data)
# using_a_factorplot(college_data)
using_a_lmplot(college_data)
