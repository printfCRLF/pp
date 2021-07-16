import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from data import load_ansur_ii_male_data, load_ansur_ii_female_data


def accuracy_with_large_dimension(ansur_df):
    # Select the Gender column as the feature to be predicted (y)
    y = ansur_df["Gender"]
    # Remove the Gender column to create the training data
    X = ansur_df.drop("Gender", axis=1)

    # Perform a 70% train and 30% test data split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    print("{} rows in test set vs. {} in training set. {} Features.".format(
        X_test.shape[0], X_train.shape[0], X_test.shape[1]))

    # Create an instance of the Support Vector Classification class
    svc = SVC()

    # Fit the model to the training data
    svc.fit(X_train, y_train)

    # Calculate accuracy scores on both train and test data
    accuracy_train = accuracy_score(y_train, svc.predict(X_train))
    accuracy_test = accuracy_score(y_test, svc.predict(X_test))

    print("{0:.1%} accuracy on test set vs. {1:.1%} on training set".format(
        accuracy_test, accuracy_train))


def accuracy_after_dimensionality_reduction(ansur_df):
    # Assign just the 'neckcircumferencebase' column from ansur_df to X
    X = ansur_df[["neckcircumferencebase"]]
    y = ansur_df["Gender"]

    # Split the data, instantiate a classifier and fit the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    svc = SVC()
    svc.fit(X_train, y_train)

    # Calculate accuracy scores on both train and test data
    accuracy_train = accuracy_score(y_train, svc.predict(X_train))
    accuracy_test = accuracy_score(y_test, svc.predict(X_test))

    print("{0:.1%} accuracy on test set vs. {1:.1%} on training set".format(
        accuracy_test, accuracy_train))


ansur_ii_male = load_ansur_ii_male_data().sample(500)
ansur_ii_female = load_ansur_ii_female_data().sample(500)
df = pd.concat([ansur_ii_male, ansur_ii_female])
non_numeric = ['Branch', 'Component', "weight_kg",
               "stature_m", "BMI", "BMI_class", "Height_class"]

df.drop(non_numeric, axis=1, inplace=True)
accuracy_with_large_dimension(df)
accuracy_after_dimensionality_reduction(df)
