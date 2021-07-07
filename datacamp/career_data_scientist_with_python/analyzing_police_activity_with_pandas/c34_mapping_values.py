import pandas as pd
import matplotlib.pyplot as plt
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def converting_stop_durations_to_numbers(ri):
    # Print the unique values in 'stop_duration'
    print(ri.stop_duration.unique())

    # Create a dictionary that maps strings to integers
    mapping = {'0-15 Min': 8,
               '16-30 Min': 23,
               '30+ Min': 45}

    # Convert the 'stop_duration' strings to integers using the 'mapping'
    ri['stop_minutes'] = ri.stop_duration.map(mapping)

    # Print the unique values in 'stop_minutes'
    print(ri['stop_minutes'].unique())

    # Calculate the mean 'stop_minutes' for each value in 'violation_raw'
    print(ri.groupby("violation_raw").stop_minutes.mean())

    # Save the resulting Series as 'stop_length'
    stop_length = ri.groupby("violation_raw").stop_minutes.mean()

    # Sort 'stop_length' by its values and create a horizontal bar plot
    stop_length.sort_values().plot(kind="barh")

    # Display the plot
    plt.show()


ri = prepare_data_for_following_chapters()
converting_stop_durations_to_numbers(ri)
