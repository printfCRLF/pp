import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.cluster import KMeans
import data


def scaling_fishing_data():
    # Create scaler: scaler
    scaler = StandardScaler()
    # Create KMeans instance: kmeans
    kmeans = KMeans(n_clusters=4)
    # Create pipeline: pipeline
    pipeline = make_pipeline(scaler, kmeans)

    return pipeline


def clustering_fish_data(samples, species, pipeline):
    # Fit the pipeline to samples
    pipeline.fit(samples)
    # Calculate the cluster labels: labels
    labels = pipeline.predict(samples)
    # Create a DataFrame with labels and species as columns: df
    df = pd.DataFrame({'labels': labels, 'species': species})
    # Create crosstab: ct
    ct = pd.crosstab(df['labels'], df['species'])
    # Display ct
    print(ct)


def clustering_stock_data(movements, companies):
    normalizer = Normalizer()
    kmeans = KMeans(n_clusters=10)
    pipeline = make_pipeline(normalizer, kmeans)
    pipeline.fit(movements)
    labels = pipeline.predict(movements)
    df = pd.DataFrame({'labels': labels, 'companies': companies})
    print(df.sort_values('labels'))


samples, species = data.load_fish_data()
pipeline = scaling_fishing_data()
clustering_fish_data(samples, species, pipeline)
clustering_stock_data(*data.load_stock_movements_data())
