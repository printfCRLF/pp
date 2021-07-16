import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from data import load_ansur_ii_male_data, load_ansur_ii_female_data


def prepare_data():
    ansur_ii_male = load_ansur_ii_male_data()
    cols = ['stature_m', 'buttockheight',
            'waistcircumference', 'shouldercircumference']
    ansur_df = ansur_ii_male[cols].sample(250)
    # X = ansur_ii_male[cols]
    # y = ansur_ii_male["bicepscircumferenceflexed"]
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # return X_train, X_test, y_train, y_test, X, y
    return ansur_df


def simple_pca(ansur_df):
    # Create a pairplot to inspect ansur_df
    sns.pairplot(ansur_df)
    plt.show()

    # Create the scaler
    scaler = StandardScaler()
    ansur_std = scaler.fit_transform(ansur_df)

    # Create the PCA instance and fit and transform the data with pca
    pca = PCA()
    pc = pca.fit_transform(ansur_std)
    pc_df = pd.DataFrame(pc, columns=['PC 1', 'PC 2', 'PC 3', 'PC 4'])

    # Create a pairplot of the principal component dataframe
    sns.pairplot(pc_df)
    plt.show()


def pca_on_larger_dataset():
    ansur_ii_male = load_ansur_ii_male_data()
    cols = ['stature_m', 'buttockheight', 'waistdepth', 'span', 'waistcircumference', 'shouldercircumference', 'footlength', 'handlength', 'functionalleglength', 'chestheight', 'chestcircumference',
            'cervicaleheight', 'sittingheight']

    ansur_df = ansur_ii_male[cols].sample(250)
    # Scale the data
    scaler = StandardScaler()
    ansur_std = scaler.fit_transform(ansur_df)

    # Apply PCA
    pca = PCA()
    pca.fit(ansur_std)

    # Inspect the explained variance ratio per component
    print(pca.explained_variance_ratio_)

    # Print the cumulative sum of the explained variance ratio
    print(pca.explained_variance_ratio_.cumsum())


# ansur_df = prepare_data()
# simple_pca(ansur_df)
# # After scaling with a StandardScaler and PCA transformation, none of the
# # principal components are correlated to one another.

pca_on_larger_dataset()
