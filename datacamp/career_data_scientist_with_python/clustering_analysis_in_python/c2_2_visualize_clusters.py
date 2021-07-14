import matplotlib.pylab as plt
import seaborn as sns
from scipy.cluster.hierarchy import fcluster, linkage
from data import load_comic_con_data


def visualize_clusters_with_matplotlib(comic_con):
    # Define a colors dictionary for clusters
    colors = {1: 'red', 2: 'blue'}

    # Plot a scatter plot
    comic_con.plot.scatter(x="x_scaled", y="y_scaled",
                           c=comic_con['cluster_labels'].apply(lambda x: colors[x]))
    plt.show()


def visualize_clusters_with_seaborn(comic_con):
    # Plot a scatter plot using seaborn
    sns.scatterplot(x="x_scaled",
                    y="y_scaled",
                    hue="cluster_labels",
                    data=comic_con)
    plt.show()


sns.set()
comic_con = load_comic_con_data()
distance_matrix = linkage(
    comic_con[['x_scaled', 'y_scaled']], method="ward", metric='euclidean')
# Assign cluster labels
comic_con['cluster_labels'] = fcluster(
    distance_matrix, 2, criterion='maxclust')

visualize_clusters_with_matplotlib(comic_con)
visualize_clusters_with_seaborn(comic_con)
