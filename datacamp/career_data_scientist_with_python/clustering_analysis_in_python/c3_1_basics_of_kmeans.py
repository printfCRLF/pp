import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans, vq
from data import load_comic_con_data


def kmeans_first_exercies(comic_con):
    # Generate cluster centers
    cluster_centers, distortion = kmeans(
        comic_con[["x_scaled", "y_scaled"]], 2)

    # Assign cluster labels
    comic_con['cluster_labels'], distortion_list = vq(
        comic_con[["x_scaled", "y_scaled"]], cluster_centers)

    # Plot clusters
    sns.scatterplot(x='x_scaled', y='y_scaled',
                    hue='cluster_labels', data=comic_con)
    plt.show()


def elbow_method_on_distinct_clusters(comic_con):
    distortions = []
    num_clusters = range(1, 7)

    # Create a list of distortions from the kmeans function
    for i in num_clusters:
        cluster_centers, distortion = kmeans(
            comic_con[["x_scaled", "y_scaled"]], i)
        distortions.append(distortion)

    # Create a data frame with two lists - num_clusters, distortions
    elbow_plot = pd.DataFrame(
        {'num_clusters': num_clusters, 'distortions': distortions})

    # Creat a line plot of num_clusters and distortions
    sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
    plt.xticks(num_clusters)
    plt.show()


def elbow_method_on_uniform_data():
    scaled_x = np.array([2.37619911, 2.55898365, 3.53383457, 2.61991184, 0.79206637,
                         1.94970183, 3.65569093, 0.79206637, 1.58413274, 1.64506092,
                         1.76691728, 3.10733729, 0.85299455, 3.04640911, 3.7775473,
                         3.59476275, 3.04640911, 3.7775473, 3.96033185, 1.0357791,
                         1.52320456, 2.7417682, 3.35105002, 2.92455275, 2.55898365,
                         3.53383457, 4.14311639, 3.53383457, 2.25434274, 3.35105002])

    scaled_y = np.array([1.15223748, 2.68855411, 1.15223748, 1.15223748, 2.30447496,
                         1.9203958, 1.15223748, 1.53631664, 0., 3.45671243,
                         2.30447496, 1.15223748, 0., 2.68855411, 1.53631664,
                         0.38407916, 1.15223748, 0., 0.76815832, 1.9203958,
                         3.45671243, 1.9203958, 3.07263327, 2.30447496, 1.15223748,
                         0.38407916, 1.53631664, 0.76815832, 3.07263327, 2.68855411])
    uniform_data = pd.DataFrame({"scaled_x": scaled_x, "scaled_y": scaled_y})

    distortions = []
    num_clusters = range(2, 7)

    # Create a list of distortions from the kmeans function
    for i in num_clusters:
        cluster_centers, distortion = kmeans(uniform_data, i)
        distortions.append(distortion)

    # Create a data frame with two lists - num_clusters, distortions
    elbow_plot = pd.DataFrame(
        {'num_clusters': num_clusters, 'distortions': distortions})

    # Creat a line plot of num_clusters and distortions
    sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
    plt.xticks(num_clusters)
    plt.show()


sns.set()
# comic_con = load_comic_con_data()
# kmeans_first_exercies(comic_con)
# elbow_method_on_distinct_clusters(comic_con)
elbow_method_on_uniform_data()
