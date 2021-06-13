import numpy as np
from sklearn.linear_model import LogisticRegression
import util


def load_data():
    X = np.array([[1.78862847,  0.43650985],
                  [0.09649747, -1.8634927],
                  [-0.2773882, -0.35475898],
                  [-3.08274148,  2.37299932],
                  [-3.04381817,  2.52278197],
                  [-1.31386475,  0.88462238],
                  [-2.11868196,  4.70957306],
                  [-2.94996636,  2.59532259],
                  [-3.54535995,  1.45352268],
                  [0.98236743, -1.10106763],
                  [-1.18504653, -0.2056499],
                  [-1.51385164,  3.23671627],
                  [-4.02378514,  2.2870068],
                  [0.62524497, -0.16051336],
                  [-3.76883635,  2.76996928],
                  [0.74505627,  1.97611078],
                  [-1.24412333, -0.62641691],
                  [-0.80376609, -2.41908317],
                  [-0.92379202, -1.02387576],
                  [1.12397796, -0.13191423]])
    y = np.array([-1, -1, -1,  1,  1, -1,  1,  1,  1, -1, -1,  1,  1, -1,  1, -1, -1,
                  -1, -1, -1])

    return X, y


def changing_the_model_coefficients(X, y):    
    model = LogisticRegression()
    model.fit(X, y)
    model.coef_ = np.array([[-1, 1]])
    model.intercept_ = np.array([-3])

    util.plot_classifier(X, y, model)
    num_err = np.sum(y != model.predict(X))
    print("Number of errors:", num_err)

X, y = load_data()
changing_the_model_coefficients(X, y)
