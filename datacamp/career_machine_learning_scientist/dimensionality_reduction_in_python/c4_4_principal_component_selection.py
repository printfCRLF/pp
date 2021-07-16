import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from data import load_ansur_ii_female_data
from util import plot_digits


def selecting_portion_of_variance_to_keep(ansur_df):
    # Pipe a scaler to PCA selecting 80% of the variance
    pipe = Pipeline([('scaler', StandardScaler()),
                    ('reducer', PCA(n_components=0.8))])
    # Fit the pipe to the data
    pipe.fit(ansur_df)
    print('{} components selected'.format(len(pipe.steps[1][1].components_)))

    # Let PCA select 90% of the variance
    pipe = Pipeline([('scaler', StandardScaler()),
                    ('reducer', PCA(n_components=0.9))])
    # Fit the pipe to the data
    pipe.fit(ansur_df)
    print('{} components selected'.format(len(pipe.steps[1][1].components_)))


def selecting_number_of_components_with_elbow_plot(ansur_df):
    # Pipeline a scaler and pca selecting 10 components
    pipe = Pipeline([('scaler', StandardScaler()),
                    ('reducer', PCA(n_components=10))])

    # Fit the pipe to the data
    pipe.fit(ansur_df)

    # Plot the explained variance ratio
    plt.plot(pipe.steps[1][1].explained_variance_ratio_)

    plt.xlabel('Principal component index')
    plt.ylabel('Explained variance ratio')
    plt.show()


def pca_for_image_compression(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("reducer", PCA(n_components=32))
    ])
    # Plot the MNIST sample data
    plot_digits(X_test)

    # Transform the input data to principal components
    pc = pipe.fit_transform(X_test)

    # Prints the number of features per dataset
    print("X_test has {} features".format(X_test.shape[1]))
    print("pc has {} features".format(pc.shape[1]))

    # Inverse transform the components to original feature space
    X_rebuilt = pipe.inverse_transform(pc)

    # Prints the number of features
    print("X_rebuilt has {} features".format(X_rebuilt.shape[1]))

    # Plot the reconstructed data
    plot_digits(X_rebuilt)


sns.set()
# ansur_df = load_ansur_ii_female_data()
# non_numeric = ['Branch', 'Gender', 'Component', "weight_kg",
#                "stature_m", "BMI", "BMI_class", "Height_class"]
# ansur_df = ansur_df.drop(non_numeric, axis=1)
# selecting_portion_of_variance_to_keep(ansur_df)

# selecting_number_of_components_with_elbow_plot(ansur_df)


X, y = load_digits(return_X_y=True)
pca_for_image_compression(X, y)
