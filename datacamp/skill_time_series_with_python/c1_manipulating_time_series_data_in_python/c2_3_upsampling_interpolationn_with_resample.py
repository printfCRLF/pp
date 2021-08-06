import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def use_interpolation_to_create_weekly_employment_data():
    monthly = pd.read_csv("data/stock_data/unrate.csv",
                          parse_dates=["DATE"], index_col="DATE")

    # Inspect data here
    print(monthly.info())

    # Create weekly dates
    weekly_dates = pd.date_range(
        start=monthly.index.min(), end=monthly.index.max(), freq="W")

    # Reindex monthly to weekly data
    weekly = monthly.reindex(weekly_dates)

    # Create ffill and interpolated columns
    weekly['ffill'] = weekly.UNRATE.ffill()
    weekly['interpolated'] = weekly.UNRATE.interpolate()

    # Plot weekly
    weekly.plot()
    plt.show()


def interpolate_deb_gdp_and_compare_to_unemployment():
    data = pd.read_csv("data/stock_data/debt_unemployment.csv",
                       parse_dates=["date"], index_col="date")
    print(data.info())

    # Interpolate and inspect here
    interpolated = data.interpolate()
    print(interpolated.info())

    # Plot interpolated data here
    interpolated.plot(secondary_y="Unemployment")
    plt.show()


if __name__ == "__main__":
    sns.set()
    use_interpolation_to_create_weekly_employment_data()
    # interpolate_deb_gdp_and_compare_to_unemployment()
