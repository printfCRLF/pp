import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from c11_introduction_to_course import merging_time_series_with_different_dates


def correlation_of_stocks_and_bonds(stocks_and_bonds):
    # Compute percent change using pct_change()
    returns = stocks_and_bonds.pct_change()

    # Compute correlation using corr()
    correlation = returns["SP500"].corr(returns["US10Y"])
    print("Correlation of stocks and interest rates: ", correlation)

    # Make scatter plot
    plt.scatter(x=returns["SP500"], y=returns["US10Y"])
    plt.show()


def flying_saucers_are_not_correlated_to_flying_markets():
    dji = pd.read_csv("data/financial_data/DJI.csv",
                      parse_dates=["Date"], index_col="Date")
    dji.columns = ["DJI"]
    ufo = pd.read_csv("data/UFO.csv", parse_dates=["Date"], index_col="Date")
    ufo.columns = ["UFO"]
    levels = dji.join(ufo, how="inner")

    # Compute correlation of levels
    correlation1 = levels["DJI"].corr(levels["UFO"])
    print("Correlation of levels: ", correlation1)

    # Compute correlation of percent changes
    changes = levels.pct_change()
    correlation2 = changes["DJI"].corr(changes["UFO"])
    print("Correlation of changes: ", correlation2)

    fig, ax = plt.subplots()
    levels.plot(ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Dow Jones Average / UFO Sightnings")
    ax.legend(["Dow Jones", "UFO Sightings"])
    fig.suptitle("Flying Saucers Aren't Correlated to Flying Markets")
    plt.show()


if __name__ == "__main__":
    sns.set()
    # stocks_and_bonds = merging_time_series_with_different_dates()
    # correlation_of_stocks_and_bonds(stocks_and_bonds)

    flying_saucers_are_not_correlated_to_flying_markets()
