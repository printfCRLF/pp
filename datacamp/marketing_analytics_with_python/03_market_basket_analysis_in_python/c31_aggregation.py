import pandas as pd
from data import prepare_online_retail_data, onehot_online_retail_data
from util import aggregate


def performing_aggregation(onehot):
    # Select the column headers for sign items
    sign_headers = [i for i in onehot.columns if i.lower().find('sign') >= 0]

    # Select columns of sign items using sign_headers
    sign_columns = onehot[sign_headers]

    # Perform aggregation of sign items into sign category
    signs = sign_columns.sum(axis=1) >= 1.0

    # Print support for signs
    print('Share of Signs: %.2f' % signs.mean())


def defining_aggregation_function(onehot):
    # Aggregate items for the bags, boxes, and candles categories
    bags = aggregate(onehot, 'bag')
    boxes = aggregate(onehot, 'box')
    candles = aggregate(onehot, 'candle')

    print("Support for bags", bags.mean())
    print("Support for boxes", boxes.mean())
    print("Support for candles", candles.mean())


if __name__ == "__main__":
    retail_data = prepare_online_retail_data()
    onehot = onehot_online_retail_data(retail_data)
    # performing_aggregation(onehot)
    defining_aggregation_function(onehot)
