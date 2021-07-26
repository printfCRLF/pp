import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from data import load_inargural_speech_data
from c41_encoding_text import cleaning_up_your_text


def tfidf(speech_df):
    # Instantiate TfidfVectorizer
    tv = TfidfVectorizer(max_features=100, stop_words="english")
    # Fit the vectroizer and transform the data
    tv_transformed = tv.fit_transform(speech_df['text_clean'])
    # Create a DataFrame with these features
    tv_df = pd.DataFrame(tv_transformed.toarray(),
                         columns=tv.get_feature_names()).add_prefix('TFIDF_')
    print(tv_df.head())

    # Isolate the row to be examined
    sample_row = tv_df.iloc[0]

    # Print the top 5 words of the sorted output
    print(sample_row.sort_values(ascending=False).head())


def transforming_unseen_data(train_speech_df, test_speech_df):
    # Instantiate TfidfVectorizer
    tv = TfidfVectorizer(max_features=100, stop_words='english')

    # Fit the vectroizer and transform the data
    tv_transformed = tv.fit_transform(train_speech_df['text_clean'])

    # Transform test data
    test_tv_transformed = tv.transform(test_speech_df['text_clean'])

    # Create new features for the test set
    test_tv_df = pd.DataFrame(test_tv_transformed.toarray(),
                              columns=tv.get_feature_names()).add_prefix('TFIDF_')
    print(test_tv_df.head())


speech_df = load_inargural_speech_data()
speech_df = cleaning_up_your_text(speech_df)
train_speech_df = speech_df.iloc[:45, :]
test_speech_df = speech_df.iloc[45:, :]
tfidf(speech_df)
transforming_unseen_data(train_speech_df, test_speech_df)
