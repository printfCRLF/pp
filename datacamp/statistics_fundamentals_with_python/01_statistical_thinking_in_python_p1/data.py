from sklearn import datasets
import pandas as pd
import numpy as np


def load_iris_datasets():
    iris = datasets.load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['species'])
    is_setosa = df["species"] == 0
    is_versicolour = df["species"] == 1
    is_virginica = df["species"] == 2
    setosa_petal_length = df[is_setosa]["petal length (cm)"]
    versicolor_petal_length = df[is_versicolour]["petal length (cm)"]
    virginica_petal_length = df[is_virginica]["petal length (cm)"]

    return df, setosa_petal_length, versicolor_petal_length, virginica_petal_length


def load_belmont_data():
    belmont_no_outliers = [148.51, 146.65, 148.52, 150.7, 150.42, 150.88, 151.57, 147.54,
                           149.65, 148.74, 147.86, 148.75, 147.5, 148.26, 149.71, 146.56,
                           151.19, 147.88, 149.16, 148.82, 148.96, 152.02, 146.82, 149.97,
                           146.13, 148.1, 147.2, 146., 146.4, 148.2, 149.8, 147.,
                           147.2, 147.8, 148.2, 149., 149.8, 148.6, 146.8, 149.6,
                           149., 148.2, 149.2, 148., 150.4, 148.8, 147.2, 148.8,
                           149.6, 148.4, 148.4, 150.2, 148.8, 149.2, 149.2, 148.4,
                           150.2, 146.6, 149.8, 149., 150.8, 148.6, 150.2, 149.,
                           148.6, 150.2, 148.2, 149.4, 150.8, 150.2, 152.2, 148.2,
                           149.2, 151., 149.6, 149.6, 149.4, 148.6, 150., 150.6,
                           149.2, 152.6, 152.8, 149.6, 151.6, 152.8, 153.2, 152.4,
                           152.2]
    return belmont_no_outliers
