# Import the dendrogram function
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pylab as plt
import seaborn as sns
from scipy.cluster.hierarchy import fcluster, linkage
from data import load_comic_con_data


def create_a_dendrogram(comic_con):

    distance_matrix = linkage(
        comic_con[['x_scaled', 'y_scaled']], method="ward", metric='euclidean')
    # Create a dendrogram
    dn = dendrogram(distance_matrix)
    # Display the dendogram
    plt.show()


sns.set()
comic_con = load_comic_con_data()
create_a_dendrogram(comic_con)
