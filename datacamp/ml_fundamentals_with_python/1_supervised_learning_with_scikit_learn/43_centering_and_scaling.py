import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.linear_model import ElasticNet
from scipy import stats


def load_wine_data():
    df = pd.read_csv('data/white-wine.csv')
    X = df.drop(columns=['quality']).to_numpy()
    quality = df['quality'].to_numpy()
    y = quality <= 5
    return X, y


def load_mortality_data():
    df = pd.read_csv('data/gm_2008_region.csv')
    X = df.drop(columns=['life', 'Region']).to_numpy()
    y = df['life'].to_numpy()
    return X, y


def centering_and_scaling_your_data(X, _):
    # Print the mean and standard deviation of the unscaled features
    print("Mean of Unscaled Features: {}".format(np.mean(X)))
    print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

    X_scaled = scale(X)
    # Print the mean and standard deviation of the scaled features
    print("Mean of Scaled Features: {}".format(np.mean(X_scaled)))
    print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))


def centering_and_scaling_in_a_pipeline(X, y):
    # Setup the pipeline steps: steps
    steps = [('scaler', StandardScaler()),
             ('knn', KNeighborsClassifier())]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps)

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Fit the pipeline to the training set: knn_scaled
    knn_scaled = pipeline.fit(X_train, y_train)

    # Instantiate and fit a k-NN classifier to the unscaled data
    knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

    # Compute and print metrics
    print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test, y_test)))
    print('Accuracy without Scaling: {}'.format(
        knn_unscaled.score(X_test, y_test)))


def bring_it_all_together_pipeline_for_regression(X, y):
    # Setup the pipeline steps: steps
    steps = [('imputation', SimpleImputer(missing_values=np.nan, strategy='mean')),
             ('scaler', StandardScaler()),
             ('elasticnet', ElasticNet())]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps)

    # Specify the hyperparameter space
    parameters = {'elasticnet__l1_ratio': np.linspace(0, 1, 30)}

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42)

    # Create the GridSearchCV object: gm_cv
    gm_cv = GridSearchCV(pipeline, param_grid=parameters, cv=3)

    # Fit to the training set
    gm_cv.fit(X_train, y_train)

    # Compute and print the metrics
    r2 = gm_cv.score(X_test, y_test)
    print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
    print("Tuned ElasticNet R squared: {}".format(r2))


centering_and_scaling_your_data(*load_wine_data())
centering_and_scaling_in_a_pipeline(*load_wine_data())
bring_it_all_together_pipeline_for_regression(*load_mortality_data())
