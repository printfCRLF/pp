import pandas as pd
import matplotlib.pyplot as plt
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def calculating_and_plotting_the_hourly_arrest_rate(ri):
    # Calculate the overall arrest rate
    print(ri.is_arrested.mean())

    # Calculate the hourly arrest rate
    print(ri.groupby(ri.index.hour).is_arrested.mean())

    # Save the hourly arrest rate
    hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()

    # Create a line plot of 'hourly_arrest_rate'
    hourly_arrest_rate.plot()

    # Add the xlabel, ylabel, and title
    plt.xlabel("Hour")
    plt.ylabel("Arrest Rate")
    plt.title("Arrest Rate by Time of Day")

    # Display the plot
    plt.show()


ri = prepare_data_for_following_chapters()
calculating_and_plotting_the_hourly_arrest_rate(ri)
