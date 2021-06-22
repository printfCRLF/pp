def performing_anti_join(employees, top_cust):
    # Merge employees and top_cust
    empl_cust = employees.merge(top_cust, on='srid',
                                how='left', indicator=True)

    # Select the srid column where _merge is left_only
    srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

    # Get employees not working with top customers
    print(employees[employees["srid"].isin(srid_list)])


def performing_a_semi_join(non_mus_tcks, top_invoices, genres):
    # Merge the non_mus_tck and top_invoices tables on tid
    tracks_invoices = non_mus_tcks.merge(top_invoices, on="tid")

    # Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
    top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices["tid"])]

    # Group the top_tracks by gid and count the tid rows
    cnt_by_gid = top_tracks.groupby(
        ['gid'], as_index=False).agg({'tid': 'count'})

    # Merge the genres table to cnt_by_gid on gid and print
    print(cnt_by_gid.merge(genres, on="gid"))
