from data import load_taxi_data, load_wards, load_census
import math


def inner_join(taxi_owners, taxi_veh):
    # Merge the taxi_owners and taxi_veh tables setting a suffix
    taxi_own_veh = taxi_owners.merge(
        taxi_veh, on='vid', suffixes=('_own', '_veh'))

    # Print the value_counts to find the most popular fuel_type
    print(taxi_own_veh['fuel_type'].value_counts())


def inner_join_when_keys_do_not_match():
    wards = load_wards()
    census = load_census()

    # Merge the wards and census tables on the ward column
    wards_census = wards.merge(census, on="ward")
    # Print the shape of wards_census
    print('wards_census table shape:', wards_census.shape)

    wards_altered = wards
    wards_altered["ward"][0] = 61
    # Print the first few rows of the wards_altered table to view the change
    print(wards_altered[['ward']].head())
    # Merge the wards_altered and census tables on the ward column
    wards_altered_census = wards_altered.merge(census, on="ward")
    # Print the shape of wards_altered_census
    print('wards_altered_census table shape:', wards_altered_census.shape)

    census_altered = census
    census_altered["ward"][0] = math.nan
    # Print the first few rows of the census_altered table to view the change
    print(census_altered[['ward']].head())
    # Merge the wards and census_altered tables on the ward column
    wards_census_altered = wards.merge(census_altered, on="ward")

    # Print the shape of wards_census_altered
    print('wards_census_altered table shape:', wards_census_altered.shape)


taxi_owners, taxi_veh = load_taxi_data()
#inner_join(taxi_owners, taxi_veh)
inner_join_when_keys_do_not_match()
