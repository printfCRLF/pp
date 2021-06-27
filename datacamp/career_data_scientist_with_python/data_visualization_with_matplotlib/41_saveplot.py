import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_climate_change_data
from util import plot_timeseries


def switching_between_styles(seattle_weather, austin_weather):
    # Use the "ggplot" style and create new Figure/Axes
    fig, ax = plt.subplots()
    plt.style.use("ggplot")
    ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
    plt.show()

    # Use the "Solarize_Light2" style and create new Figure/Axes
    fig, ax = plt.subplots()
    plt.style.use("Solarize_Light2")
    ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
    plt.show()


def save_figure():
    fig, ax = plt.subplots()
    fig.set_size_inches([5, 3])
    fig.savefig("my_figure_300dpi.png", dpi=300)
