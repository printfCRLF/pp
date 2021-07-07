import pandas as pd
import matplotlib.pyplot as plt
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters
from data import load_weather_data


def plotting_temperature(weather):
    # Describe the temperature columns
    print(weather[["TMIN", "TAVG", "TMAX"]].describe())

    # Create a box plot of the temperature columns
    weather[["TMIN", "TAVG", "TMAX"]].plot(kind='box')

    # Display the plot
    plt.show()


def plotting_temperature_difference(weather):
    # Create a 'TDIFF' column that represents temperature difference
    weather["TDIFF"] = weather["TMAX"] - weather["TMIN"]

    # Describe the 'TDIFF' column
    print(weather["TDIFF"].describe())

    # Create a histogram with 20 bins to visualize 'TDIFF'
    weather["TDIFF"].plot(kind="hist", bins=20)

    # Display the plot
    plt.show()


weather = load_weather_data()
plotting_temperature(weather)
plotting_temperature_difference(weather)
