from sklearn.decomposition import TruncatedSVD, NMF
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import normalize, MaxAbsScaler, Normalizer
import pandas as pd
import data


def which_articles_are_similar_to_cristiano_ronaldo(articles, titles):
    model = NMF(n_components=6)
    # Fit the model to articles
    model.fit(articles)
    # Transform the articles: nmf_features
    nmf_features = model.transform(articles)

    # Normalize the NMF features: norm_features
    norm_features = normalize(nmf_features)
    # Create a DataFrame: df
    df = pd.DataFrame(norm_features, index=titles)
    # Select the row corresponding to 'Cristiano Ronaldo': article
    article = df.loc['Cristiano Ronaldo']
    # Compute the dot products: similarities
    similarities = df.dot(article)
    # Display those with the largest cosine similarity
    print(similarities.nlargest())


def recommend_musical_artists(artists, artist_names):
    # Create a MaxAbsScaler: scaler
    scaler = MaxAbsScaler()
    # Create an NMF model: nmf
    nmf = NMF(n_components=20)
    # Create a Normalizer: normalizer
    normalizer = Normalizer()
    # Create a pipeline: pipeline
    pipeline = make_pipeline(scaler, nmf, normalizer)
    # Apply fit_transform to artists: norm_features
    norm_features = pipeline.fit_transform(artists)

    # Create a DataFrame: df
    df = pd.DataFrame(norm_features, index=artist_names)
    # Select row of 'Bruce Springsteen': artist
    artist = df.loc['Bruce Springsteen']
    # Compute cosine similarities: similarities
    similarities = df.dot(artist)
    # Display those with highest cosine similarity
    print(similarities.nlargest())


# articles, titles = data.load_wikipedia_articles_and_titles()
# which_articles_are_similar_to_cristiano_ronaldo(articles, titles)

artists, artist_names = data.load_musical_artists()
recommend_musical_artists(artists, artist_names)
