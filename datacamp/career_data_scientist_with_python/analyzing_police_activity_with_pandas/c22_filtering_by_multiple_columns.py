import pandas as pd
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def comparing_speeding_outcomes_by_gender(ri):
    # Create a DataFrame of female drivers stopped for speeding
    female_and_speeding = ri[(ri.driver_gender == "F")
                             & (ri.violation == "Speeding")]
    # Create a DataFrame of male drivers stopped for speeding
    male_and_speeding = ri[(ri.driver_gender == "M") &
                           (ri.violation == "Speeding")]

    print("Compute the stop outcomes for female drivers (as proportions)")
    print(female_and_speeding.stop_outcome.value_counts(
        normalize=True), end="\n\n")

    print("Compute the stop outcomes for male drivers (as proportions)")
    print(male_and_speeding.stop_outcome.value_counts(normalize=True), end="\n\n")


ri = prepare_data_for_following_chapters()
comparing_speeding_outcomes_by_gender(ri)
