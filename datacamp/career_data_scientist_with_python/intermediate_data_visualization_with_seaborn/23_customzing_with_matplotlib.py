import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_fy18_4050_data


def using_matplotliba_axes(df):
    # Create a figure and axes
    fig, ax = plt.subplots()
    # Plot the distribution of data
    sns.distplot(df['fmr_3'], ax=ax)
    # Create a more descriptive x axis label
    ax.set(xlabel="3 Bedroom Fair Market Rent")
    plt.show()


def limit_on_xaxes(df):
    # Create a figure and axes
    fig, ax = plt.subplots()

    # Plot the distribution of 1 bedroom rents
    sns.distplot(df['fmr_1'], ax=ax)

    # Modify the properties of the plot
    ax.set(xlabel="1 Bedroom Fair Market Rent",
           xlim=(100, 1500),
           title="US Rent")
    plt.show()


def vertical_lines(df):
    # Create a figure and axes. Then plot the data
    fig, ax = plt.subplots()
    sns.distplot(df['fmr_1'], ax=ax)

    # Customize the labels and limits
    ax.set(xlabel="1 Bedroom Fair Market Rent",
           xlim=(100, 1500), title="US Rent")

    # Add vertical lines for the median and mean
    median = df['fmr_1'].median()
    mean = df['fmr_1'].mean()
    ax.axvline(x=median, color='m', label='Median',
               linestyle='--', linewidth=2)
    ax.axvline(x=mean, color='b', label='Mean', linestyle='-', linewidth=2)

    # Show the legend and plot the data
    ax.legend()
    plt.show()


def multiple_plots(df):
    # Create a plot with 1 row and 2 columns that share the y axis label
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

    # Plot the distribution of 1 bedroom apartments on ax0
    sns.distplot(df['fmr_1'], ax=ax0)
    ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500))

    # Plot the distribution of 2 bedroom apartments on ax1
    sns.distplot(df['fmr_2'], ax=ax1)
    ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100, 1500))

    # Display the plot
    plt.show()


housing_data = load_fy18_4050_data()
# using_matplotliba_axes(housing_data)
# limit_on_xaxes(housing_data)
# vertical_lines(housing_data)
multiple_plots(housing_data)
