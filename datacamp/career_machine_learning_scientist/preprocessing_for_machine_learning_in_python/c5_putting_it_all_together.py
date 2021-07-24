
import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from data import load_ufo_data
from c4_selecting_feature_for_modeling import words_to_filter


def checking_column_types(ufo):
    # Check the column types
    print(ufo.dtypes)

    # Change the type of seconds to float
    ufo["seconds"] = ufo["seconds"].astype(float)

    # Change the date column to type datetime
    ufo["date"] = pd.to_datetime(ufo["date"])

    # Check the column types
    print(ufo[["seconds", "date"]].dtypes)

    return ufo


def dropping_missing_data(ufo):
    # Check how many values are missing in the length_of_time, state, and type columns
    print(ufo[["length_of_time", "state", "type"]].isnull().sum())

    # Keep only rows where length_of_time, state, and type are not null
    ufo_no_missing = ufo[ufo["length_of_time"].notnull() &
                         ufo["state"].notnull() &
                         ufo["type"].notnull()]

    # Print out the shape of the new dataset
    print(ufo_no_missing.shape)

    return ufo_no_missing


def return_minutes(time_string):

    # Use \d+ to grab digits
    pattern = re.compile(r"\d+")

    # Use match on the pattern and column
    num = re.match(pattern, time_string)
    if num is not None:
        return int(num.group(0))


def extract_numbers_from_strings(ufo):
    # Apply the extraction to the length_of_time column
    ufo["minutes"] = ufo["length_of_time"].apply(lambda t: return_minutes(t))

    # Take a look at the head of both of the columns
    print(ufo[["length_of_time", "minutes"]].head())

    ufo_no_missing = ufo[ufo["minutes"].notnull() & ufo["seconds"].notnull()]

    ufo_no_missing = ufo_no_missing[(ufo_no_missing["minutes"] != 0) & (
        ufo_no_missing["seconds"] != 0)]

    return ufo_no_missing


def identifying_features_for_standardization(ufo):
    # Check the variance of the seconds and minutes columns
    print(ufo[["seconds", "minutes"]].var())

    # Log normalize the seconds column
    ufo["seconds_log"] = np.log(ufo["seconds"])

    # Print out the variance of just the seconds_log column
    print(ufo["seconds_log"].var())

    return ufo


def encoding_categorical_variables(ufo):
    # Use Pandas to encode us values as 1 and others as 0
    ufo["country_enc"] = ufo["country"].apply(lambda c: 1 if c == "us" else 0)

    # Print the number of unique type values
    print(len(ufo["type"].unique()))

    # Create a one-hot encoded set of the type values
    type_set = pd.get_dummies(ufo["type"])

    # Concatenate this set back to the ufo DataFrame
    ufo = pd.concat([ufo, type_set], axis=1)

    return ufo


def features_from_dates(ufo):
    # Look at the first 5 rows of the date column
    print(ufo["date"].head())
    # Extract the month from the date column
    ufo["month"] = ufo["date"].apply(lambda d: d.month)
    # Extract the year from the date column
    ufo["year"] = ufo["date"].apply(lambda d: d.year)
    # Take a look at the head of all three columns
    print(ufo[["date", "month", "year"]].head())
    return ufo


def text_vectorization(ufo):
    # Take a look at the head of the desc field
    print(ufo["desc"].head())
    # Create the tfidf vectorizer object
    vec = TfidfVectorizer()
    # Use vec's fit_transform method on the desc field
    desc_tfidf = vec.fit_transform(ufo["desc"])
    # Look at the number of columns this creates
    print(desc_tfidf.shape)
    return vec, desc_tfidf


def selecting_ideal_dataset(ufo, vec, desc_tfidf):
    # Check the correlation between the seconds, seconds_log, and minutes columns
    print(ufo[["seconds", "seconds_log", "minutes"]].corr())

    # Make a list of features to drop
    to_drop = ["city", "country", "lat", "long", "state", "date",
               "recorded", "desc", "minutes", "seconds", "length_of_time"]

    # Drop those features
    ufo_dropped = ufo.drop(to_drop, axis=1)

    # Let's also filter some words out of the text vector we created
    vocab = {v: k for k, v in vec.vocabulary_.items()}
    filtered_words = words_to_filter(vocab, vec.vocabulary_,  desc_tfidf, 4)

    return ufo_dropped, filtered_words


def modeling_the_ufo_dataset(ufo):
    X = ufo.drop(["type", "country_enc"], axis=1)
    y = ufo["country_enc"]
    # Take a look at the features in the X set of data
    print(X.columns)

    # Split the X and y sets using train_test_split, setting stratify=y
    train_X, test_X, train_y, test_y = train_test_split(X, y, stratify=y)

    # Fit knn to the training sets
    knn = KNeighborsClassifier()
    knn.fit(train_X, train_y)

    # Print the score of knn on the test sets
    print(knn.score(test_X, test_y))


def modeling_ufo_dataset_2(ufo, filtered_words, desc_tfidf):
    y = ufo["type"]
    # Use the list of filtered words we created to filter the text vector
    filtered_text = desc_tfidf[:, list(filtered_words)]

    # Split the X and y sets using train_test_split, setting stratify=y
    train_X, test_X, train_y, test_y = train_test_split(
        filtered_text.toarray(), y, stratify=y)

    # Fit nb to the training sets
    nb = GaussianNB(priors=None)
    nb.fit(train_X, train_y)

    # Print the score of nb on the test sets
    print(nb.score(test_X, test_y))


ufo = load_ufo_data()
ufo = checking_column_types(ufo)
ufo_no_missing = dropping_missing_data(ufo)
ufo_no_missing = extract_numbers_from_strings(ufo_no_missing)
ufo = identifying_features_for_standardization(ufo_no_missing)
ufo = encoding_categorical_variables(ufo)
ufo = features_from_dates(ufo)
vec, desc_tfidf = text_vectorization(ufo)
ufo_dropped, filtered_words = selecting_ideal_dataset(ufo, vec, desc_tfidf)
modeling_the_ufo_dataset(ufo_dropped)
modeling_ufo_dataset_2(ufo_dropped, filtered_words, desc_tfidf)
