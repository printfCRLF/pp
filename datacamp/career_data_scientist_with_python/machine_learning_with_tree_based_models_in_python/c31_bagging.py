from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from data import load_indian_liver_patient_preprocessed_data


def evaluate_bagging_performance(X_train, X_test, y_train, y_test):
    # Instantiate dt
    dt = DecisionTreeClassifier(random_state=1)

    # Instantiate bc
    bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)

    # Fit bc to the training set
    bc.fit(X_train, y_train)

    # Predict test set labels
    y_pred = bc.predict(X_test)

    # Evaluate acc_test
    acc_test = accuracy_score(y_test, y_pred)
    print('Test set accuracy of bc: {:.2f}'.format(acc_test))


def evaluating_single_tree_performance(X_train, X_test, y_train, y_test):
    dt = DecisionTreeClassifier(random_state=1)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    acc_test = accuracy_score(y_test, y_pred)
    print(
        'Test set accuracy of a single DecisionTree: {:.2f}'.format(acc_test))


df = load_indian_liver_patient_preprocessed_data()
X = df.drop(columns=["Liver_disease"])
y = df["Liver_disease"]
SEED = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y, random_state=SEED)
evaluate_bagging_performance(X_train, X_test, y_train, y_test)
evaluating_single_tree_performance(X_train, X_test, y_train, y_test)
