import numpy as np
import pandas as pd
from data import load_sales_data


def percentage_by_store_type(sales):
    # Calc total weekly sales
    sales_all = sales["weekly_sales"].sum()

    # Subset for type A stores, calc total weekly sales
    sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

    # Subset for type B stores, calc total weekly sales
    sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

    # Subset for type C stores, calc total weekly sales
    sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

    # Get proportion for each type
    sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
    print(sales_propn_by_type)


def percentage_by_store_type_groupby(sales):
    # Group by type; calc total weekly sales
    sales_by_type = sales.groupby("type")["weekly_sales"].sum()

    # Get proportion for each type
    sales_propn_by_type = sales_by_type / sum(sales_by_type)
    print(sales_propn_by_type)


def multiple_grouped_summaries(sales):
    # For each store type, aggregate weekly_sales: get min, max, mean, and median
    sales_stats = sales.groupby("type")["weekly_sales"].agg(
        [np.min, np.max, np.mean, np.median])

    # Print sales_stats
    print(sales_stats)

    # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
    unemp_fuel_stats = sales.groupby("type")["unemployment", "fuel_price_usd_per_l"].agg([
        np.min, np.max, np.mean, np.median])

    # Print unemp_fuel_stats
    print(unemp_fuel_stats)


sales = load_sales_data()
# percentage_by_store_type(sales)
# percentage_by_store_type_groupby(sales)
multiple_grouped_summaries(sales)
