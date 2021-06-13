from sklearn.decomposition import NMF
import pandas as pd
import data


def nmf_applied_to_wikipedia_articles(articles):
    # Create an NMF instance: model
    model = NMF(n_components=6)
    # Fit the model to articles
    model.fit(articles)
    # Transform the articles: nmf_features
    nmf_features = model.transform(articles)
    # Print the NMF features
    print(nmf_features.round(2))
    return nmf_features


def nmf_features(nmf_features):
    # Create a pandas DataFrame: df
    df = pd.DataFrame(nmf_features, index=titles)
    # Print the row for 'Anne Hathaway'
    print(df.loc['Anne Hathaway'])
    # Print the row for 'Denzel Washington'
    print(df.loc['Denzel Washington'])


articles, titles = data.load_wikipedia_articles_and_titles()
nmf_features = nmf_applied_to_wikipedia_articles(articles)
nmf_features(nmf_features)
