import pandas as pd 
import datetime as dt 

def data_type_constraints(): 
    ride_sharing = pd.read_csv('data/ride_sharing_new.csv')
    print(ride_sharing.info())
    
    print(ride_sharing['user_type'].describe())
    ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')
    assert ride_sharing['user_type_cat'].dtype == 'category'
    print(ride_sharing['user_type_cat'].describe())

    ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')
    ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')
    assert ride_sharing['duration_time'].dtype == 'int'
    print(ride_sharing[['duration', 'duration_trim', 'duration_time']])
    print(ride_sharing['duration_time'].mean())


def data_range_constraints(): 
    ride_sharing = pd.read_csv('data/ride_sharing_new.csv')
    ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')
    ride_sharing.loc[ride_sharing['tire_sizes'] > 27, :] = 27
    ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')
    print(ride_sharing['tire_sizes'].describe())

    ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])
    today = dt.date.today()
    ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today
    print(ride_sharing['ride_dt'].max())

def uniqueness_constraints(): 
    ride_sharing = pd.read_csv('data/ride_sharing_new.csv')
    # Find duplicates
    duplicates = ride_sharing.duplicated('ride_id', keep=False)

    # Sort your duplicated rides
    duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

    # Print relevant columns of duplicated_rides
    print(duplicated_rides[['ride_id','duration','user_birth_year']])

    # Drop complete duplicates from ride_sharing
    ride_dup = ride_sharing.drop_duplicates()

    # Create statistics dictionary for aggregation function
    statistics = {'user_birth_year': 'min', 'duration': 'mean'}

    # Group by ride_id and compute new statistics
    ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

    # Find duplicated values again
    duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
    duplicated_rides = ride_unique[duplicates == True]

    # Assert duplicates are processed
    assert duplicated_rides.shape[0] == 0

#data_type_constraints()
#data_range_constraints()
uniqueness_constraints()