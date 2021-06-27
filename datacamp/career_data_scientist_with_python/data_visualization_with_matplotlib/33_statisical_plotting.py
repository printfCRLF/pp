import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_mens_rowing, load_mens_gymnastics, \
    load_austin_weather_data_12months, load_seattle_weather_data_12months
from util import plot_timeseries


def adding_error_bars_to_a_bar_chart(mens_rowing, mens_gymnastics):
    fig, ax = plt.subplots()
    # Add a bar for the rowing "Height" column mean/std
    ax.bar("Rowing", mens_rowing["Height"].mean(),
           yerr=mens_rowing["Height"].std())

    # Add a bar for the gymnastics "Height" column mean/std
    ax.bar("Gymnastics", mens_gymnastics["Height"].mean(
    ), yerr=mens_gymnastics["Height"].std())

    # Label the y-axis
    ax.set_ylabel("Height (cm)")
    plt.show()


def adding_error_bars_to_a_plot(seattle_weather, austin_weather):
    fig, ax = plt.subplots()

    # Add Seattle temperature data in each month with error bars
    ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"],
                yerr=seattle_weather["MLY-TAVG-STDDEV"])

    # Add Austin temperature data in each month with error bars
    ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"],
                yerr=austin_weather["MLY-TAVG-STDDEV"])

    # Set the y-axis label
    ax.set_ylabel("Temperature (Fahrenheit)")

    plt.show()


def creating_box_plots(mens_rowing, mens_gymnastics):
    fig, ax = plt.subplots()

    # Add a boxplot for the "Height" column in the DataFrames
    ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

    # Add x-axis tick labels:
    ax.set_xticklabels(["Rowing", "Gymnastics"])

    # Add a y-axis label
    ax.set_ylabel("Height (cm)")

    plt.show()


sns.set()
mens_rowing = load_mens_rowing()
mens_gymnastics = load_mens_gymnastics()
# adding_error_bars_to_a_bar_chart(mens_rowing, mens_gymnastics)

seattle_weather = load_seattle_weather_data_12months()
austin_weather = load_austin_weather_data_12months()
#adding_error_bars_to_a_plot(seattle_weather, austin_weather)

creating_box_plots(mens_rowing, mens_gymnastics)
