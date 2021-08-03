from numpy.random import normal, seed, choice
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def annual_return_correlations_among_several_stocks():
    data = pd.read_csv("data/stock_data/5_stocks.csv",
                       parse_dates=["Date"], index_col="Date")
    print(data.info())

    # Calculate year-end prices here
    annual_prices = data.resample("A").last()
    # Calculate annual returns here
    annual_returns = annual_prices.pct_change()
    # Calculate and print the correlation matrix here
    correlations = annual_returns.corr()
    print(correlations)

    # Visualize the correlations as heatmap here
    sns.heatmap(correlations, annot=True)
    plt.show()


annual_return_correlations_among_several_stocks()
