import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import normalize
import data




def hierarchical_clustering(samples, varieties):
    # Calculate the linkage: mergings
    mergings = linkage(samples, method='complete')

    # Plot the dendrogram, using varieties as labels
    dendrogram(mergings,
               labels=varieties,
               leaf_rotation=90,
               leaf_font_size=6,
               )
    plt.show()


def hierarchies_of_stocks(movements, companies):
    # Normalize the movements: normalized_movements
    normalized_movements = normalize(movements)

    # Calculate the linkage: mergings
    mergings = linkage(normalized_movements, method='complete')

    # Plot the dendrogram
    dendrogram(mergings, labels=companies, leaf_rotation=90, leaf_font_size=6)
    plt.show()


hierarchical_clustering(*data.load_seed_data())
hierarchies_of_stocks(*data.load_stock_movements_data())
