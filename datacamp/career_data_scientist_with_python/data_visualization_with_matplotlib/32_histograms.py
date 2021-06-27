import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_mens_rowing, load_mens_gymnastics
from util import plot_timeseries


def step_histogram(mens_rowing, mens_gymnastics):
    fig, ax = plt.subplots()

    # Plot a histogram of "Weight" for mens_rowing
    ax.hist(mens_rowing["Weight"], label="Rowing", histtype="step", bins=5)

    # Compare to histogram of "Weight" for mens_gymnastics
    ax.hist(mens_gymnastics["Weight"],
            label="Gymnastics", histtype="step", bins=5)

    ax.set_xlabel("Weight (kg)")
    ax.set_ylabel("# of observations")

    # Add the legend and show the Figure
    ax.legend()
    plt.show()


mens_rowing = load_mens_rowing()
mens_gymnastics = load_mens_gymnastics()
step_histogram(mens_rowing, mens_gymnastics)
