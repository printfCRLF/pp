from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data import load_wisconsin_breast_cancer_data
from util import plot_labeled_decision_regions


wbc = load_wisconsin_breast_cancer_data()
X = wbc[["radius_mean", "concave points_mean"]]
mappings = {"M": 1, "B": 0}
y = wbc["diagnosis"].map(mappings)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y, random_state=1)


def train_your_first_classification_tree(X_train, X_test, y_train, y_test):
    # Instantiate a DecisionTreeClassifier 'dt' with a maximum depth of 6
    dt = DecisionTreeClassifier(max_depth=6, random_state=1)

    # Fit dt to the training set
    dt.fit(X_train, y_train)

    # Predict test set labels
    y_pred = dt.predict(X_test)
    print(y_pred[0:5])

    return dt


def evaluate_the_classification_tree(dt, X_test, y_test):
    # Predict test set labels
    y_pred = dt.predict(X_test)

    # Compute test set accuracy
    acc = accuracy_score(y_test, y_pred)
    print("Test set accuracy: {:.2f}".format(acc))


def logistic_regression_vs_classification_tree(dt, X_train, X_test, y_train, y_test):
    # Instatiate logreg
    logreg = LogisticRegression(random_state=1)

    # Fit logreg to the training set
    logreg.fit(X_train, y_train)

    # Define a list called clfs containing the two classifiers logreg and dt
    clfs = [logreg, dt]

    # Review the decision regions of the two classifiers
    plot_labeled_decision_regions(X_test, y_test, clfs)


dt = train_your_first_classification_tree(X_train, X_test, y_train, y_test)
evaluate_the_classification_tree(dt, X_test, y_test)
logistic_regression_vs_classification_tree(
    dt, X_train, X_test, y_train, y_test)
