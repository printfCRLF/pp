import pandas as pd
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def examining_traffic_violations(ri):
    print("Count the unique values in 'violation' column")
    print(ri.violation.value_counts(), end="\n\n")

    print("Count the unique values in 'violation' column as proportions")
    print(ri.violation.value_counts(normalize=True), end="\n\n")


def comparing_violations_by_gender(ri):
    # Create a DataFrame of female drivers
    female = ri[ri.driver_gender == "F"]
    # Create a DataFrame of male drivers
    male = ri[ri.driver_gender == "M"]

    print("Compute the violations by female drivers (as proportions)")
    print(female.violation.value_counts(normalize=True), end="\n\n")

    print("Compute the violations by male drivers (as proportions)")
    print(male.violation.value_counts(normalize=True), end="\n\n")


ri = prepare_data_for_following_chapters()
examining_traffic_violations(ri)
comparing_violations_by_gender(ri)
