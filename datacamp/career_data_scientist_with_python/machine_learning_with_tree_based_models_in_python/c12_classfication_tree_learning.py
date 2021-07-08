from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data import load_wisconsin_breast_cancer_data


wbc = load_wisconsin_breast_cancer_data()
X = wbc.drop(columns=["id", "diagnosis"])
mappings = {"M": 1, "B": 0}
y = wbc["diagnosis"].map(mappings)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y, random_state=1)


def entropy_vs_gini_index(X_train, X_test, y_train, y_test):
    accuracy_entropy = fit_predict_accuracy(
        X_train, X_test, y_train, y_test, 'entropy')
    # Print accuracy_entropy
    print('Accuracy achieved by using entropy: ', accuracy_entropy)

    accuracy_gini = fit_predict_accuracy(
        X_train, X_test, y_train, y_test, 'gini')
    # Print accuracy_gini
    print('Accuracy achieved by using the gini index: ', accuracy_gini)


def fit_predict_accuracy(X_train, X_test, y_train, y_test, criterion):
    # Instantiate a DecisionTreeClassifier, set 'criterion' as the information criterion
    dt = DecisionTreeClassifier(
        max_depth=8, criterion=criterion, random_state=1)

    # Fit dt_entropy to the training set
    dt.fit(X_train, y_train)

    # Use dt_entropy to predict test set labels
    y_pred = dt.predict(X_test)

    # Evaluate accuracy_entropy
    accuracy_entropy = accuracy_score(y_pred, y_test)

    return accuracy_entropy


entropy_vs_gini_index(X_train, X_test, y_train, y_test)
