import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold
from data import load_ansur_ii_male_data, load_ansur_ii_female_data


def prepare_data():
    ansur_ii_male = load_ansur_ii_male_data().sample(500)
    ansur_ii_female = load_ansur_ii_female_data().sample(500)
    df = pd.concat([ansur_ii_male, ansur_ii_female])
    return df


def filtering_out_highly_correlated_features(ansur_df):
    # Calculate the correlation matrix and take the absolute value
    corr_matrix = ansur_df.corr().abs()

    # Create a True/False mask and apply it
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    tri_df = corr_matrix.mask(mask)

    # List column names of highly correlated features (r > 0.95)
    to_drop = [c for c in tri_df.columns if any(tri_df[c] > 0.95)]

    # Drop the features in the to_drop list
    reduced_df = ansur_df.drop(to_drop, axis=1)

    print("The reduced dataframe has {} columns.".format(reduced_df.shape[1]))


ansur_df = prepare_data()
filtering_out_highly_correlated_features(ansur_df)
