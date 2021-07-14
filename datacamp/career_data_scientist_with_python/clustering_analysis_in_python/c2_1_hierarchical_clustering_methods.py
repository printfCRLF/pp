import matplotlib.pylab as plt
import seaborn as sns
from scipy.cluster.hierarchy import fcluster, linkage
from data import load_comic_con_data


def ward_method(comic_con):
    # Use the linkage() function
    distance_matrix = linkage(
        comic_con[['x_scaled', 'y_scaled']], method="ward", metric='euclidean')
    # Assign cluster labels
    comic_con['cluster_labels'] = fcluster(
        distance_matrix, 2, criterion='maxclust')
    # Plot clusters
    sns.scatterplot(x='x_scaled', y='y_scaled',
                    hue='cluster_labels', data=comic_con)
    plt.show()


def single_method(comic_con):
    # Use the linkage() function
    distance_matrix = linkage(
        comic_con[['x_scaled', 'y_scaled']], method="single", metric='euclidean')
    # Assign cluster labels
    comic_con['cluster_labels'] = fcluster(
        distance_matrix, 2, criterion='maxclust')
    # Plot clusters
    sns.scatterplot(x='x_scaled', y='y_scaled',
                    hue='cluster_labels', data=comic_con)
    plt.show()


def complete_method(comic_con):
    # Use the linkage() function
    distance_matrix = linkage(
        comic_con[['x_scaled', 'y_scaled']], method="complete", metric='euclidean')
    # Assign cluster labels
    comic_con['cluster_labels'] = fcluster(
        distance_matrix, 2, criterion='maxclust')
    # Plot clusters
    sns.scatterplot(x='x_scaled', y='y_scaled',
                    hue='cluster_labels', data=comic_con)
    plt.show()


sns.set()
comic_con = load_comic_con_data()
ward_method(comic_con)
single_method(comic_con)
complete_method(comic_con)
