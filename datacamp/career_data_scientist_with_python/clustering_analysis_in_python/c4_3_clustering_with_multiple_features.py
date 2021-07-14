import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans, vq, whiten
from data import load_fifa_18_sample_data


def what_makes_a_complete_player(fifa):
    features = ['pac', 'sho', 'pas', 'dri', 'def', 'phy']
    scaled_features = ['scaled_pac', 'scaled_sho',
                       'scaled_pas', 'scaled_dri', 'scaled_def', 'scaled_phy']

    for i in range(len(features)):
        fifa[scaled_features[i]] = whiten(fifa[features[i]])

    # Create centroids with kmeans for 2 clusters
    cluster_centers, _ = kmeans(fifa[scaled_features], 2)

    # Assign cluster labels and print cluster centers
    fifa['cluster_labels'], _ = vq(fifa[scaled_features], cluster_centers)
    print(fifa.groupby('cluster_labels')[scaled_features].mean())

    # Plot cluster centers to visualize clusters
    fifa.groupby('cluster_labels')[scaled_features].mean().plot(
        legend=True, kind='bar')
    plt.show()

    # Get the name column of first 5 players in each cluster
    for cluster in fifa['cluster_labels'].unique():
        print(cluster, fifa[fifa['cluster_labels']
              == cluster]["name"].values[:5])


sns.set()
fifa = load_fifa_18_sample_data()
what_makes_a_complete_player(fifa)
