import pandas as pd
from data import load_volunteer_data, load_wine_data
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from c3_feature_engineering import engineering_features_from_strings_tfidf


def selecting_relevant_features(volunteer):
    # Create a list of redundant column names to drop
    to_drop = ["vol_requests", "created_date",
               "locality", "region", "category_desc"]
    # Drop those columns from the dataset
    volunteer_subset = volunteer.drop(to_drop, axis=1)
    # Print out the head of the new dataset
    print(volunteer_subset.head())


def checking_for_correlated_features(wine):
    # Print out the column correlations of the wine dataset
    print(wine.corr().columns)

    # Take a minute to find the column where the correlation value is greater than 0.75 at least twice
    to_drop = "Flavanoids"

    # Drop that column from the DataFrame
    wine = wine.drop(to_drop, axis=1)


def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))

    # Let's transform that zipped dict into a series
    zipped_series = pd.Series({vocab[i]: zipped[i]
                               for i in vector[vector_index].indices})

    # Let's sort the series to pull out the top n weighted words
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]


def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):

        # Here we'll call the function from the previous exercise, and extend the list we're creating
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
    # Return the list in a set, so we don't get duplicate word indices
    return set(filter_list)


def exploring_text_vectors():
    y = volunteer["category_desc"]
    tfidf_vec, text_tfidf = engineering_features_from_strings_tfidf()
    # Print out the weighted words
    print(return_weights(vocab, tfidf_vec.vocabulary_, text_tfidf, 8, 3))

    # Split the dataset according to the class distribution of category_desc, using the filtered_text vector
    train_X, test_X, train_y, test_y = train_test_split(
        filtered_text.toarray(), y, stratify=y)

    # Fit the model to the training data
    nb = GaussianNB(priors=None)
    nb.fit(train_X, train_y)

    # Print out the model's accuracy
    print(nb.score(test_X, test_y))


volunteer = load_volunteer_data()
selecting_relevant_features(volunteer)
wine = load_wine_data()
checking_for_correlated_features(wine)
