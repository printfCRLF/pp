import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_your_time_series_data():
    # Read in the file content in a DataFrame called discoveries
    discoveries = pd.read_csv("data/ch1_discoveries.csv")
    # Display the first five lines of the DataFrame
    print(discoveries.head())

    # Print the data type of each column in discoveries
    print(discoveries.dtypes)
    # Convert the date column to a datestamp type
    discoveries['date'] = pd.to_datetime(discoveries['date'])
    # Print the data type of each column in discoveries, again
    print(discoveries.dtypes)
    discoveries.set_index("date", inplace=True)

    return discoveries


def your_first_plot(discoveries):
    # Set the date column as the index of your DataFrame discoveries
    discoveries = discoveries.set_index("date")
    # Plot the time series in your DataFrame
    ax = discoveries.plot(color="blue")
    # Specify the x-axis label in your plot
    ax.set_xlabel('Date')
    # Specify the y-axis label in your plot
    ax.set_ylabel('Number of great discoveries')
    # Show plot
    plt.show()


def styling_and_labels(discoveries):
    # Use the fivethirtyeight style
    plt.style.use('fivethirtyeight')

    # Plot the time series
    ax1 = discoveries.plot()
    ax1.set_title('FiveThirtyEight Style')
    plt.show()

    # Plot a line chart of the discoveries DataFrame using the specified arguments
    ax = discoveries.plot(color='blue', figsize=(8, 3),
                          linewidth=2, fontsize=6)

    # Specify the title in your plot
    ax.set_title(
        'Number of great inventions and scientific discoveries from 1860 to 1959', fontsize=8)

    # Show plot
    plt.show()


def subset_time_series_data(discoveries):
    # Select the subset of data between 1945 and 1950
    discoveries_subset_1 = discoveries['1945-1-1':'1950-1-1']
    # Plot the time series in your DataFrame as a blue area chart
    ax = discoveries_subset_1.plot(color='blue', fontsize=15)
    # Show plot
    plt.show()


def add_vertical_and_horizontal_markers(discoveries):
    # Plot your the discoveries time series
    ax = discoveries.plot(color='blue', fontsize=6)
    # Add a red vertical line
    ax.axvline(x="1939-01-01", color="red", linestyle='--')
    # Add a green horizontal line
    ax.axhline(y=4, color="green", linestyle='--')
    plt.show()


def add_shaed_regions_to_your_plot(discoveries):
    # Plot your the discoveries time series
    ax = discoveries.plot(color='blue', fontsize=6)
    # Add a vertical red shaded region
    ax.axvspan('1900-01-01', "1915-01-01", color="red", alpha=0.3)
    # Add a horizontal green shaded region
    ax.axhspan(6, 8, color="green", alpha=0.3)
    plt.show()


if __name__ == "__main__":
    sns.set()
    discoveries = load_your_time_series_data()
    # your_first_plot(discoveries)
    # styling_and_labels(discoveries)
    # subset_time_series_data(discoveries)
    # add_vertical_and_horizontal_markers(discoveries)
    add_shaed_regions_to_your_plot(discoveries)
