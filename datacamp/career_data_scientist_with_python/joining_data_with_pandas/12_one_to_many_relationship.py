from data import load_licenses, load_bussiness_owners


def one_to_many_merge(licenses, biz_owners):
    # Merge the licenses and biz_owners table on account
    licenses_owners = licenses.merge(biz_owners, on="account")

    # Group the results by title then count the number of accounts
    counted_df = licenses_owners.groupby("title").agg({'account': 'count'})

    # Sort the counted_df in desending order
    sorted_df = counted_df.sort_values("account", ascending=False)

    # Use .head() method to print the first few rows of sorted_df
    print(sorted_df.head())


licenses = load_licenses()
biz_owners = load_bussiness_owners()
one_to_many_merge(licenses, biz_owners)
