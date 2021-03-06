import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.hierarchy import fcluster
import data


def single_linkage(samples, country_names):
    # Calculate the linkage: mergings
    mergings = linkage(samples, method='single')

    # Plot the dendrogram
    dendrogram(mergings,
               labels=country_names,
               leaf_rotation=90,
               leaf_font_size=6)
    plt.show()


def extracting_cluster_labels(samples, varieties):
    mergings = linkage(samples, method='complete')
    # Use fcluster to extract labels: labels
    labels = fcluster(mergings, 6, criterion='distance')

    # Create a DataFrame with labels and varieties as columns: df
    df = pd.DataFrame({'labels': labels, 'varieties': varieties})

    # Create crosstab: ct
    ct = pd.crosstab(df['labels'], df['varieties'])

    # Display ct
    print(ct)


single_linkage(*data.load_eurovision_data())
extracting_cluster_labels(*data.load_seed_data())
