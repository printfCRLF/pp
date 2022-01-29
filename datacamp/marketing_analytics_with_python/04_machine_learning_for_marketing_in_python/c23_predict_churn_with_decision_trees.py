import numpy as np
import pandas as pd
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, recall_score
from data import load_telco_data
from c12_preparation_for_modeling import seperate_numerical_and_categorical_columns, encoding_categorical_and_scale_numerical_variables
from c13_ml_modeling_steps import split_data_into_training_and_testing


def fit_decision_tree_model(train_X, test_X, train_Y, test_Y):
    # Initialize decision tree classifier
    mytree = DecisionTreeClassifier()

    # Fit the decision tree on training data
    mytree.fit(train_X, train_Y)

    # Predict churn labels on testing data
    pred_test_Y = mytree.predict(test_X)

    # Calculate accuracy score on testing data
    test_accuracy = accuracy_score(test_Y, pred_test_Y)

    # Print test accuracy
    print('Test accuracy:', round(test_accuracy, 4))

    return mytree


def identify_optimal_tree_depth(train_X, test_X, train_Y, test_Y):
    depth_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    depth_tuning = np.array([[2.,  0.],
                             [3.,  0.],
                             [4.,  0.],
                             [5.,  0.],
                             [6.,  0.],
                             [7.,  0.],
                             [8.,  0.],
                             [9.,  0.],
                             [10.,  0.],
                             [11.,  0.],
                             [12.,  0.],
                             [13.,  0.],
                             [14.,  0.]])
    # Run a for loop over the range of depth list length
    for index in range(0, len(depth_list)):
        # Initialize and fit decision tree with the `max_depth` candidate
        mytree = DecisionTreeClassifier(max_depth=depth_list[index])
        mytree.fit(train_X, train_Y)
        # Predict churn on the testing data
        pred_test_Y = mytree.predict(test_X)
        # Calculate the recall score
        depth_tuning[index, 1] = recall_score(
            test_Y, pred_test_Y, pos_label="Yes")

    # Name the columns and print the array as pandas DataFrame
    col_names = ['Max_Depth', 'Recall']
    print(pd.DataFrame(depth_tuning, columns=col_names))


def break_down_decision_tree_rules(mytree):
    # Export graphviz object from the trained decision tree
    exported = export_graphviz(decision_tree=mytree,
                               # Assign feature names
                               out_file=None, feature_names=train_X.columns,
                               # Set precision to 1 and add class names
                               precision=1, class_names=['Not churn', 'Churn'], filled=True, )

    # Call the Source function and pass the exported graphviz object
    graph = graphviz.Source(exported)
    graph.render(view=True, format="png")
    # Display the decision tree
    # display_image("/usr/local/share/datasets/decision_tree_rules.png")


if __name__ == "__main__":
    telco_raw = load_telco_data()
    categorical, numerical = seperate_numerical_and_categorical_columns(
        telco_raw)
    df = encoding_categorical_and_scale_numerical_variables(
        telco_raw, categorical, numerical)
    train_X, test_X, train_Y, test_Y = split_data_into_training_and_testing(df)
    mytree = fit_decision_tree_model(train_X, test_X, train_Y, test_Y)
    # identify_optimal_tree_depth(train_X, test_X, train_Y, test_Y)
    break_down_decision_tree_rules(mytree)
