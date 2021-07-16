import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class Dictifier(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('in the DictifierTransformer init method: ')

    def fit(self, x, y=None):
        return self

    def transform(self, x):
        return x.to_dict("records")
