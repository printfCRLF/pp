import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics import tsaplots
import statsmodels.api as sm


def visualize_airlinnne_dataset(airline):
    # Plot the time series in your dataframe
    ax = airline.plot(color="blue", fontsize=12)

    # Add a red vertical line at the date 1955-12-01
    ax.axvline('1955-12-01', color='red', linestyle='--')

    # Specify the labels in your plot
    ax.set_xlabel('Date', fontsize=12)
    ax.set_title('Number of Monthly Airline Passengers', fontsize=12)
    plt.show()


def analyze_the_airlinne_dataset(airline):
    # Get month for each dates from the index of airline
    index_month = airline.index.month
    # Compute the mean number of passengers for each month of the year
    mean_airline_by_month = airline.groupby(index_month).mean()
    # Plot the mean number of passengers for each month of the year
    mean_airline_by_month.plot()
    plt.legend(fontsize=20)
    plt.show()


def time_series_decomposition(airline):
    # Perform time series decompositon
    decomposition = sm.tsa.seasonal_decompose(airline)

    # Extract the trend and seasonal components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    airline_decomposed = pd.DataFrame(
        {"trend": trend, "seasonal": seasonal}, index=airline.index)

    # Print the first 5 rows of airline_decomposed
    print(airline_decomposed.head())

    # Plot the values of the airline_decomposed DataFrame
    ax = airline_decomposed.plot(figsize=(12, 6), fontsize=15)

    # Specify axis labels
    ax.set_xlabel('Date', fontsize=15)
    plt.legend(fontsize=15)
    plt.show()


if __name__ == "__main__":
    sns.set()
    airline = pd.read_csv("data/ch3_airline_passengers.csv",
                          parse_dates=["Month"], index_col="Month")
    airline.fillna(method="bfill", inplace=True)
    # visualize_airlinnne_dataset(airline)
    # analyze_the_airlinne_dataset(airline)
    time_series_decomposition(airline)
