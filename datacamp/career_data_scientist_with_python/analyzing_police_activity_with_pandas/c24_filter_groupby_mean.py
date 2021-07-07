import pandas as pd
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def counting_protective_frisks(ri):
    # Count the 'search_type' values
    print(ri.search_type.value_counts())

    # Check if 'search_type' contains the string 'Protective Frisk'
    ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

    # Check the data type of 'frisk'
    print(ri['frisk'].dtypes)

    # Take the sum of 'frisk'
    print(ri['frisk'].sum())

    return ri


def comparing_frisk_rates_by_gender(ri):
    # Create a DataFrame of stops in which a search was conducted
    searched = ri[ri.search_conducted == True]

    # Calculate the overall frisk rate by taking the mean of 'frisk'
    print(searched.frisk.mean())

    # Calculate the frisk rate for each gender
    print(searched.groupby("driver_gender").frisk.mean())


ri = prepare_data_for_following_chapters()
counting_protective_frisks(ri)
comparing_frisk_rates_by_gender(ri)
