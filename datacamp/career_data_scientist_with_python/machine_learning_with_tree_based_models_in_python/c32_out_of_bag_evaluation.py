from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from data import load_wisconsin_breast_cancer_data


def out_of_bag_evaluation_in_action(X_train, X_test, y_train, y_test):
    # Instantiate dt
    dt = DecisionTreeClassifier(min_samples_leaf=8, random_state=1)
    # Instantiate bc
    bc = BaggingClassifier(base_estimator=dt, n_estimators=50,
                           oob_score=True, random_state=1)

    # Fit bc to the training set
    bc.fit(X_train, y_train)
    # Predict test set labels
    y_pred = bc.predict(X_test)
    # Evaluate test set accuracy
    acc_test = accuracy_score(y_pred, y_test)
    # Evaluate OOB accuracy
    acc_oob = bc.oob_score_
    # Print acc_test and acc_oob
    print('Test set accuracy: {:.3f}, OOB accuracy: {:.3f}'.format(
        acc_test, acc_oob))


wbc = load_wisconsin_breast_cancer_data()
X = wbc.drop(columns=["id", "diagnosis"])
mappings = {"M": 1, "B": 0}
y = wbc["diagnosis"].map(mappings)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y, random_state=1)
out_of_bag_evaluation_in_action(X_train, X_test, y_train, y_test)
