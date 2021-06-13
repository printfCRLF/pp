import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from util import plot_classifier, show_digit


def regularization_and_probabilities():
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

    # Set the regularization strength
    model = LogisticRegression(C=1)
    # Fit and plot
    model.fit(X, y)
    plot_classifier(X, y, model, proba=True)
    # Predict probabilities on training points
    prob = model.predict_proba(X)
    print("Maximum predicted probability", np.max(prob))

    # Set the regularization strength
    model = LogisticRegression(C=0.1)
    # Fit and plot
    model.fit(X, y)
    plot_classifier(X, y, model, proba=True)
    # Predict probabilities on training points
    prob = model.predict_proba(X)
    print("Maximum predicted probability", np.max(prob))


def visualizing_easy_and_difficult_examples():
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    lr = LogisticRegression()
    lr.fit(X,y)

    # Get predicted probabilities
    proba = lr.predict_proba(X)

    # Sort the example indices by their maximum probability
    proba_inds = np.argsort(np.max(proba,axis=1))


    plt.figure(1, figsize=(3, 3))
    
    # # Show the most confident (least ambiguous) digit
    # show_digit(proba_inds[-1], lr)
    plt.imshow(digits.images[proba_inds[-1]], cmap=plt.cm.gray_r, interpolation='nearest')

    # # Show the least confident (most ambiguous) digit
    # show_digit(proba_inds[0], lr)
    plt.imshow(digits.images[proba_inds[0]], cmap=plt.cm.gray_r, interpolation='nearest')


#regularization_and_probabilities()
visualizing_easy_and_difficult_examples()
