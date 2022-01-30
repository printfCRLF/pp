import datetime as dt
import pandas as pd
from data import load_c1_data
from util import get_date_int


def get_month(x):
    return dt.datetime(x.year, x.month, 1)


def assign_monthly_acquisition_cohort(online):
    online["InvoiceMonth"] = online["InvoiceDate"].apply(get_month)

    grouping = online.groupby("CustomerID")["InvoiceMonth"]
    online["CohortMonth"] = grouping.transform("min")


def calculate_time_offset_in_months(online):
    invoice_year, invoice_month, _ = get_date_int(online, "InvoiceMonth")
    cohort_year, cohort_month, _ = get_date_int(online, "CohortMonth")
    online["CohortIndex"] = (invoice_year - cohort_year) * \
        12 + (invoice_month - cohort_month) + 1


def calculate_retention(online):
    grouping = online.groupby(["CohortMonth", "CohortIndex"])

    # Count the number of unique values per customer ID
    cohort_data = grouping["CustomerID"].apply(pd.Series.nunique).reset_index()

    # Create a pivot
    cohort_counts = cohort_data.pivot(
        index="CohortMonth", columns="CohortIndex", values="CustomerID")

    # Select the first column and store it to cohort_sizes
    cohort_sizes = cohort_counts.iloc[:, 0]

    # Divide the cohort count by cohort sizes along the rows
    retention = cohort_counts.divide(cohort_sizes, axis=0)
    print(retention.head())
    
    return retention


def calculate_retention_explain(online):
    grouping = online.groupby(["CohortMonth", "CohortIndex"])

    # Count the number of unique values per customer ID
    cohort_data = grouping["CustomerID"].apply(pd.Series.nunique).reset_index()
    print()
    print("cohort_data.head()")
    print("CohortMonth \t CohortIndex \t NumOfUnique CustomerID")
    print(cohort_data.head())

    # Create a pivot
    cohort_counts = cohort_data.pivot(
        index="CohortMonth", columns="CohortIndex", values="CustomerID")
    print()
    print("Pivot cohort_data intou cohort_counts")
    print(cohort_counts.head())

    # Select the first column and store it to cohort_sizes
    cohort_sizes = cohort_counts.iloc[:, 0]

    # Divide the cohort count by cohort sizes along the rows
    retention = cohort_counts.divide(cohort_sizes, axis=0)
    print()
    print("retention = acitve customers this month / active customers in the beginning of a cohort period")
    print(retention.head())


def calculate_average_price(online):
    # Create a groupby object and pass the monthly cohort and cohort index as a list
    grouping = online.groupby(["CohortMonth", "CohortIndex"])

    # Calculate the average of the unit price column
    cohort_data = grouping["UnitPrice"].mean()

    # Reset the index of cohort_data
    cohort_data = cohort_data.reset_index()

    # Create a pivot
    average_price = cohort_data.pivot(
        index="CohortMonth", columns="CohortIndex", values="UnitPrice")
    print("average_price")
    print(average_price.round(1))


if __name__ == "__main__":
    online = load_c1_data()
    assign_monthly_acquisition_cohort(online)
    calculate_time_offset_in_months(online)
    # calculate_retention(online)
    # calculate_retention_explain(online)
    calculate_average_price(online)
