import matplotlib.pyplot as plt
from data import load_austin_weather_data_12months, load_seattle_weather_data_12months


def create_an_empty_plot():
    # Create a Figure and an Axes with plt.subplots
    fig, ax = plt.subplots()

    # Call the show function to show the result
    plt.show()


def adding_data_to_an_axes_object(seattle_weather, austin_weather):
    # Create a Figure and an Axes with plt.subplots
    fig, ax = plt.subplots()

    # Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
    ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

    # Plot MLY-PRCP-NORMAL from austin_weather against MONTH
    ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

    # Call the show function
    plt.show()


# create_an_empty_plot()

seattle_weather = load_seattle_weather_data_12months()
austin_weather = load_austin_weather_data_12months()
adding_data_to_an_axes_object(seattle_weather, austin_weather)
