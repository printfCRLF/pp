import pandas as pd
import matplotlib.pyplot as plt


def concatenation_basics(tracks_master, tracks_ride, tracks_st):
    # Concatenate the tracks, show only columns names that are in all tables
    tracks_from_albums = pd.concat([tracks_master,  tracks_ride, tracks_st],
                                   join="inner",
                                   sort=True)
    print(tracks_from_albums)

    # Concatenate the tracks so the index goes from 0 to n-1
    tracks_from_albums = pd.concat([tracks_master,  tracks_ride, tracks_st],
                                   ignore_index=True,
                                   sort=True)
    print(tracks_from_albums)

    # Concatenate the tracks, show only columns names that are in all tables
    tracks_from_albums = pd.concat([tracks_master,  tracks_ride, tracks_st],
                                   join="inner",
                                   sort=True)
    print(tracks_from_albums)


def concatenating_with_keys(inv_jul, inv_aug, inv_sep):
    # Concatenate the tables and add keys
    inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                                keys=['7Jul', '8Aug', '9Sep'])

    # Group the invoices by the index keys and find avg of the total column
    avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total': 'mean'})

    # Bar plot of avg_inv_by_month
    avg_inv_by_month.plot(kind='bar')
    plt.show()


def using_append(tracks_ride, tracks_master, tracks_st, invoice_items):
    # Use the .append() method to combine the tracks tables
    metallica_tracks = tracks_ride.append(
        [tracks_master, tracks_st], sort=False)

    # Merge metallica_tracks and invoice_items
    tracks_invoices = metallica_tracks.merge(
        invoice_items, on="tid", how="inner")

    # For each tid and name sum the quantity sold
    tracks_sold = tracks_invoices.groupby(
        ['tid', 'name']).agg({'quantity': 'sum'})

    # Sort in decending order by quantity and print the results
    print(tracks_sold.sort_values('quantity', ascending=False))
