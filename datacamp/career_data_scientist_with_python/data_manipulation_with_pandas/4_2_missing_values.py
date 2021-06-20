import matplotlib.pyplot as plt
import seaborn as sns
from data import load_avocado_data


def find_missing_values(avocados_2016):
    # Check individual values for missing values
    print(avocados_2016.isna())
    # Check each column for missing values
    print(avocados_2016.isna().any())
    # Bar plot of missing values by variable
    avocados_2016.isna().sum().plot(kind="bar")
    # Show plot
    plt.show()


def removing_missing_values(avocados_2016):
    # Remove rows with missing values
    avocados_complete = avocados_2016.dropna()

    # Check if any columns contain missing values
    print(avocados_complete.isna().any())


def replacing_missing_values(avocados_2016):
    # From previous step
    cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
    avocados_2016[cols_with_missing].hist()
    plt.show()

    # Fill in missing values with 0
    avocados_filled = avocados_2016.fillna(0)

    # Create histograms of the filled columns
    avocados_filled[cols_with_missing].hist()

    # Show the plot
    plt.show()


sns.set()
avocados = load_avocado_data()
avocados_2016 = avocados[avocados["year"] == 2016]
# TODO avocados_2016 needs to be reworked

# find_missing_values(avocados_2016)
# removing_missing_values(avocados_2016)
replacing_missing_values(avocados_2016)
