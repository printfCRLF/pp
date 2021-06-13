from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from util import plot_classifier


def effect_of_removing_examples(X, y):
    # Train a linear SVM
    svm = SVC(kernel="linear")
    svm.fit(X, y)
    plot_classifier(X, y, svm, lims=(11, 15, 0, 6))

    # Make a new data set keeping only the support vectors
    print("Number of original examples", len(X))
    print("Number of support vectors", len(svm.support_))
    X_small = X[svm.support_]
    y_small = y[svm.support_]

    # Train a new SVM using only the support vectors
    svm_small = SVC(kernel="linear")
    svm_small.fit(X_small, y_small)
    plot_classifier(X_small, y_small, svm_small, lims=(11, 15, 0, 6))


df = datasets.load_wine()
X = df.data[:, [0, 1]]
y = df.target
effect_of_removing_examples(X, y)
