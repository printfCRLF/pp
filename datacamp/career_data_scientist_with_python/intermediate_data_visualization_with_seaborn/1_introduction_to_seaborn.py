import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_school_data, load_insurance_data


def compare_a_histogram_and_distplot(df):
    # Display pandas histogram
    df['Award_Amount'].plot.hist()
    plt.show()
    plt.clf()

    # Display a Seaborn distplot
    sns.distplot(df['Award_Amount'])
    plt.show()
    plt.clf()


def rug_plot_and_kde_shading(df):
    # Create a distplot of the Award Amount
    sns.distplot(df['Award_Amount'],
                 hist=False, rug=True, kde_kws={'shade': True})
    plt.show()


def creat_regression_plots(df):
    # Create a regression plot of premiums vs. insurance_losses
    sns.regplot(x="insurance_losses", y="premiums",  data=df)
    plt.show()

    # Create an lmplot of premiums vs. insurance_losses
    sns.lmplot(x="insurance_losses", y="premiums", data=df)
    plt.show()


def plotting_multiple_variables_using_hue(df):
    # Create a regression plot using hue
    sns.lmplot(data=df, x="insurance_losses", y="premiums",
               hue="Region")
    plt.show()


def facetting_multiple_variables_with_rows_and_cols(df):
    # Create a regression plot with multiple rows
    sns.lmplot(data=df, x="insurance_losses", y="premiums",
               row="Region")
    plt.show()


school_data = load_school_data()
# compare_a_histogram_and_distplot(school_data)
# rug_plot_and_kde_shading(school_data)

insurance_data = load_insurance_data()
# creat_regression_plots(insurance_data)
plotting_multiple_variables_using_hue(insurance_data)
facetting_multiple_variables_with_rows_and_cols(insurance_data)
