import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from data import load_wine_data


def modeling_without_normalizing(wine):
    X = wine.drop("Type", axis=1)
    y = wine["Type"]
    # Split the dataset and labels into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # Fit the k-nearest neighbors model to the training data
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    # Score the model on the test data
    print(knn.score(X_test, y_test))


def log_normalization_in_python(wine):
    # Print out the variance of the Proline column
    print(wine["Proline"].var())

    # Apply the log normalization function to the Proline column
    wine["Proline_log"] = np.log(wine["Proline"])

    # Check the variance of the normalized Proline column
    print(wine["Proline_log"].var())


def standardizing_columns(wine):
    X = wine.drop("Type", axis=1)
    y = wine["Type"]

    # Split the dataset and labels into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    # Fit the k-nearest neighbors model to the training data
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    # Score the model on the test data
    print(knn.score(X_test, y_test))

    # Create the scaler
    ss = StandardScaler()
    # Take a subset of the DataFrame you want to scale
    wine_subset = wine[["Ash", "Alcalinity of ash", "Magnesium"]]
    # Apply the scaler to the DataFrame subset
    wine_subset_scaled = ss.fit_transform(wine_subset)

    X_scaled = ss.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
    # Fit the k-nearest neighbors model to the training data.
    knn.fit(X_train, y_train)
    # Score the model on the test data.
    print(knn.score(X_test, y_test))


wine = load_wine_data()
# modeling_without_normalizing(wine)
# log_normalization_in_python(wine)
standardizing_columns(wine)
