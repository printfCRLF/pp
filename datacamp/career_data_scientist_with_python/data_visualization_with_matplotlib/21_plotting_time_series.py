import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_climate_change_data


def plotting_time_series_data(climate_change):
    fig, ax = plt.subplots()
    # Add the time-series for "relative_temp" to the plot
    ax.plot(climate_change.index, climate_change["relative_temp"])
    # Set the x-axis label
    ax.set_xlabel("Time")
    # Set the y-axis label
    ax.set_ylabel("Relative temperature (Celsius)")
    # Show the figure
    plt.show()


def using_time_index_to_zoom_in(climate_change):
    # Use plt.subplots to create fig and ax
    fig, ax = plt.subplots()

    # Create variable seventies with data from "1970-01-01" to "1979-12-31"
    seventies = climate_change["1970-01-01":"1979-12-31"]

    # Add the time-series for "co2" data from seventies to the plot
    ax.plot(seventies.index, seventies["co2"])

    # Show the figure
    plt.show()


sns.set()
climate_change = load_climate_change_data()
# plotting_time_series_data(climate_change)
using_time_index_to_zoom_in(climate_change)
