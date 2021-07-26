import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from data import load_inargural_speech_data


def cleaning_up_your_text(speech_df):
    # Replace all non letter characters with a whitespace
    speech_df['text_clean'] = speech_df['text'].str.replace('[^a-zA-Z]', ' ')

    # Change to lower case
    speech_df['text_clean'] = speech_df['text_clean'].str.lower()

    # Print the first 5 rows of the text_clean column
    print(speech_df['text_clean'].head())
    return speech_df


def high_level_text_features(speech_df):
    # Find the length of each text
    speech_df['char_cnt'] = speech_df['text_clean'].str.len()

    # Count the number of words in each text
    speech_df['word_cnt'] = speech_df['text_clean'].str.split().str.len()

    # Find the average length of word
    speech_df['avg_word_length'] = speech_df['char_cnt'] / \
        speech_df['word_cnt']

    # Print the first 5 rows of these columns
    print(speech_df[['text_clean', 'char_cnt', 'word_cnt', 'avg_word_length']])


def couting_words(speech_df):
    # Instantiate CountVectorizer
    cv = CountVectorizer()
    # Fit the vectorizer
    cv.fit(speech_df['text_clean'])
    # Print feature names
    print(cv.get_feature_names())

    # Apply the vectorizer
    cv_transformed = cv.transform(speech_df['text_clean'])
    # Print the full array
    cv_array = cv_transformed.toarray()
    # Print the shape of cv_array
    print(cv_array.shape)


def limiting_your_features(speech_df):
    # Specify arguements to limit the number of features generated
    cv = CountVectorizer(min_df=0.2, max_df=0.8)
    # Fit, transform, and convert into array
    cv_transformed = cv.fit_transform(speech_df['text_clean'])
    cv_array = cv_transformed.toarray()
    # Print the array shape
    print(cv_array.shape)

    # Create a DataFrame with these features
    cv_df = pd.DataFrame(cv_array,
                         columns=cv.get_feature_names()).add_prefix('Counts_')
    # Add the new columns to the original DataFrame
    speech_df_new = pd.concat([speech_df, cv_df], axis=1, sort=False)
    print(speech_df_new.head())


speech_df = load_inargural_speech_data()
speech_df = cleaning_up_your_text(speech_df)
high_level_text_features(speech_df)
couting_words(speech_df)
limiting_your_features(speech_df)
