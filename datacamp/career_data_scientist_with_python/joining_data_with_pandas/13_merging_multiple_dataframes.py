from data import load_cta_calendar, load_cta_ridership, load_stations, \
    load_land_use, load_census, load_licenses


def total_riders_in_a_month(ridership, cal, stations):
    # Merge the ridership, cal, and stations tables
    ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
        .merge(stations, on='station_id')

    # Create a filter to filter ridership_cal_stations
    filter_criteria = ((ridership_cal_stations['month'] == 7)
                       & (ridership_cal_stations['day_type'] == "Weekday")
                       & (ridership_cal_stations['station_name'] == "Wilson"))

    # Use .loc and the filter to select for rides
    print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())


def start_my_business(land_use, census, licenses):
    # Merge land_use and census and merge result with licenses including suffixes
    land_cen_lic = land_use.merge(census, on='ward') \
        .merge(licenses, on='ward', suffixes=('_cen', '_lic'))

    # Group by ward, pop_2010, and vacant, then count the # of accounts
    pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'],
                                       as_index=False).agg({'account': 'count'})

    # Sort pop_vac_lic and print the results
    sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant", "account", "pop_2010"],
                                                 ascending=[False, True, True])

    # Print the top few rows of sorted_pop_vac_lic
    print(sorted_pop_vac_lic.head())


ridership = load_cta_ridership()
cal = load_cta_calendar()
stations = load_stations()
total_riders_in_a_month(ridership, cal, stations)


land_use = load_land_use()
census = load_census()
licenses = load_licenses()
start_my_business(land_use, census, licenses)
