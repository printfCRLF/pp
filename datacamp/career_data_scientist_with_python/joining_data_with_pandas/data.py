import pandas as pd


def load_taxi_data():
    taxi_owners = pd.read_pickle("data/taxi_owners.p")
    taxi_veh = pd.read_pickle("data/taxi_vehicles.p")
    return taxi_owners, taxi_veh


def load_wards():
    wards = pd.read_pickle("data/ward.p")
    return wards


def load_census():
    census = pd.read_pickle("data/census.p")
    return census


def load_licenses():
    licenses = pd.read_pickle("data/licenses.p")
    return licenses


def load_bussiness_owners():
    biz_owners = pd.read_pickle("data/business_owners.p")
    return biz_owners


def load_land_use():
    land_use = pd.read_pickle("data/land_use.p")
    return land_use


def load_cta_calendar():
    cal = pd.read_pickle("data/cta_calendar.p")
    return cal


def load_cta_ridership():
    ridership = pd.read_pickle("data/cta_ridership.p")
    return ridership


def load_stations():
    stations = pd.read_pickle("data/stations.p")
    return stations


def load_movies():
    return pd.read_pickle("data/movies.p")


def load_movie_to_genres():
    return pd.read_pickle("data/movie_to_genres.p")


def load_taglines():
    return pd.read_pickle("data/taglines.p")


def load_sequels():
    return pd.read_pickle("data/sequels.p")


def load_crews():
    return pd.read_pickle("data/crews.p")


def load_casts():
    return pd.read_pickle("data/casts.p")


def load_sequels():
    return pd.read_pickle("data/sequels.p")


def load_financials():
    return pd.read_pickle("data/financials.p")


taxi_owners, taxi_veh = load_taxi_data()
