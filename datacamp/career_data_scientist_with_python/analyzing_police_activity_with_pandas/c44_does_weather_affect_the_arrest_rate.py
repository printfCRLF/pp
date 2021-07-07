from c43_merging_datasets import merging_datasets


def comparing_arrest_rates_by_weather_rating(ri_weather):
    # Calculate the overall arrest rate
    print(ri_weather.is_arrested.mean())

    # Calculate the arrest rate for each 'rating'
    print(ri_weather.groupby("rating").is_arrested.mean())

    # Calculate the arrest rate for each 'violation' and 'rating'
    print(ri_weather.groupby(["violation", "rating"]).is_arrested.mean())


def selecting_from_multi_indexed_series(ri_weather):
    # Save the output of the groupby operation from the last exercise
    arrest_rate = ri_weather.groupby(
        ['violation', 'rating']).is_arrested.mean()

    # Print the 'arrest_rate' Series
    print(arrest_rate)

    # Print the arrest rate for moving violations in bad weather
    print(arrest_rate.loc["Moving violation", "bad"])

    # Print the arrest rates for speeding violations in all three weather conditions
    print(arrest_rate.loc["Speeding"])

    return arrest_rate


def reshaping_the_arrest_rate_data(arrest_rate):
    # Unstack the 'arrest_rate' Series into a DataFrame
    print(arrest_rate.unstack())

    # Create the same DataFrame using a pivot table
    print(ri_weather.pivot_table(index='violation',
                                 columns='rating', values='is_arrested'))


ri_weather = merging_datasets()
# comparing_arrest_rates_by_weather_rating(ri_weather)
arrest_rate = selecting_from_multi_indexed_series(ri_weather)
reshaping_the_arrest_rate_data(arrest_rate)
