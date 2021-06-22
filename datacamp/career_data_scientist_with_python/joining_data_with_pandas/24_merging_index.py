import math
from data import load_sequels, load_financials


def do_sequels_earn_more(sequels, financials):
    # Merge sequels and financials on index id
    sequels_fin = sequels.merge(financials, on='id', how='left')

    # Self merge with suffixes as inner join with left on sequel and right on id
    orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                                 right_on='id', right_index=True,
                                 suffixes=('_org', '_seq'))

    # Add calculation to subtract revenue_org from revenue_seq
    orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

    # Select the title_org, title_seq, and diff
    titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

    # Print the first rows of the sorted titles_diff
    print(titles_diff.sort_values("diff", ascending=False).head())


sequels = load_sequels()
sequels.fillna(math.nan)
sequels = sequels.set_index("id")
financials = load_financials()
financials.fillna(math.nan)
financials = financials.set_index("id")
do_sequels_earn_more(sequels, financials)
