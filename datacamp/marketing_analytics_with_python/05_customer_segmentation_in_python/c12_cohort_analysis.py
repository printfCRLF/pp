import datetime as dt
from data import load_c1_data
from util import get_date_int


def get_day(x):
    return dt.datetime(x.year, x.month, x.day)


def assign_daily_acquisition_cohort(online):
    online["InvoiceDay"] = online["InvoiceDate"].apply(get_day)

    grouping = online.groupby("CustomerID")["InvoiceDay"]

    online["CohortDay"] = grouping.transform("min")
    print(online.head())


def assign_daily_acquisition_cohort_explain(online):
    print(f"There are {online.shape[0]} transactions")
    print(f"Number of unique CustomerID: {online['CustomerID'].nunique()}")

    online["InvoiceDay"] = online["InvoiceDate"].apply(get_day)
    grouping = online.groupby("CustomerID")["InvoiceDay"]
    print(f"Grouping by CustomerID results in {len(grouping)} groups")

    print()
    print("First Group")
    for name, group in grouping:
        print("Group name (CustomerID): ", name)
        print("Index \t InvoiceDay")
        print(group)
        break

    online["CohortDay"] = grouping.transform("min")
    print("transform set the min value to all CustomerID, not just the group")
    print(online[online["CustomerID"] == 12747])


def calculate_time_offset_in_days(online):
    # Get the integers for date parts from the `InvoiceDay` column
    invoice_year, invoice_month, invoice_day = get_date_int(
        online, "InvoiceDay")

    # Get the integers for date parts from the `CohortDay` column
    cohort_year, cohort_month, cohort_day = get_date_int(online, "CohortDay")

    # Calculate difference in years
    years_diff = invoice_year - cohort_year

    # Calculate difference in months
    months_diff = invoice_month - cohort_month

    # Calculate difference in days
    days_diff = invoice_day - cohort_day

    # Extract the difference in days from all previous values
    online['CohortIndex'] = years_diff * 365 + months_diff * 30 + days_diff + 1
    print(online.head())


if __name__ == "__main__":
    online = load_c1_data()
    assign_daily_acquisition_cohort(online)
    # assign_daily_acquisition_cohort_help(online)
    calculate_time_offset_in_days(online)
