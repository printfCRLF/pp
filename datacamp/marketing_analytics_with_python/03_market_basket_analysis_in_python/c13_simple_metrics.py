from mlxtend.preprocessing import TransactionEncoder
import numpy as np
import pandas as pd
from c12_intro_to_market_basket_analysis import preparing_data_for_market_basket_analysis


def onehot_encoding_transaction_data(transactions):
    encoder = TransactionEncoder().fit(transactions)
    onehot = encoder.transform(transactions)
    onehot = pd.DataFrame(onehot, columns=encoder.columns_)

    print(onehot)
    return onehot


def compute_support_metric(onehot):
    support = onehot.mean()
    print(support)

    onehot['jam+bread'] = np.logical_and(onehot['jam'], onehot["bread"])
    support = onehot.mean()
    print(support)


if __name__ == "__main__":
    transactions = preparing_data_for_market_basket_analysis()
    onehot = onehot_encoding_transaction_data(transactions)
    compute_support_metric(onehot)

