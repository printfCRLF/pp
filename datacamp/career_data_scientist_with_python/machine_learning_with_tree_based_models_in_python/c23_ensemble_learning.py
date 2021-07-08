from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier
from data import load_indian_liver_patient_preprocessed_data


def define_the_ensemble():
    # Set seed for reproducibility
    SEED = 1
    # Instantiate lr
    lr = LogisticRegression(random_state=SEED)
    # Instantiate knn
    knn = KNN(n_neighbors=27)
    # Instantiate dt
    dt = DecisionTreeClassifier(min_samples_leaf=0.13, random_state=SEED)
    # Define the list classifiers
    classifiers = [('Logistic Regression', lr),
                   ('K Nearest Neighbours', knn), ('Classification Tree', dt)]

    return classifiers


def evaluate_individual_classifiers(classifiers, X_train, X_test, y_train, y_test):
    # Iterate over the pre-defined list of classifiers
    for clf_name, clf in classifiers:
        # Fit clf to the training set
        clf.fit(X_train, y_train)
        # Predict y_pred
        y_pred = clf.predict(X_test)
        # Calculate accuracy
        accuracy = accuracy_score(y_pred, y_test)
        # Evaluate clf's accuracy on the test set
        print('{:s} : {:.3f}'.format(clf_name, accuracy))


def better_performance_with_a_voting_classifier(classifiers, X_train, X_test, y_train, y_test):
    # Instantiate a VotingClassifier vc
    vc = VotingClassifier(estimators=classifiers)
    # Fit vc to the training set
    vc.fit(X_train, y_train)
    # Evaluate the test set predictions
    y_pred = vc.predict(X_test)
    # Calculate accuracy score
    accuracy = accuracy_score(y_pred, y_test)
    print('Voting Classifier: {:.3f}'.format(accuracy))


df = load_indian_liver_patient_preprocessed_data()
X = df.drop(columns=["Liver_disease"])
y = df["Liver_disease"]

SEED = 1
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=SEED)
classifiers = define_the_ensemble()
evaluate_individual_classifiers(classifiers, X_train, X_test, y_train, y_test)
better_performance_with_a_voting_classifier(
    classifiers, X_train, X_test, y_train, y_test)
