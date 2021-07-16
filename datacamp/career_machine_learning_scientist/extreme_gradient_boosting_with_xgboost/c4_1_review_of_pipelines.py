import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from data import load_ames_housing_data_unprocessed


def encoding_categorical_columns1_label_encoder(df):
    # Fill missing values with 0
    df.LotFrontage = df.LotFrontage.fillna(0)
    # Create a boolean mask for categorical columns
    categorical_mask = (df.dtypes == object)
    # Get list of categorical column names
    categorical_columns = df.columns[categorical_mask].tolist()
    # Print the head of the categorical columns
    print(df[categorical_columns].head())

    # Create LabelEncoder object: le
    le = LabelEncoder()

    # Apply LabelEncoder to categorical columns
    df[categorical_columns] = df[categorical_columns].apply(
        lambda x: le.fit_transform(x))

    # Print the head of the LabelEncoded categorical columns
    print(df[categorical_columns].head())

    return df, categorical_mask


def encoding_cateogrical_columns2_one_hot_encoder(df, categorical_mask):
    # 'categorical_features' is deprecated
    # # Create OneHotEncoder: ohe
    # ohe = OneHotEncoder(categorical_features=categorical_mask,  sparse=False)
    # # Apply OneHotEncoder to categorical columns - output is no longer a dataframe: df_encoded
    # df_encoded = ohe.fit_transform(df)

    ct = ColumnTransformer(
        [("Country", OneHotEncoder(), categorical_mask)], remainder='passthrough')
    df_encoded = ct.fit_transform(df)

    # Print first 5 rows of the resulting dataset - again, this will no longer be a pandas dataframe
    print(df_encoded[:5, :])

    # Print the shape of the original DataFrame
    print(df.shape)

    # Print the shape of the transformed array
    print(df_encoded.shape)


def encoding_categorical_columns3_dict_vectorizer(df):
    # Convert df into a dictionary: df_dict
    df_dict = df.to_dict("records")
    # Create the DictVectorizer object: dv
    dv = DictVectorizer(sparse=False)
    # Apply dv on df: df_encoded
    df_encoded = dv.fit_transform(df_dict)
    # Print the resulting first five rows
    print(df_encoded[:5, :])
    # Print the vocabulary
    print(dv.vocabulary_)
    print(df_encoded.shape)
    return df_encoded


def preprocessing_with_a_pipeline(df):
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    # Fill LotFrontage missing values with 0
    X.LotFrontage = X.LotFrontage.fillna(0)

    # Setup the pipeline steps: steps
    steps = [("ohe_onestep", DictVectorizer(sparse=False)),
             ("xgb_model", xgb.XGBRegressor())]

    # Create the pipeline: xgb_pipeline
    xgb_pipeline = Pipeline(steps)

    # Fit the pipeline
    xgb_pipeline.fit(X.to_dict("records"), y)


df = load_ames_housing_data_unprocessed()
# df, categorical_mask = encoding_categorical_columns1_label_encoder(df)
# encoding_cateogrical_columns2_one_hot_encoder(df, categorical_mask)
# encoding_categorical_columns3_dict_vectorizer(df)
preprocessing_with_a_pipeline(df)
