from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from data import load_indian_liver_patient_preprocessed_data


def ada_boost_in_action(X_train, X_test, y_train, y_test):
    # Instantiate dt
    dt = DecisionTreeClassifier(max_depth=2, random_state=1)
    # Instantiate ada
    ada = AdaBoostClassifier(
        base_estimator=dt, n_estimators=180, random_state=1)
    # Fit ada to the training set
    ada.fit(X_train, y_train)
    # Compute the probabilities of obtaining the positive class
    y_pred_proba = ada.predict_proba(X_test)[:, 1]
    # Evaluate test-set roc_auc_score
    ada_roc_auc = roc_auc_score(y_test, y_pred_proba)
    # Print roc_auc_score
    print('ROC AUC score: {:.2f}'.format(ada_roc_auc))


df = load_indian_liver_patient_preprocessed_data()
X = df.drop(columns=["Liver_disease"])
y = df["Liver_disease"]
SEED = 1
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=SEED)
ada_boost_in_action(X_train, X_test, y_train, y_test)
