import matplotlib.pyplot as plt
from data import load_austin_weather_data_12months, load_seattle_weather_data_12months


def create_small_multiples(seattle_weather, austin_weather):
    # Create a Figure and an array of subplots with 2 rows and 2 columns
    fig, ax = plt.subplots(2, 2)

    # Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
    ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

    # In the top right (index 0,1), plot month and Seattle temperatures
    ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

    # In the bottom left (1, 0) plot month and Austin precipitations
    ax[1, 0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

    # In the bottom right (1, 1) plot month and Austin temperatures
    ax[1, 1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
    plt.show()


def small_multiples_with_shared_yaxis(seattle_weather, austin_weather):
    # Create a figure and an array of axes: 2 rows, 1 column with shared y axis
    fig, ax = plt.subplots(2, 1, sharey=True)

    # Plot Seattle precipitation data in the top axes
    ax[0].plot(seattle_weather["MONTH"],
               seattle_weather["MLY-PRCP-NORMAL"], color="b")
    ax[0].plot(seattle_weather["MONTH"],
               seattle_weather["MLY-PRCP-25PCTL"], color="b", linestyle="--")
    ax[0].plot(seattle_weather["MONTH"],
               seattle_weather["MLY-PRCP-75PCTL"], color="b", linestyle="--")

    # Plot Austin precipitation data in the bottom axes
    ax[1].plot(austin_weather["MONTH"],
               austin_weather["MLY-PRCP-NORMAL"], color="r")
    ax[1].plot(austin_weather["MONTH"],
               austin_weather["MLY-PRCP-25PCTL"], color="r", linestyle="--")
    ax[1].plot(austin_weather["MONTH"],
               austin_weather["MLY-PRCP-75PCTL"], color="r", linestyle="--")

    plt.show()


seattle_weather = load_seattle_weather_data_12months()
austin_weather = load_austin_weather_data_12months()
#create_small_multiples(seattle_weather, austin_weather)
small_multiples_with_shared_yaxis(seattle_weather, austin_weather)
