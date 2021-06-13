import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression


def regualrized_logistic_regression():
    digits = datasets.load_digits()
    X_train, X_valid, y_train, y_valid = train_test_split(
        digits.data, digits.target)

    # Train and validaton errors initialized as empty list
    train_errs = list()
    valid_errs = list()
    C_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

    # Loop over values of C_value
    for C_value in C_values:
        # Create LogisticRegression object and fit
        lr = LogisticRegression(C=C_value)
        lr.fit(X_train, y_train)

        # Evaluate error rates and append to lists
        train_errs.append(1.0 - lr.score(X_train, y_train))
        valid_errs.append(1.0 - lr.score(X_valid, y_valid))

    # Plot results
    _ = plt.semilogx(C_values, train_errs, C_values, valid_errs)
    _ = plt.legend(("train", "validation"))
    _ = plt.xlabel("C, inverse of regularization strength")
    _ = plt.ylabel("error")
    _ = plt.show()


def logistic_regression_and_feature_selection():
    # Specify L1 regularization
    lr = LogisticRegression(penalty='l1')

    # Instantiate the GridSearchCV object and run the search
    searcher = GridSearchCV(lr, {'C': [0.001, 0.01, 0.1, 1, 10]})
    searcher.fit(X_train, y_train)

    # Report the best parameters
    print("Best CV params", searcher.best_params_)

    # Find the number of nonzero coefficients (selected features)
    best_lr = searcher.best_estimator_
    coefs = best_lr.coef_
    print("Total number of features:", coefs.size)
    print("Number of selected features:", np.count_nonzero(coefs))


def identifying_the_most_positive_and_negative_words():
    # Get the indices of the sorted cofficients
    inds_ascending = np.argsort(lr.coef_.flatten())
    inds_descending = inds_ascending[::-1]

    # Print the most positive words
    print("Most positive words: ", end="")
    for i in range(5):
        print(vocab[inds_descending[i]], end=", ")
    print("\n")

    # Print most negative words
    print("Most negative words: ", end="")
    for i in range(5):
        print(vocab[inds_ascending[i]], end=", ")
    print("\n")


sns.set()
regualrized_logistic_regression()
# need to load movie review data first
# logistic_regression_and_feature_selection()
# identifying_the_most_positive_and_negative_words()
