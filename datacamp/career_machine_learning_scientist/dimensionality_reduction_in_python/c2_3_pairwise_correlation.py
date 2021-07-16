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
    cols = ['elbowrestheight', 'wristcircumference',
            'anklecircumference', 'buttockheight', 'crotchheight']
    ansur_df = df[cols]
    return ansur_df


def visualizing_correlation_matrix(ansur_df):
    # Create the correlation matrix
    corr = ansur_df.corr()
    # Draw the heatmap
    sns.heatmap(corr, center=0, linewidths=1, annot=True, fmt=".2f")
    plt.show()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Add the mask to the heatmap
    sns.heatmap(corr, mask=mask, center=0, linewidths=1, annot=True, fmt=".2f")
    plt.show()


sns.set()
ansur_df = prepare_data()
visualizing_correlation_matrix(ansur_df)
