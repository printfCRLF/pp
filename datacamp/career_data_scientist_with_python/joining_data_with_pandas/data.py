import pandas as pd


def load_taxi_data():
    taxi_owners = pd.read_pickle("data/chicago/taxi_owners.p")
    taxi_veh = pd.read_pickle("data/chicago/taxi_vehicles.p")
    return taxi_owners, taxi_veh


def load_wards():
    wards = pd.read_pickle("data/chicago/ward.p")
    return wards


def load_census():
    census = pd.read_pickle("data/chicago/census.p")
    return census


def load_licenses():
    licenses = pd.read_pickle("data/chicago/licenses.p")
    return licenses


def load_bussiness_owners():
    biz_owners = pd.read_pickle("data/chicago/business_owners.p")
    return biz_owners


def load_land_use():
    land_use = pd.read_pickle("data/chicago/land_use.p")
    return land_use


def load_cta_calendar():
    cal = pd.read_pickle("data/cta/cta_calendar.p")
    return cal


def load_cta_ridership():
    ridership = pd.read_pickle("data/cta/cta_ridership.p")
    return ridership


def load_stations():
    stations = pd.read_pickle("data/cta/stations.p")
    return stations


def load_movies():
    return pd.read_pickle("data/movie/movies.p")


def load_movie_to_genres():
    return pd.read_pickle("data/movie/movie_to_genres.p")


def load_taglines():
    return pd.read_pickle("data/movie/taglines.p")


def load_sequels():
    return pd.read_pickle("data/movie/sequels.p")


def load_crews():
    return pd.read_pickle("data/movie/crews.p")


def load_casts():
    return pd.read_pickle("data/movie/casts.p")


def load_sequels():
    return pd.read_pickle("data/movie/sequels.p")


def load_financials():
    return pd.read_pickle("data/movie/financials.p")


def load_sp500():
    return pd.read_csv("data/economy/S&P500.xls")


def load_gdp():
    return pd.read_csv("data/economy/WorldBank_GDP.xls")


def load_population():
    return pd.read_csv("data/economy/WorldBank_POP.xls")
