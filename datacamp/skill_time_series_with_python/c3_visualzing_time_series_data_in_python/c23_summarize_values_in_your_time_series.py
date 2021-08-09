import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def compute_numerical_summaries(co2_levels):
    # Print out summary statistics of the co2_levels DataFrame
    print(co2_levels.describe())
    # Print out the minima of the co2 column in the co2_levels DataFrame
    print(co2_levels["co2"].min())
    # Print out the maxima of the co2 column in the co2_levels DataFrame
    print(co2_levels["co2"].max())


def generate_boxplot(co2_levels):
    # Generate a boxplot
    ax = co2_levels.boxplot()

    # Set the labels and display the plot
    ax.set_xlabel('CO2', fontsize=10)
    ax.set_ylabel('Boxplot CO2 levels in Maui Hawaii', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()


def histograms(co2_levels):
    # Generate a histogram
    ax = co2_levels.plot(kind="hist", bins=50, fontsize=6)

    # Set the labels and display the plot
    ax.set_xlabel('CO2', fontsize=10)
    ax.set_ylabel('Histogram of CO2 levels in Maui Hawaii', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()


def density_plots(co2_levels):
    # Display density plot of CO2 levels values
    ax = co2_levels.plot(kind="density", linewidth=4, fontsize=6)
    # Annotate x-axis labels
    ax.set_xlabel('CO2', fontsize=10)
    # Annotate y-axis labels
    ax.set_ylabel('Density plot of CO2 levels in Maui Hawaii', fontsize=10)
    plt.show()


if __name__ == "__main__":
    sns.set()
    co2_levels = pd.read_csv("data/ch2_co2_levels.csv",
                             parse_dates=["datestamp"], index_col="datestamp")
    co2_levels.fillna(method="bfill", inplace=True)

    # compute_numerical_summaries(co2_levels)
    # generate_boxplot(co2_levels)
    # histograms(co2_levels)
    density_plots(co2_levels)
