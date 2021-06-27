import matplotlib.pyplot as plt
from data import load_austin_weather_data_12months, load_seattle_weather_data_12months


def customizing_data_appearance(seattle_weather, austin_weather):
    fig, ax = plt.subplots()

    # Plot Seattle data, setting data appearance
    ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],
            color="b", marker="o", linestyle="--")

    # Plot Austin data, setting data appearance
    ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
            color="r", marker="v", linestyle="--")

    # Call show to display the resulting plot
    plt.show()


def add_label_and_title(seattle_weather, austin_weather):
    fig, ax = plt.subplots()

    ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
    ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

    # Customize the x-axis label
    ax.set_xlabel("Time (months)")

    # Customize the y-axis label
    ax.set_ylabel("Precipitation (inches)")

    # Add the title
    ax.set_title("Weather patterns in Austin and Seattle")

    # Display the figure
    plt.show()


seattle_weather = load_seattle_weather_data_12months()
austin_weather = load_austin_weather_data_12months()
#customizing_data_appearance(seattle_weather, austin_weather)
add_label_and_title(seattle_weather, austin_weather)
