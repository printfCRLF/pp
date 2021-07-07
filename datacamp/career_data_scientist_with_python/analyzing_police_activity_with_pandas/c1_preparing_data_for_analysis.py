import pandas as pd
from data import load_police_data


def examing_data_sets(ri):
    # Examine the head of the DataFrame
    print(ri.head())

    # Count the number of missing values in each column
    print(ri.isnull().sum())


def dropping_columns(ri):
    # Examine the shape of the DataFrame
    print(ri.shape)

    # Drop the 'county_name' and 'state' columns
    ri.drop(["county_name", "state"], axis='columns', inplace=True)

    # Examine the shape of the DataFrame (again)
    print(ri.shape)


def dropping_rows(ri):
    # Count the number of missing values in each column
    print(ri.isnull().sum())

    # Drop all rows that are missing 'driver_gender'
    ri.dropna(subset=["driver_gender"], inplace=True)

    # Count the number of missing values in each column (again)
    print(ri.isnull().sum())

    # Examine the shape of the DataFrame
    print(ri.shape)


def fixing_data_types(ri):
    # Examine the head of the 'is_arrested' column
    print(ri.is_arrested.dtype)

    # Change the data type of 'is_arrested' to 'bool'
    ri['is_arrested'] = ri.is_arrested.astype("bool")

    # Check the data type of 'is_arrested'
    print(ri.is_arrested.dtype)


def combine_datetime_and_create_index(ri):
    # Concatenate 'stop_date' and 'stop_time' (separated by a space)
    combined = ri.stop_date.str.cat(ri.stop_time, sep=" ")

    # Convert 'combined' to datetime format
    ri['stop_datetime'] = pd.to_datetime(combined)

    # Examine the data types of the DataFrame
    print(ri.dtypes)

    # Set 'stop_datetime' as the index
    ri.set_index("stop_datetime", inplace=True)

    # Examine the index
    print(ri.index)

    # Examine the columns
    print(ri.columns)

    return ri


def prepare_data_for_following_chapters():
    # ri stand for Rhode Island
    ri = load_police_data()
    # examing_data_sets(ri)
    dropping_columns(ri)
    dropping_rows(ri)
    fixing_data_types(ri)
    return combine_datetime_and_create_index(ri)
