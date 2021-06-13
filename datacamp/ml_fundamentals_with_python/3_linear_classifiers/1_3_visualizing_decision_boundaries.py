from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from util import plot_classifier


def plot_4_classifiers(X, y, clfs):

    # Set-up 2x2 grid for plotting.
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    for clf, ax, title in zip(clfs, sub.flatten(), ("(1) LogisticRegression", "(2) LinearSVC", "(3) SVC", "(4) KNN")):
        # clf.fit(X, y)
        plot_classifier(X, y, clf, ax, ticks=True)
        ax.set_title(title)
    plt.show()


def visualizing_decision_boundaries():
    wine = load_wine()
    samples = wine.data
    X = samples[20:70,[0, 1]]
    y = wine.target[20:70]
    # Define the classifiers
    classifiers = [LogisticRegression(), LinearSVC(), SVC(),
                   KNeighborsClassifier()]

    # Fit the classifiers
    for c in classifiers:
        c.fit(X, y)

    # Plot the classifiers
    plot_4_classifiers(X, y, classifiers)
    plt.show()


visualizing_decision_boundaries()
