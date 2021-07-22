import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from data import load_hiking_data, load_volunteer_data


def encoding_categorical_variables_binary(hiking):
    # Set up the LabelEncoder object
    enc = LabelEncoder()
    # Apply the encoding to the "Accessible" column
    hiking["Accessible_enc"] = enc.fit_transform(hiking["Accessible"])
    # Compare the two columns
    print(hiking[["Accessible", "Accessible_enc"]].head())


def encoding_categorical_variables_one_hot_encoder(volunteer):
    # Transform the category_desc column
    category_enc = pd.get_dummies(volunteer["category_desc"])

    # Take a look at the encoded columns
    print(category_enc.head())


def engineering_numerical_features_taking_an_average():
    names = ["Sue", "Mark", "Sean", "Erin", "Jenny", "Russell"]
    runs = {
        "name": names
    }
    for i in range(5):
        run = np.random.normal(23, 5, size=6)
        key = "run" + str(i+1)
        runs[key] = run

    running_times_5k = pd.DataFrame(runs)

    # Create a list of the columns to average
    run_columns = ["run1", "run2", "run3", "run4", "run5"]

    # Use apply to create a mean column
    running_times_5k["mean"] = running_times_5k.apply(
        lambda row: row[run_columns].mean(), axis=1)

    # Take a look at the results
    print(running_times_5k)


def engineering_numerical_features_datetime(volunteer):
    # First, convert string column to date column
    volunteer["start_date_converted"] = pd.to_datetime(
        volunteer["start_date_date"])

    # Extract just the month from the converted column
    volunteer["start_date_month"] = volunteer["start_date_converted"].apply(
        lambda date: date.month)

    # Take a look at the converted and new month columns
    print(volunteer[["start_date_converted", "start_date_month"]].head())


def return_mileage(length):
    # Write a pattern to extract numbers and decimals
    pattern = re.compile(r"\d+\.\d+")

    # Search the text for matches
    mile = re.match(pattern, length)

    # If a value is returned, use group(0) to return the found value
    if mile is not None:
        return float(mile.group(0))


def engineering_features_from_strings_extraction(hiking):
    hiking.dropna(inplace=True)
    # Apply the function to the Length column and take a look at both columns
    hiking["Length_num"] = hiking["Length"].apply(
        lambda row: return_mileage(row))
    print(hiking[["Length", "Length_num"]].head())


def engineering_features_from_strings_tfidf(volunteer):
    volunteer = volunteer[volunteer["title"].notnull() & volunteer["category_desc"].notnull()]
    # Take the title text
    title_text = volunteer["title"]
    # Create the vectorizer method
    tfidf_vec = TfidfVectorizer()
    # Transform the text into tf-idf vectors
    text_tfidf = tfidf_vec.fit_transform(title_text)

    # Split the dataset according to the class distribution of category_desc
    y = volunteer["category_desc"]
    X_train, X_test, y_train, y_test = train_test_split(
        text_tfidf.toarray(), y, stratify=y)

    nb = GaussianNB(priors=None)
    # Fit the model to the training data
    nb.fit(X_train, y_train)

    # Print out the model's accuracy
    print(nb.score(X_test, y_test))

    return tfidf_vec, text_tfidf


hiking = load_hiking_data()
volunteer = load_volunteer_data()
encoding_categorical_variables_binary(hiking)

# encoding_categorical_variables_one_hot_encoder(volunteer)

# engineering_numerical_features_taking_an_average()

# engineering_numerical_features_datetime(volunteer)

# engineering_features_from_strings_extraction(hiking)

engineering_features_from_strings_tfidf(volunteer)
