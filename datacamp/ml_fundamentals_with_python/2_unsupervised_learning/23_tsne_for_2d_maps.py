import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.hierarchy import fcluster
from sklearn.manifold import TSNE
from sklearn.preprocessing import Normalizer
import data


def tsne_visualization_of_grain_dataset(samples, variety_numbers):
    # Create a TSNE instance: model
    model = TSNE(learning_rate=200)

    # Apply fit_transform to samples: tsne_features
    tsne_features = model.fit_transform(samples)

    # Select the 0th feature: xs
    xs = tsne_features[:, 0]

    # Select the 1st feature: ys
    ys = tsne_features[:, 1]

    # Scatter plot, coloring by variety_numbers
    plt.scatter(xs, ys, c=variety_numbers)
    plt.show()


def tsne_of_stock_market(movements, companies): 
    normalized_movements = Normalizer().fit_transform(movements)

    # Create a TSNE instance: model
    model = TSNE(learning_rate=50)

    # Apply fit_transform to normalized_movements: tsne_features
    tsne_features = model.fit_transform(normalized_movements)

    # Select the 0th feature: xs
    xs = tsne_features[:,0]

    # Select the 1th feature: ys
    ys = tsne_features[:,1]

    # Scatter plot
    plt.scatter(xs, ys, alpha=0.5)

    # Annotate the points
    for x, y, company in zip(xs, ys, companies):
        plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
    plt.show()    


# samples, variety_numbers = data.load_grain_data_from_file()
# tsne_visualization_of_grain_dataset(samples, variety_numbers)
movements, companies = data.load_stock_movements_data()
tsne_of_stock_market(movements, companies)
