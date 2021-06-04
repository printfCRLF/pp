import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


def exploring_categorical_features(df):
    df.boxplot('life', 'Region', rot=60)
    plt.show()


def creating_dummy_variables(df):
    # Create dummy variables: df_region
    df_region = pd.get_dummies(df)

    # Print the columns of df_region
    print(df_region.columns)

    # Create dummy variables with drop_first=True: df_region
    df_region = pd.get_dummies(df, drop_first=True)

    # Print the new columns of df_region
    print(df_region.columns)
    return df_region


def regression_with_categorical_features(df_region):
    X = df_region.drop(['life'], axis=1).to_numpy()
    y = df_region['life']
    # Instantiate a ridge regressor: ridge
    ridge = Ridge(alpha=0.5, normalize=True)

    # Perform 5-fold cross-validation: ridge_cv
    ridge_cv = cross_val_score(ridge, X, y, cv=5)

    # Print the cross-validated scores
    print(ridge_cv)


df = pd.read_csv('data/gm_2008_region.csv')
exploring_categorical_features(df)
df_region = creating_dummy_variables(df)
regression_with_categorical_features(df_region)
