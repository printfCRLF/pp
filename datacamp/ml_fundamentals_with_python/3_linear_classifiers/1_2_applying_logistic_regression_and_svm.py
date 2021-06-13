from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer


def runninng_logistic_regression():
    digits = datasets.load_digits()
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target)

    # Apply logistic regression and print scores
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    print("LogisticRegression - train score", lr.score(X_train, y_train))
    print("LogisticRegression - test score", lr.score(X_test, y_test))

    # Apply SVM and print scores
    svm = SVC()
    svm.fit(X_train, y_train)
    print("SVC - training score", svm.score(X_train, y_train))
    print("SVC - training score", svm.score(X_test, y_test))


def sentiment_analysis_for_movie_reviews(X, y):
    # Instantiate logistic regression and train
    lr = LogisticRegression()
    lr.fit(X, y)

    # Predict sentiment for a glowing review
    review1 = "LOVED IT! This movie was amazing. Top 10 this year."
    review1_features = get_features(review1)
    print("Review:", review1)
    print("Probability of positive review:",
          lr.predict_proba(review1_features)[0, 1])

    # Predict sentiment for a poor review
    review2 = "Total junk! I'll never watch a film by that director again, no matter how good the reviews."
    review2_features = get_features(review2)
    print("Review:", review2)
    print("Probability of positive review:",
          lr.predict_proba(review2_features)[0, 1])


def get_features(review):
    vectorizer = CountVectorizer()
    return vectorizer.transform([review])


runninng_logistic_regression()
# Large Movie Review dataset is not loaded.
# sentiment_analysis_for_movie_reviews()
