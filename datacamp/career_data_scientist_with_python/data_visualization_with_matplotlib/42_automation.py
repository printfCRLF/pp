import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_summer_olympics_data
from util import plot_timeseries


def automate_your_visualization(summer_2016_medals):
    fig, ax = plt.subplots()

    sports_column = summer_2016_medals["Sport"]
    sports = sports_column.unique()

    # Loop over the different sports branches
    for sport in sports:
        # Extract the rows only for this sport
        sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
        # Add a bar for the "Weight" mean with std y error bar
        ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

    ax.set_ylabel("Weight")
    ax.set_xticklabels(sports, rotation=90)

    # Save the figure to file
    plt.show()
    fig.savefig("sports_weights.png")


summer_2016_medals = load_summer_olympics_data()
automate_your_visualization(summer_2016_medals)
