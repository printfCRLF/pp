import matplotlib.pylab as plt
import seaborn as sns
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.cluster.vq import whiten
from data import load_fifa_18_sample_data


def exploring_defenders(fifa):
    fifa["scaled_sliding_tackle"] = whiten(fifa["sliding_tackle"])
    fifa["scaled_aggression"] = whiten(fifa["aggression"])

    # Fit the data into a hierarchical clustering algorithm
    distance_matrix = linkage(
        fifa[['scaled_sliding_tackle', 'scaled_aggression']], 'ward')

    # Assign cluster labels to each row of data
    fifa['cluster_labels'] = fcluster(distance_matrix, 3, criterion='maxclust')

    # Display cluster centers of each cluster
    print(fifa[['scaled_sliding_tackle', 'scaled_aggression',
          'cluster_labels']].groupby('cluster_labels').mean())

    # Create a scatter plot through seaborn
    sns.scatterplot(x="scaled_sliding_tackle",
                    y="scaled_aggression", hue="cluster_labels", data=fifa)
    plt.show()


sns.set()
fifa = load_fifa_18_sample_data()
exploring_defenders(fifa)
