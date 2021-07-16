import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold
from data import load_ansur_ii_male_data, load_ansur_ii_female_data, load_school_data


def prepare_data():
    ansur_ii_male = load_ansur_ii_male_data().sample(500)
    ansur_ii_female = load_ansur_ii_female_data().sample(500)
    df = pd.concat([ansur_ii_male, ansur_ii_female])
    cols = ['headbreadth', 'headcircumference',
            'headlength', 'tragiontopofhead']
    head_df = df[cols]
    head_df["n_hairs"] = np.random.normal(100000, 10)
    head_df["measurement_error"] = np.random.normal(0.1, 1.387893e-17)
    return head_df


def finding_a_good_variance_threshold(head_df):
    # Create the boxplot
    head_df.boxplot()
    plt.show()

    # Normalize the data
    normalized_df = head_df / head_df.mean()

    normalized_df.boxplot()
    plt.show()


def features_with_low_variance(head_df):
    # Create a VarianceThreshold feature selector
    sel = VarianceThreshold(threshold=0.001)
    # Fit the selector to normalized head_df
    sel.fit(head_df / head_df.mean())
    # Create a boolean mask
    mask = sel.get_support()
    # Apply the mask to create a reduced dataframe
    reduced_df = head_df.loc[:, mask]

    print("Dimensionality reduced from {} to {}.".format(
        head_df.shape[1], reduced_df.shape[1]))


def removing_features_with_many_missing_values(school_df):
    # Create a boolean mask on whether each feature less than 50% missing values.
    mask = school_df.isna().sum() / len(school_df) < 0.5
    # Create a reduced dataset by applying the mask
    reduced_df = school_df.loc[:, mask]

    print(school_df.shape)
    print(reduced_df.shape)


sns.set()

head_df = prepare_data()
finding_a_good_variance_threshold(head_df)
features_with_low_variance(head_df)

school_df = load_school_data()
removing_features_with_many_missing_values(school_df)
