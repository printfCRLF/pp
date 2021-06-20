import matplotlib.pyplot as plt
import seaborn as sns
from data import load_avocado_data


def which_avocado_size_is_most_popular(avocados):
    # Look at the first few rows of data
    print(avocados.head())

    # Get the total number of avocados sold of each size
    nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

    # Create a bar plot of the number of avocados sold by size
    nb_sold_by_size.plot(kind="bar")

    # Show the plot
    plt.show()


def change_in_sales_over_time(avocados):
    # Get the total number of avocados sold on each date
    nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

    # Create a line plot of the number of avocados sold by date
    nb_sold_by_date.plot(x="date", y="nb_sold", kind="line")

    # Show the plot
    plt.show()


def supply_and_demand(avocados):
    # Scatter plot of nb_sold vs avg_price with title
    avocados.plot(x="nb_sold", y="avg_price", kind="scatter",
                  title="Number of avocados sold vs. average price")

    # Show the plot
    plt.show()


def price_of_conventional_vs_organic(avocados):
    # Histogram of conventional avg_price
    avocados[avocados["type"] == "conventional"]["avg_price"].hist()

    # Histogram of organic avg_price
    avocados[avocados["type"] == "organic"]["avg_price"].hist()

    # Add a legend
    plt.legend(["conventional", "organic"])

    # Show the plot
    plt.show()


sns.set()
avocados = load_avocado_data()
# which_avocado_size_is_most_popular(avocados)
# change_in_sales_over_time(avocados)
#  qsupply_and_demand(avocados)
price_of_conventional_vs_organic(avocados)
