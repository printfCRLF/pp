from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
import pandas as pd
import data

# https://www.lateral.io/resources-blog/the-unknown-perils-of-mining-wikipedia
articles, titles = data.load_wikipedia_articles_and_titles()

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)
# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)
# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)


# Fit the pipeline to articles
pipeline.fit(articles)
# Calculate the cluster labels: labels
labels = pipeline.predict(articles)
# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})
# Display df sorted by cluster label
print(df.sort_values(by='label'))
