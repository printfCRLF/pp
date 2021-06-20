import numpy as np
import pandas as pd
from data import load_sales_data


def dropping_duplciates(sales):
    # Drop duplicate store/type combinations
    store_types = sales.drop_duplicates(subset=["store", "type"])
    print(store_types.head())

    # Drop duplicate store/department combinations
    store_depts = sales.drop_duplicates(subset=["store", "department"])
    print(store_depts.head())

    # Subset the rows where is_holiday is True and drop duplicate dates
    holiday_dates = sales[sales["is_holiday"]].drop_duplicates("date")

    # Print date col of holiday_dates
    print(holiday_dates)

    return store_types, store_depts


def couting_categorical_variables(store_types, store_depts):
    # Count the number of stores of each type
    store_counts = store_types["type"].value_counts()
    print(store_counts)

    # Get the proportion of stores of each type
    store_props = store_types["type"].value_counts(normalize=True)
    print(store_props)

    # Count the number of each department number and sort
    dept_counts_sorted = store_depts["department"].value_counts(
        sort=True, ascending=False)
    print(dept_counts_sorted)

    # Get the proportion of departments of each number and sort
    dept_props_sorted = store_depts["department"].value_counts(
        sort=True, normalize=True, ascending=False)
    print(dept_props_sorted)


sales = load_sales_data()
store_types, store_depts = dropping_duplciates(sales)
couting_categorical_variables(store_types, store_depts)
