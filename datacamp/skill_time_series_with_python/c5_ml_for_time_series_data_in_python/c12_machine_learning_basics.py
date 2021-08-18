import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn import linear_model


def classification_example():
    iris = datasets.load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['species'])
    data, targets = train_test_split(df, test_size=0.2)

    # Print the first 5 rows for inspection
    print(data.head())

    # Construct data for the model
    X = data[["petal length (cm)", "petal width (cm)"]]
    y = data[['species']]
    # Fit the model
    model = LinearSVC()
    model.fit(X, y)

    # Create input array
    X_predict = targets[['petal length (cm)', 'petal width (cm)']]

    # Predict with the model
    predictions = model.predict(X_predict)
    print(predictions)

    # Visualize predictions and actual values
    plt.scatter(X_predict['petal length (cm)'], X_predict['petal width (cm)'],
                c=predictions, cmap=plt.cm.coolwarm)
    plt.title("Predicted class values")
    plt.show()


def regression():
    bunch = datasets.load_boston()
    boston = pd.DataFrame(bunch['data'],
                          columns=bunch['feature_names'])
    print(boston.shape)
    # Prepare input and output DataFrames
    X = boston["AGE"].values.reshape(-1, 1)
    y = boston["RM"].values.reshape(-1, 1)
    # Fit the model
    model = linear_model.LinearRegression()
    model.fit(X, y)

    new_inputs = np.array([
        2.9,    3.88080808,    4.86161616,    5.84242424, 6.82323232,    7.8040404,    8.78484848,    9.76565657,
        10.74646465,   11.72727273,   12.70808081,   13.68888889, 14.66969697,   15.65050505,   16.63131313,   17.61212121,
        18.59292929,   19.57373737,   20.55454545,   21.53535354, 22.51616162,   23.4969697,   24.47777778,   25.45858586,
        26.43939394,   27.42020202,   28.4010101,   29.38181818, 30.36262626,   31.34343434,   32.32424242,   33.30505051,
        34.28585859,   35.26666667,   36.24747475,   37.22828283, 38.20909091,   39.18989899,   40.17070707,   41.15151515,
        42.13232323,   43.11313131,   44.09393939,   45.07474747, 46.05555556,   47.03636364,   48.01717172,   48.9979798,
        49.97878788,   50.95959596,   51.94040404,   52.92121212, 53.9020202,   54.88282828,   55.86363636,   56.84444444,
        57.82525253,   58.80606061,   59.78686869,   60.76767677, 61.74848485,   62.72929293,   63.71010101,   64.69090909,
        65.67171717,   66.65252525,   67.63333333,   68.61414141, 69.59494949,   70.57575758,   71.55656566,   72.53737374,
        73.51818182,   74.4989899,   75.47979798,   76.46060606, 77.44141414,   78.42222222,   79.4030303,   80.38383838,
        81.36464646,   82.34545455,   83.32626263,   84.30707071, 85.28787879,   86.26868687,   87.24949495,   88.23030303,
        89.21111111,   90.19191919,   91.17272727,   92.15353535, 93.13434343,   94.11515152,   95.0959596,   96.07676768,
        97.05757576,   98.03838384,   99.01919192,  100.])

    # Generate predictions with the model using those inputs
    predictions = model.predict(new_inputs.reshape(-1, 1))

    # Visualize the inputs and predicted values
    plt.scatter(new_inputs, predictions, color='r', s=3)
    plt.xlabel('inputs')
    plt.ylabel('predictions')
    plt.show()


if __name__ == "__main__":
    sns.set()
    # classification_example()
    regression()
