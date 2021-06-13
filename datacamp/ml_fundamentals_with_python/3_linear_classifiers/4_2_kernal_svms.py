from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn import datasets


def gridSearchCV_warm_up(X, y):
    # Instantiate an RBF SVM
    svm = SVC()

    # Instantiate the GridSearchCV object and run the search
    parameters = {'gamma': [0.00001, 0.0001, 0.001, 0.01, 0.1]}
    searcher = GridSearchCV(svm, parameters)
    searcher.fit(X, y)

    # Report the best parameters
    print("Best CV params", searcher.best_params_)


def tunning_gamma_and_c(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    # Instantiate an RBF SVM
    svm = SVC()

    # Instantiate the GridSearchCV object and run the search
    parameters = {'C': [0.1, 1, 10], 'gamma': [
        0.00001, 0.0001, 0.001, 0.01, 0.1]}
    searcher = GridSearchCV(svm, parameters)
    searcher.fit(X_train, y_train)

    # Report the best parameters and the corresponding score
    print("Best CV params", searcher.best_params_)
    print("Best CV accuracy", searcher.best_score_)

    # Report the test accuracy using these best parameters
    print("Test accuracy of best grid search hypers:",
          searcher.score(X_test, y_test))


def using_SGDClassifier(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    # We set random_state=0 for reproducibility
    linear_classifier = SGDClassifier(random_state=0)

    # Instantiate the GridSearchCV object and run the search
    parameters = {'alpha': [0.00001, 0.0001, 0.001, 0.01, 0.1, 1],
                  'loss': ['hinge', 'log'], 'penalty': ['l1', 'l2']}
    searcher = GridSearchCV(linear_classifier, parameters, cv=10)
    searcher.fit(X_train, y_train)

    # Report the best parameters and the corresponding score
    print("Best CV params", searcher.best_params_)
    print("Best CV accuracy", searcher.best_score_)
    print("Test accuracy of best grid search hypers:",
          searcher.score(X_test, y_test))


df = datasets.load_digits()
X = df.data
y = df.target
#gridSearchCV_warm_up(X, y)
#tunning_gamma_and_c(X, y)
using_SGDClassifier(X, y)
