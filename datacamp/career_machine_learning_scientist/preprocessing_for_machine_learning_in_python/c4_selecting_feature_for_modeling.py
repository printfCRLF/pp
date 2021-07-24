import pandas as pd
from data import load_volunteer_data, load_wine_data
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


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


def exploring_text_vectors(volunteer):
    volunteer = volunteer[volunteer["title"].notnull(
    ) & volunteer["category_desc"].notnull()]
    # Take the title text
    title_text = volunteer["title"]
    # Create the vectorizer method
    tfidf_vec = TfidfVectorizer()
    # Transform the text into tf-idf vectors
    text_tfidf = tfidf_vec.fit_transform(title_text)

    vocab = {v: k for k, v in tfidf_vec.vocabulary_.items()}
    # Call the function to get the list of word indices
    filtered_words = words_to_filter(
        vocab, tfidf_vec.vocabulary_, text_tfidf, 3)

    # By converting filtered_words back to a list, we can use it to filter the columns in the text vector
    filtered_text = text_tfidf[:, list(filtered_words)]

    # Split the dataset according to the class distribution of category_desc, using the filtered_text vector
    y = volunteer["category_desc"]
    train_X, test_X, train_y, test_y = train_test_split(
        filtered_text.toarray(), y, stratify=y)

    # Fit the model to the training data
    nb = GaussianNB(priors=None)
    nb.fit(train_X, train_y)

    # Print out the model's accuracy
    print(nb.score(test_X, test_y))


def using_pca(wine):
    # Set up PCA and the X vector for diminsionality reduction
    pca = PCA()
    wine_X = wine.drop("Type", axis=1)
    y = wine["Type"]

    # Apply PCA to the wine dataset X vector
    transformed_X = pca.fit_transform(wine_X)

    # Look at the percentage of variance explained by the different components
    print(pca.explained_variance_ratio_)

    # Split the transformed X and the y labels into training and test sets
    X_wine_train, X_wine_test, y_wine_train, y_wine_test = train_test_split(
        transformed_X, y)

    knn = KNeighborsClassifier(n_neighbors=5)
    # Fit knn to the training data
    knn.fit(X_wine_train, y_wine_train)

    # Score knn on the test data and print it out
    score = knn.score(X_wine_test, y_wine_test)
    print(score)


volunteer = load_volunteer_data()
wine = load_wine_data()

# selecting_relevant_features(volunteer)
# exploring_text_vectors(volunteer)

# checking_for_correlated_features(wine)
using_pca(wine)
