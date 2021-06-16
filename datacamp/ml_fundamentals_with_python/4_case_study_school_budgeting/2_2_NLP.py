import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from util import combine_text_columns

def loading_budget_data():
    # https://github.com/datacamp/course-resources-ml-with-experts-budgets
    # https://github.com/drivendata/boxplots-for-education-1st-place
    df_all = pd.read_csv('data/TrainingData.csv', index_col=0)
    # df = df_all.sample(1560 * 20)
    df = df_all
    # print(df.info())
    print(df.describe())

    NUMERIC_COLUMNS = ['FTE', 'Total']
    LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type',
              'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']
    return df, NUMERIC_COLUMNS, LABELS


def create_a_bag_of_words(df):
    # Create the token pattern: TOKENS_ALPHANUMERIC
    TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

    # Fill missing values in df.Position_Extra
    df.Position_Extra.fillna('', inplace=True)

    # Instantiate the CountVectorizer: vec_alphanumeric
    vec_alphanumeric = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

    # Fit to the data
    vec_alphanumeric.fit(df.Position_Extra)

    # Print the number of tokens and first 15 tokens
    msg = "There are {} tokens in Position_Extra if we split on non-alpha numeric"
    print(msg.format(len(vec_alphanumeric.get_feature_names())))
    print(vec_alphanumeric.get_feature_names()[:15])


def what_is_in_token(df, NUMERIC_COLUMNS, LABELS):
    # Create the basic token pattern
    TOKENS_BASIC = '\\S+(?=\\s+)'

    # Create the alphanumeric token pattern
    TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

    # Instantiate basic CountVectorizer: vec_basic
    vec_basic = CountVectorizer(token_pattern=TOKENS_BASIC)

    # Instantiate alphanumeric CountVectorizer: vec_alphanumeric
    vec_alphanumeric = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

    # Create the text vector
    text_vector = combine_text_columns(df, NUMERIC_COLUMNS + LABELS)

    # Fit and transform vec_basic
    vec_basic.fit_transform(text_vector)

    # Print number of tokens of vec_basic
    print("There are {} tokens in the dataset".format(
        len(vec_basic.get_feature_names())))

    # Fit and transform vec_alphanumeric
    vec_alphanumeric.fit_transform(text_vector)

    # Print number of tokens of vec_alphanumeric
    print("There are {} alpha-numeric tokens in the dataset".format(
        len(vec_alphanumeric.get_feature_names())))


budget_data, NUMERIC_COLUMNS, LABELS = loading_budget_data()
# create_a_bag_of_words(budget_data)
what_is_in_token(budget_data, NUMERIC_COLUMNS, LABELS)
