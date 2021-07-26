from numpy import load
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from data import load_inargural_speech_data
from c41_encoding_text import cleaning_up_your_text


def using_longer_ngrams(speech_df):
    # Instantiate a trigram vectorizer
    cv_trigram_vec = CountVectorizer(max_features=100,
                                     stop_words='english',
                                     ngram_range=(3, 3))

    # Fit and apply trigram vectorizer
    cv_trigram = cv_trigram_vec.fit_transform(speech_df['text_clean'])

    # Print the trigram features
    print(cv_trigram_vec.get_feature_names())

    # Create a DataFrame of the features
    cv_tri_df = pd.DataFrame(cv_trigram.toarray(),
                             columns=cv_trigram_vec.get_feature_names()).add_prefix('Counts_')

    # Print the top 5 words in the sorted output
    print(cv_tri_df.sum().sort_values(ascending=False).head())


speech_df = load_inargural_speech_data()
speech_df = cleaning_up_your_text(speech_df)
using_longer_ngrams(speech_df)
