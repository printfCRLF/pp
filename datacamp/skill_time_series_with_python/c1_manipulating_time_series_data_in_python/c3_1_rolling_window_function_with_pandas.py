import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def rolling_average_air_quanlity():
    data = pd.read_csv("data/air_quality_data/ozone_nyc.csv",
                       parse_dates=["date"], index_col="date")
    print(data.info())

    # Calculate 90d and 360d rolling mean for the last price
    data['90D'] = data["Ozone"].rolling(window="90D").mean()
    data['360D'] = data["Ozone"].rolling(window="360D").mean()

    # Plot data
    data.loc["2010":].plot(title="New York City")
    plt.show()


def rolling_median_std():
    data = pd.read_csv("data/air_quality_data/ozone_nyc.csv",
                       parse_dates=["date"], index_col="date").dropna()

    # Calculate the rolling mean and std here
    rolling_stats = data.Ozone.rolling(360).agg(['mean', 'std'])

    # Join rolling_stats with ozone data
    stats = data.join(rolling_stats)

    # Plot stats
    stats.plot(subplots=True)
    plt.show()


def rolling_quantiles():
    data = pd.read_csv("data/air_quality_data/ozone_nyc.csv",
                       parse_dates=["date"], index_col="date")
    # Resample, interpolate and inspect ozone data here
    data = data.resample("D").interpolate()
    print(data.info())

    # Create the rolling window
    rolling = data.rolling(360)["Ozone"]

    # Insert the rolling quantiles to the monthly returns
    data['q10'] = rolling.quantile(0.1).to_frame("q10")
    data['q50'] = rolling.quantile(0.5).to_frame("q50")
    data['q90'] = rolling.quantile(0.9).to_frame("q90")

    # Plot the data
    data.plot()
    plt.show()


sns.set()
# rolling_average_air_quanlity()
# rolling_median_std()
rolling_quantiles()
