import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def load_voting_data():
    df = pd.read_csv('data/house-votes-84.csv')
    columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite', 'aid', 'missile',
               'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']
    df.columns = columns
    df[df == 'y'] = 1
    df[df == 'n'] = 0
    df[df == '?'] = np.nan
    df = df.fillna(df.mode().iloc[0])

    new = [0.696469,  0.286139,  0.226851,  0.551315,  0.719469,  0.423106,  0.980764,   0.68483,
           0.480932,  0.392118,  0.343178,  0.72905,  0.438572,  0.059678, 0.398044, 0.737995]
    X_new = pd.DataFrame(new)
    X_new = X_new.transpose()
    return df, X_new


def k_NearestNeighbors(df, X_new):
    y = df['party'].values
    X = df.drop('party', axis=1).values
    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(X, y)
    y_pred = knn.predict(X)
    new_prediction = knn.predict(X_new)
    print(new_prediction)

k_NearestNeighbors(*load_voting_data())
