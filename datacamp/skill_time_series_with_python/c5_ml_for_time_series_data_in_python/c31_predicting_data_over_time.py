import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score


def introducing_the_dataset():
    df = pd.read_csv("data/prices.csv", parse_dates=["date"], index_col="date")
    mask = df["symbol"].isin(["EBAY", "YHOO"])
    df = df[mask]
    prices = df.pivot_table(values="close", index=df.index, columns="symbol")
    prices = prices["2010": "2013"]
    # Plot the raw values over time
    prices.plot()
    plt.show()

    # Scatterplot with one company per axis
    prices.plot.scatter("EBAY", "YHOO")
    plt.show()

    # Scatterplot with color relating to time
    prices.plot.scatter('EBAY', 'YHOO', c=prices.index,
                        cmap=plt.cm.viridis, colorbar=False)
    plt.show()


def fitting_a_simple_regression_model():
    df = pd.read_csv("data/prices.csv", parse_dates=["date"], index_col="date")
    mask = df["symbol"].isin(["EBAY", "NVDA", "YHOO", "AAPL"])
    df = df[mask]

    all_prices = df.pivot_table(
        values="close", index=df.index, columns="symbol")
    all_prices = all_prices["2010": "2013"]
    all_prices.plot()
    plt.show()

    # Use stock symbols to extract training data
    X = all_prices[["EBAY", "NVDA", "YHOO"]]
    y = all_prices[["AAPL"]]

    # Fit and score the model with cross-validation
    scores = cross_val_score(Ridge(), X, y, cv=3)
    print(scores)

    return X, y


def visualizing_predicted_values(X, y):
    # Split our data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=.8, shuffle=False, random_state=1)

    # Fit our model and generate predictions
    model = Ridge()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    print(score)

    # Visualize our predictions along with the "true" values, and print the score
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(y_test.values, color='k', lw=3)
    ax.plot(predictions, color='r', lw=2)
    ax.legend(["Observed", "Predictions"])
    plt.show()


if __name__ == "__main__":
    sns.set()
    # introducing_the_dataset()
    X, y = fitting_a_simple_regression_model()
    visualizing_predicted_values(X, y)
