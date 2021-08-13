import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def exploration():
    # Load in the time series
    candy = pd.read_csv('data/candy_production.xls',
                        parse_dates=['date'],
                        index_col='date')

    # Plot and show the time series on axis ax
    fig, ax = plt.subplots()
    candy.plot(ax=ax)
    plt.show()

    return candy


def train_test_split(candy):
    # Split the data into a train and test set
    candy_train = candy.loc[:"2006"]
    candy_test = candy.loc["2007":]

    # Create an axis
    fig, ax = plt.subplots()

    # Plot the train and test sets on the axis ax
    candy_train.plot(ax=ax)
    candy_test.plot(ax=ax)
    plt.show()


if __name__ == "__main__":
    sns.set()
    candy = exploration()
    train_test_split(candy)
