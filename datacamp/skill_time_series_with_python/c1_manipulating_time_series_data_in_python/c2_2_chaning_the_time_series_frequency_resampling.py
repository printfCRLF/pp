import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def convert_monthly_to_weekly_data():
    # Set start and end dates
    start = '2016-1-1'
    end = '2016-2-29'

    # Create monthly_dates here
    monthly_dates = pd.date_range(start=start, end=end, freq="M")

    # Create and print monthly here
    monthly = pd.Series(data=[1, 2], index=monthly_dates)
    print(monthly)

    # Create weekly_dates here
    weekly_dates = pd.date_range(start=start, end=end, freq="W")

    # Print monthly, reindexed using weekly_dates
    print(monthly.reindex(weekly_dates))
    print(monthly.reindex(weekly_dates, method="bfill"))
    print(monthly.reindex(weekly_dates, method="ffill"))


def create_weekly_from_monthly_unemployment_data():
    data = pd.read_csv("data/stock_data/unrate_2000.csv",
                       parse_dates=["date"], index_col="date")

    # Show first five rows of weekly series
    print(data.asfreq("W").head())

    # Show first five rows of weekly series with bfill option
    print(data.asfreq("W", method="bfill").head())

    # Create weekly series with ffill option and show first five rows
    weekly_ffill = data.asfreq("W", method="ffill")
    print(weekly_ffill.head())

    # Plot weekly_fill starting 2015 here
    weekly_ffill.loc["2015":].plot()
    plt.show()


sns.set()
convert_monthly_to_weekly_data()
create_weekly_from_monthly_unemployment_data()
