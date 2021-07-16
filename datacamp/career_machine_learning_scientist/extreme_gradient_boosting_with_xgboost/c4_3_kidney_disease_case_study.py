import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn_pandas import DataFrameMapper
# from sklearn_pandas import CategoricalImputer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score, RandomizedSearchCV
from data import load_kidney_data
from Dictifier import Dictifier

df = load_kidney_data()
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Check number of nulls in each feature column
nulls_per_column = X.isnull().sum()
print(nulls_per_column)

# Create a boolean mask for categorical columns
categorical_feature_mask = X.dtypes == object

# Get list of categorical column names
categorical_columns = X.columns[categorical_feature_mask].tolist()

# Get list of non-categorical column names
non_categorical_columns = X.columns[~categorical_feature_mask].tolist()

# Apply numeric imputer
numeric_imputation_mapper = DataFrameMapper(
    [([numeric_feature], SimpleImputer(strategy="median"))
     for numeric_feature in non_categorical_columns],
    input_df=True,
    df_out=True
)

# Apply categorical imputer
categorical_imputation_mapper = DataFrameMapper(
    [(category_feature, SimpleImputer(strategy="most_frequent"))
     for category_feature in categorical_columns],
    input_df=True,
    df_out=True
)

# Combine the numeric and categorical transformations
numeric_categorical_union = FeatureUnion([
    ("num_mapper", numeric_imputation_mapper),
    ("cat_mapper", categorical_imputation_mapper)
])


# Create full pipeline
pipeline = Pipeline([
    ("featureunion", numeric_categorical_union),
    ("dictifier", Dictifier()), ## problem here
    ("vectorizer", DictVectorizer(sort=False)),
    ("clf", xgb.XGBClassifier(max_depth=3))
])


def kidney_disease_case_study():
    # Perform cross-validation
    cross_val_scores = cross_val_score(pipeline, X, y, scoring="roc_auc", cv=3)
    # Print avg. AUC
    print("3-fold AUC: ", np.mean(cross_val_scores))


def bring_it_all_together():
    # Create the parameter grid
    gbm_param_grid = {
        'clf__learning_rate': np.arange(.05, 1, .05),
        'clf__max_depth': np.arange(3, 10, 1),
        'clf__n_estimators': np.arange(50, 200, 50)
    }

    # Perform RandomizedSearchCV
    randomized_roc_auc = RandomizedSearchCV(estimator=pipeline,
                                            param_distributions=gbm_param_grid,
                                            n_iter=2, scoring='roc_auc', cv=2, verbose=1)

    # Fit the estimator
    randomized_roc_auc.fit(X, y)

    # Compute metrics
    print(randomized_roc_auc.best_score_)
    print(randomized_roc_auc.best_estimator_)
