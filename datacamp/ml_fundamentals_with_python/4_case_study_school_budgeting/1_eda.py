import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import random
import seaborn as sns
from util import compute_log_loss


def loading_data():
    # https://github.com/datacamp/course-resources-ml-with-experts-budgets
    # https://github.com/drivendata/boxplots-for-education-1st-place

    df_all = pd.read_csv('data/TrainingData.csv', index_col=0)
    df = df_all.sample(1560)
    print(df.info())
    print(df.describe())
    return df


def exploring_fte_column(df):
    plt.hist(df['FTE'].dropna())

    # Add title and labels
    plt.title('Distribution of %full-time \n employee works')
    plt.xlabel('% of full-time')
    plt.ylabel('num employees')

    # Display the histogram
    plt.show()


def data_types(df):
    print(df.dtypes.value_counts())
    LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type',
              'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']

    # Define the lambda function: categorize_label
    def categorize_label(x): return x.astype('category')

    # Convert df[LABELS] to a categorical type
    df[LABELS] = df[LABELS].apply(categorize_label, axis=0)

    # Print the converted dtypes
    print(df[LABELS].dtypes)
    print(df[LABELS].head())

    # Calculate number of unique values for each label: num_unique_labels
    num_unique_labels = df[LABELS].apply(pd.Series.nunique)

    # Plot number of unique values for each label
    num_unique_labels.plot(kind='bar')

    # Label the axes
    plt.xlabel('Labels')
    plt.ylabel('Number of unique values')

    # Display the plot
    plt.xticks(rotation=60)
    plt.autoscale()
    plt.show()


def compute_log_loss_with_numpy():
    actual_labels = np.array([1., 1., 1., 1., 1., 0., 0., 0., 0., 0.])
    correct_confident = np.array(
        [0.95, 0.95, 0.95, 0.95, 0.95, 0.05, 0.05, 0.05, 0.05, 0.05])
    correct_not_confident = np.array(
        [0.65, 0.65, 0.65, 0.65, 0.65, 0.35, 0.35, 0.35, 0.35, 0.35])
    wrong_not_confident = np.array(
        [0.35, 0.35, 0.35, 0.35, 0.35, 0.65, 0.65, 0.65, 0.65, 0.65])
    wrong_confident = np.array(
        [0.05, 0.05, 0.05, 0.05, 0.05, 0.95, 0.95, 0.95, 0.95, 0.95])

    # Compute and print log loss for 1st case
    correct_confident_loss = compute_log_loss(correct_confident, actual_labels)
    print("Log loss, correct and confident: {}".format(correct_confident_loss))

    # Compute log loss for 2nd case
    correct_not_confident_loss = compute_log_loss(
        correct_not_confident, actual_labels)
    print("Log loss, correct and not confident: {}".format(
        correct_not_confident_loss))

    # Compute and print log loss for 3rd case
    wrong_not_confident_loss = compute_log_loss(
        wrong_not_confident, actual_labels)
    print("Log loss, wrong and not confident: {}".format(wrong_not_confident_loss))

    # Compute and print log loss for 4th case
    wrong_confident_loss = compute_log_loss(wrong_confident, actual_labels)
    print("Log loss, wrong and confident: {}".format(wrong_confident_loss))

    # Compute and print log loss for actual labels
    actual_labels_loss = compute_log_loss(actual_labels, actual_labels)
    print("Log loss, actual labels: {}".format(actual_labels_loss))


# sns.set()
df = loading_data()
exploring_fte_column(df)
data_types(df)
compute_log_loss_with_numpy()
