import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from c41_working_with_multiple_series import load_multiple_time_series


def visualize_correlation_matrices(meat):
    # Get correlation matrix of the meat DataFrame: corr_meat
    corr_meat = meat.corr(method="spearman")

    # Customize the heatmap of the corr_meat correlation matrix
    sns.heatmap(corr_meat, annot=True,
                linewidths=0.4, annot_kws={"size": 10})

    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.show()


def clustered_heatmaps(meat):
    # Get correlation matrix of the meat DataFrame
    corr_meat = meat.corr(method="pearson")

    # Customize the heatmap of the corr_meat correlation matrix and rotate the x-axis labels
    fig = sns.clustermap(corr_meat,
                         row_cluster=True,
                         col_cluster=True,
                         figsize=(10, 10))

    plt.setp(fig.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
    plt.setp(fig.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    plt.show()


if __name__ == "__main__":
    sns.set()
    meat = load_multiple_time_series()
    visualize_correlation_matrices(meat)
    clustered_heatmaps(meat)
