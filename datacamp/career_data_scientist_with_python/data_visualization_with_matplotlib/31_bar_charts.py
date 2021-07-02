import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_medals_data
from util import plot_timeseries


def stacked_barcharts(medals):
    fig, ax = plt.subplots()
    # Add bars for "Gold" with the label "Gold"
    ax.bar(medals.index, medals["Gold"], label="Gold")
    # Stack bars for "Silver" on top with label "Silver"
    ax.bar(medals.index, medals["Silver"],
           bottom=medals["Gold"], label="Silver")
    # Stack bars for "Bronze" on top of that with label "Bronze"
    ax.bar(medals.index, medals["Bronze"],
           bottom=medals["Gold"] + medals["Silver"], label="Bronze")

    # Display the legend
    ax.legend()
    plt.show()


medals = load_medals_data()
stacked_barcharts(medals)