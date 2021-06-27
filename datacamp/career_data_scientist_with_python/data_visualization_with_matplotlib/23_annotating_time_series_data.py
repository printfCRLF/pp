import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_climate_change_data
from util import plot_timeseries


def annotating_a_plot_time_series_data(climate_change):
    fig, ax = plt.subplots()
    # Plot the relative temperature data
    ax.plot(climate_change.index, climate_change["relative_temp"])
    # Annotate the date at which temperatures exceeded 1 degree
    ax.annotate(">1 degree", (pd.Timestamp("2015-10-06"), 1))
    plt.show()


def putting_it_all_together(climate_change):
    fig, ax = plt.subplots()

    # Plot the CO2 levels time-series in blue
    plot_timeseries(ax, climate_change.index,
                    climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

    # Create an Axes object that shares the x-axis
    ax2 = ax.twinx()

    # Plot the relative temperature data in red
    plot_timeseries(ax2, climate_change.index,
                    climate_change["relative_temp"], 'red', "Time (years)", "Relative temp (Celsius)")

    # Annotate point with relative temperature >1 degree
    ax2.annotate(">1 degree", xy=(pd.Timestamp("2015-10-06"), 1), xytext=(pd.Timestamp("2008-10-06"), -0.2),
                 arrowprops={"arrowstyle": "->", "color": "gray"})

    plt.show()


sns.set()
climate_change = load_climate_change_data()
# annotating_a_plot_time_series_data(climate_change)
putting_it_all_together(climate_change)
