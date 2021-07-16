import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from data import load_ames_housing_data_unprocessed


def a_simple_pipeline_with_xgboost(df):
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    # Fill LotFrontage missing values with 0
    X.LotFrontage = X.LotFrontage.fillna(0)

    # Setup the pipeline steps: steps
    steps = [("ohe_onestep", DictVectorizer(sparse=False)),
             ("xgb_model", xgb.XGBRegressor(max_depth=2, objective="reg:squarederror"))]

    # Create the pipeline: xgb_pipeline
    xgb_pipeline = Pipeline(steps)

    # Cross-validate the model
    cross_val_scores = cross_val_score(xgb_pipeline, X.to_dict(
        "records"), y, cv=10, scoring="neg_mean_squared_error")

    # Print the 10-fold RMSE
    print("10-fold RMSE: ", np.mean(np.sqrt(np.abs(cross_val_scores))))


df = load_ames_housing_data_unprocessed()
a_simple_pipeline_with_xgboost(df)
