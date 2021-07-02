import numpy as np
import pandas as pd
from data import load_sales_data


def mean_and_median(sales):
    # Print the head of the sales DataFrame
    print(sales.head())
    # Print the info about the sales DataFrame
    print(sales.info())
    # Print the mean of weekly_sales
    print(sales["weekly_sales"].mean())
    # Print the median of weekly_sales
    print(sales["weekly_sales"].median())


def summarizing_dates(sales):
    # Print the maximum of the date column
    print(sales["date"].max())

    # Print the minimum of the date column
    print(sales["date"].min())


def aggregate_on_columns_using_custom_functions(sales):
    # A custom IQR function
    def iqr(column):
        return column.quantile(0.75) - column.quantile(0.25)

    # Print IQR of the temperature_c column
    print(sales["temperature_c"].agg(iqr))


def cumulative_statistics(sales):
    department1 = sales["department"] == 1
    store1 = sales["store"] == 1
    sales_1_1 = sales[department1 & store1]
    # Sort sales_1_1 by date
    sales_1_1 = sales_1_1.sort_values("date")

    # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
    sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

    # Get the cumulative max of weekly_sales, add as cum_max_sales col
    sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

    # See the columns you calculated
    print(sales_1_1[["date", "weekly_sales",
          "cum_weekly_sales", "cum_max_sales"]])


sales = load_sales_data()
# mean_and_median(sales)
# summarizing_dates(sales)
# aggregate_on_columns_using_custom_functions(sales)
cumulative_statistics(sales)