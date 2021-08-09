import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics import tsaplots


def load_multiple_time_series():
    # Read in meat DataFrame
    meat = pd.read_csv("data/ch4_meat.csv")
    # Review the first five lines of the meat DataFrame
    print(meat.head(5))
    # Convert the date column to a datestamp type
    meat['date'] = pd.to_datetime(meat['date'])
    # Set the date column as the index of your DataFrame meat
    meat = meat.set_index("date")
    # Print the summary statistics of the DataFrame
    print(meat.describe())

    return meat


def visualize_multiple_time_series(meat):
    # Plot time series dataset
    ax = meat.plot(linewidth=2, fontsize=12)
    # Additional customizations
    ax.set_xlabel('Date')
    ax.legend(fontsize=15)
    # Show plot
    plt.show()

    # Plot an area chart
    ax = meat.plot.area(fontsize=12)
    # Additional customizations
    ax.set_xlabel('Date')
    ax.legend(fontsize=15)
    # Show plot
    plt.show()


if __name__ == "__main__":
    sns.set()
    meat = load_multiple_time_series()
    visualize_multiple_time_series(meat)
