import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_climate_change_data


def simple_scatter_plot(climate_change):
    fig, ax = plt.subplots()

    # Add data: "co2" on x-axis, "relative_temp" on y-axis
    ax.scatter(climate_change["co2"], climate_change["relative_temp"])

    # Set the x-axis label to "CO2 (ppm)"
    ax.set_xlabel("CO2 (ppm)")

    # Set the y-axis label to "Relative temperature (C)"
    ax.set_ylabel("Relative temperature (C)")

    plt.show()


def encoding_time_by_color(climate_change):
    fig, ax = plt.subplots()

    # Add data: "co2" on x-axis, "relative_temp" on y-axis
    ax.scatter(
        climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

    # Set the x-axis label to "CO2 (ppm)"
    ax.set_xlabel("CO2 (ppm)")

    # Set the y-axis label to "Relative temperature (C)"
    ax.set_ylabel("Relative temperature (C)")

    plt.show()


sns.set()
climate_change = load_climate_change_data()
# simple_scatter_plot(climate_change)
encoding_time_by_color(climate_change)
