import pandas as pd
import numpy as np
from keras.utils import to_categorical


def load_titanic_data():
    df = pd.read_csv('data/titanic_all_numeric.csv')
    df['age_was_missing'] = df['age_was_missing'].astype(int)
    target = to_categorical(df['survived'])
    predictors = df.drop(['survived'], axis=1).values
    # print(stats.describe(predictors))
    # print(stats.describe(target))
    return predictors, target
