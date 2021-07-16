import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from data import load_pokemon_data


def understanding_components(poke_df):
    cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    poke_df = poke_df[cols]

    # Build the pipeline
    pipe = Pipeline([('scaler', StandardScaler()),
                    ('reducer', PCA(n_components=2))])

    # Fit it to the dataset and extract the component vectors
    pipe.fit(poke_df)
    vectors = pipe.steps[1][1].components_.round(2)

    # Print feature effects
    print('PC 1 effects = ' + str(dict(zip(poke_df.columns, vectors[0]))))
    print('PC 2 effects = ' + str(dict(zip(poke_df.columns, vectors[1]))))


def plotting_pca(df):
    cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    poke_df = df[cols]

    pipe = Pipeline([('scaler', StandardScaler()),
                     ('reducer', PCA(n_components=2))])

    # Fit the pipeline to poke_df and transform the data
    pc = pipe.fit_transform(poke_df)

    # Add the 2 components to poke_cat_df
    poke_cat_df = df[["Type 1", "Legendary"]]
    poke_cat_df['PC 1'] = pc[:, 0]
    poke_cat_df['PC 2'] = pc[:, 1]

    # Use the Type feature to color the PC 1 vs PC 2 scatterplot
    sns.scatterplot(data=poke_cat_df,
                    x="PC 1", y="PC 2", hue="Type 1")
    plt.show()

    # Use the Legendary feature to color the PC 1 vs PC 2 scatterplot
    sns.scatterplot(data=poke_cat_df,
                    x='PC 1', y='PC 2', hue="Legendary")
    plt.show()


def pca_in_a_model_pipeline(df):
    X = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
    y = df["Legendary"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Build the pipeline
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('reducer', PCA(n_components=2)),
        ('classifier', RandomForestClassifier(random_state=0))])

    # Fit the pipeline to the training data
    pipe.fit(X_train, y_train)

    # Score the accuracy on the test set
    accuracy = pipe.score(X_test, y_test)

    # Prints the model accuracy
    print('{0:.1%} test set accuracy with 2 principal components'.format(accuracy))

    # Build the pipeline
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('reducer', PCA(n_components=3)),
        ('classifier', RandomForestClassifier(random_state=0))])

    # Fit the pipeline to the training data
    pipe.fit(X_train, y_train)

    # Score the accuracy on the test set
    accuracy = pipe.score(X_test, y_test)

    # Prints the explained variance ratio and accuracy
    print(pipe.steps[1][1].explained_variance_ratio_)
    print('{0:.1%} test set accuracy with 3 principal components'.format(accuracy))


sns.set()
poke_df = load_pokemon_data()

# understanding_components(poke_df)
# plotting_pca(poke_df)

pca_in_a_model_pipeline(poke_df)
