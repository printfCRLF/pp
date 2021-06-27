import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_climate_change_data
from util import plot_timeseries


def using_a_plot_function(climate_change):
    fig, ax = plt.subplots()
    # Plot the CO2 levels time-series in blue
    plot_timeseries(ax, climate_change.index,
                    climate_change["co2"], "blue", "Time (years)", "CO2 levels")
    # Create a twin Axes object that shares the x-axis
    ax2 = ax.twinx()
    # Plot the relative temperature data in red
    plot_timeseries(ax2, climate_change.index,
                    climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")
    plt.show()


sns.set()
climate_change = load_climate_change_data()
using_a_plot_function(climate_change)
