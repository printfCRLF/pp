import pandas as pd

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_austin_weather_data():
    return pd.read_csv("data/austin_weather.csv")


def load_austin_weather_data_12months():
    df = load_austin_weather_data()
    df["MONTH"] = MONTHS
    return df


def load_seattle_weather_data():
    return pd.read_csv("data/seattle_weather.csv")


def load_seattle_weather_data_12months():
    df = load_seattle_weather_data()
    df = df[df["STATION"] == "USW00094290"]
    df["MONTH"] = MONTHS
    return df


def load_climate_change_data():
    return pd.read_csv("data/climate_change.csv", parse_dates=["date"], index_col="date")


def load_medals_data():
    return pd.read_csv("data/medals_by_country_2016.csv")


def load_summer_olympics_data():
    return pd.read_csv("data/summer2016.csv")


def load_mens_rowing():
    summer2016 = pd.read_csv("data/summer2016.csv")
    is_men = summer2016["Sex"] == "M"
    is_rowing = summer2016["Sport"] == "Rowing"
    mens_rowing = summer2016[is_men & is_rowing]
    return mens_rowing


def load_mens_gymnastics():
    summer2016 = pd.read_csv("data/summer2016.csv")
    is_men = summer2016["Sex"] == "M"
    is_gymnastics = summer2016["Sport"] == "Gymnastics"
    mens_gymnastics = summer2016[is_men & is_gymnastics]
    return mens_gymnastics
