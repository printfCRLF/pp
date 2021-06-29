import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_bike_share_data


def build_a_joint_grid(df):
    # Build a JointGrid comparing humidity and total_rentals
    sns.set_style("whitegrid")
    g = sns.JointGrid(x="hum", y="total_rentals",
                      data=df, xlim=(0.1, 1.0))

    g.plot(sns.regplot, sns.distplot)
    plt.show()

    # Create a jointplot similar to the JointGrid
    sns.jointplot(x="hum", y="total_rentals",
                  kind='reg', data=df)

    plt.show()
    plt.clf()


def joint_plot_and_regression(df):
    # Plot temp vs. total_rentals as a regression plot
    sns.jointplot(x="temp", y="total_rentals", data=df,
                  kind='reg', order=2, xlim=(0, 1))
    plt.show()

    # Plot a jointplot showing the residuals
    sns.jointplot(x="temp", y="total_rentals", data=df,
                  kind='resid', order=2)
    plt.show()
    plt.clf()


def complex_jointplot(df):
    # Create a jointplot of temp vs. casual riders
    # Include a kdeplot over the scatter plot
    g = (sns.jointplot(x="temp", y="casual", data=df,
                       kind='scatter', marginal_kws=dict(bins=10, rug=True))
         .plot_joint(sns.kdeplot))
    plt.show()

    # Replicate the above plot but only for registered riders
    g = (sns.jointplot(x="temp", y="registered", data=df,
                       kind='scatter', marginal_kws=dict(bins=10, rug=True))
         .plot_joint(sns.kdeplot))
    plt.show()
    plt.clf()


bike_share_data = load_bike_share_data()
# build_a_joint_grid(bike_share_data)
# joint_plot_and_regression(bike_share_data)
complex_jointplot(bike_share_data)
