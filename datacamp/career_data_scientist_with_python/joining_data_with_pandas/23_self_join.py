from data import load_crews


def find_director_and_crews(crews):
    # Merge the crews table to itself
    crews_self_merged = crews.merge(crews, on='id', how='inner',
                                    suffixes=('_dir', '_crew'))

    # Create a boolean index to select the appropriate rows
    boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                      (crews_self_merged['job_crew'] != 'Director'))
    direct_crews = crews_self_merged[boolean_filter]

    # Print the first few rows of direct_crews
    print(direct_crews.head())


crews = load_crews()
find_director_and_crews(crews)
