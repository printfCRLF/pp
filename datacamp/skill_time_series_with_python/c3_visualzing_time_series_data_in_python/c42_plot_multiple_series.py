import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics import tsaplots
from c41_working_with_multiple_series import load_multiple_time_series


def add_summary_statistics_to_your_time_series_plot(meat):
    # Plot the meat data
    ax = meat.plot(fontsize=6, linewidth=1)
    # Add x-axis labels
    ax.set_xlabel('Date', fontsize=6)
    mean_series = meat.describe().loc["mean"]
    meat_mean = mean_series.to_frame().transpose()

    # Add summary table information to the plot
    ax.table(cellText=meat_mean.values,
             colWidths=[0.15]*len(meat_mean.columns),
             rowLabels=meat_mean.index,
             colLabels=meat_mean.columns,
             loc='top', fontsize=16)

    # Specify the fontsize and location of your legend
    ax.legend(loc='upper center', bbox_to_anchor=(
        0.5, 0.95), ncol=3, fontsize=6)

    # Show plot
    plt.show()


def plot_your_time_series_on_individual_plots(meat):
    # Create a facetted graph with 2 rows and 4 columns
    meat.plot(subplots=True,
              layout=(2, 4),
              sharex=False,
              sharey=False,
              colormap='viridis',
              fontsize=2,
              legend=False,
              linewidth=0.2)

    plt.show()


if __name__ == "__main__":
    sns.set()
    meat = load_multiple_time_series()
    add_summary_statistics_to_your_time_series_plot(meat)
    plot_your_time_series_on_individual_plots(meat)
