import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def compare_weekly_monthly_annual_ozone_trends():
    # Import and inspect data here
    ozone = pd.read_csv("data/air_quality_data/ozone_nyla.csv",
                        parse_dates=["date"], index_col="date")
    print(ozone.info())

    # Calculate and plot the weekly average ozone trend
    ozone.resample("W").mean().plot()
    plt.show()
    # Calculate and plot the monthly average ozone trend
    ozone.resample("M").mean().plot()
    plt.show()
    # Calculate and plot the annual average ozone trend
    ozone.resample("A").mean().plot()
    plt.show()


def compare_monthly_average_stock_prices_for_facebook_and_google():
    stocks = pd.read_csv("data/stock_data/goog_fb.csv",
                         parse_dates=["date"], index_col="date")
    print(stocks.info())

    # Calculate and plot the monthly averages
    monthly_average = stocks.resample("M").mean()
    monthly_average.plot(subplots=True)
    plt.show()


def compare_quarterly_gdp_growth_rate_and_stock_returns():
    gdp_growth = pd.read_csv("data/stock_data/gdp_growth.csv", parse_dates=[
                             "date"], index_col="date")
    print(gdp_growth.info())

    # Import and inspect djia here
    djia = pd.read_csv("data/stock_data/djia.csv",
                       parse_dates=["date"], index_col="date")
    print(djia.info())

    # Calculate djia quarterly returns here
    djia_quarterly = djia.resample("QS").first()
    djia_quarterly_return = djia_quarterly.pct_change().mul(100)

    # Concatenate, rename and plot djia_quarterly_return and gdp_growth here
    data = pd.concat([gdp_growth, djia_quarterly_return], axis=1)
    data.columns = ["gdp", "djia"]
    data.plot()
    plt.show()


def visualize_monthly_mean_median_and_std_for_sp500():
    sp500 = pd.read_csv("data/stock_data/sp500.csv",
                        parse_dates=["date"], index_col="date")
    print(sp500.info())

    # Calculate daily returns here
    daily_returns = sp500.squeeze().pct_change()

    # Resample and calculate statistics
    stats = daily_returns.resample("M").agg(["mean", "median", "std"])

    # Plot stats here
    stats.plot()
    plt.show()


sns.set()
# compare_weekly_monthly_annual_ozone_trends()
# compare_monthly_average_stock_prices_for_facebook_and_google()
# compare_quarterly_gdp_growth_rate_and_stock_returns()
visualize_monthly_mean_median_and_std_for_sp500()
