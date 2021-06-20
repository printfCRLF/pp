import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold


def label_encoder_example():
    lot_area = [220, 140, 200, 150, 340]
    borough = ['Bronx', 'Manhattan', 'Queens', 'Brooklyn', 'Staten Island']
    sale_price = [150000, 450000, 190000, 240000, 200000]
    column_names = ['LotArea', 'Borough', 'SalePrice']
    housing = pd.DataFrame(
        {'LotArea': lot_area,
         'Borough': borough,
         'SalePrice': sale_price})

    le = LabelEncoder()
    housing['Borough'] = le.fit_transform(housing['Borough'])
    print(housing)
    print(le.inverse_transform(housing['Borough']))


def min_max_scaler_example():
    min_max = MinMaxScaler()
    df_scaled = pd.DataFrame(min_max.fit_transform(df), columns=df.columns)
    print(df_scaled.head())


def logistic_regression_for_class():
    mod = LogisticRegression(fit_intercept=True)
    mod.fit(car_ownership[["income", "children"]], car_ownership["car"])
    print(mod.coef_)


def kfold_example():
    kf = KFold(n_splits=3, shuffle=True)
    segments = kf.split(X)
    for train_index, test_index in segments:
        print("TRAIN:", train_index, "TEST:", test_index)


label_encoder_example()
