from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.cluster.vq import kmeans, vq
import seaborn as sns
import pandas as pd
import numpy as np


def visualization(x, y):
    # Create a scatter plot
    plt.scatter(x, y)

    # Display the scatter plot
    plt.show()


def hierarchical_clustering(df):
    # Use the linkage() function to compute distance
    Z = linkage(df, 'ward')
    # Generate cluster labels
    df['cluster_labels'] = fcluster(Z, 2, criterion='maxclust')
    # Plot the points with seaborn
    sns.scatterplot(x="x", y="y", hue="cluster_labels", data=df)
    plt.show()


def kmeans_clustering(df):
    # Compute cluster centers
    centroids, _ = kmeans(df, 2)
    # Assign cluster labels
    df['cluster_labels'], _ = vq(df, centroids)
    # Plot the points with seaborn
    sns.scatterplot(x="x", y="y", hue="cluster_labels", data=df)
    plt.show()


sns.set()
x = np.array([9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25,
             23, 21, 23, 23, 20, 30, 23], dtype=float)
y = np.array([8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25,
             30, 29, 29, 30, 25, 27, 26, 30], dtype=float)
df = pd.DataFrame({"x": x, "y": y})
visualization(x, y)
hierarchical_clustering(df)
kmeans_clustering(df)
