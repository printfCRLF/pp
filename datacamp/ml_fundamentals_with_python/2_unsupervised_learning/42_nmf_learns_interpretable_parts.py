import pandas as pd
from sklearn.decomposition import NMF
import data


def nmf_learns_topics_of_documents(articles, words):
    model = NMF(n_components=6)
    # Fit the model to articles
    model.fit(articles)
    # Transform the articles: nmf_features
    nmf_features = model.transform(articles)
    # Print the NMF features
    print(nmf_features.round(2))

    # Create a DataFrame: components_df
    components_df = pd.DataFrame(model.components_, columns=words)

    # Print the shape of the DataFrame
    print(components_df.shape)

    # Select row 3: component
    component = components_df.iloc[3, ]

    # Print result of nlargest
    print(component.nlargest())


articles, titles = data.load_wikipedia_articles_and_titles()
words = data.load_wikipedia_words()
nmf_learns_topics_of_documents(articles, words)
