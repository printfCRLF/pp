import numpy as np
import pandas as pd
from itertools import permutations
from data import prepare_books3_dataset, prepare_books5_dataset
from util import zhang


def computing_association_and_dissociation(books):
    # Compute the support of Twilight and Harry Potter
    supportT = books['Twilight'].mean()
    supportP = books['Potter'].mean()

    # Compute the support of both books
    supportTP = np.logical_and(books['Twilight'], books['Potter']).mean()

    # Complete the expressions for the numerator and denominator
    numerator = supportTP - supportT*supportP
    denominator = max(supportTP*(1-supportT), supportT*(supportP-supportTP))

    # Compute and print Zhang's metric
    zhang = numerator / denominator
    print(zhang)


def generating_association_rules(items):
    df = pd.DataFrame(columns=['antecedents', 'consequents', 'zhang'])
    rules = list(permutations(items, 2))

    for rule in rules:
        df.loc[-1] = [rule[0], rule[1], np.NaN]
        df.index = df.index + 1  # shifting index
        df = df.sort_index()  # sorting by index

    return df


def applying_zhangs_metric(books, itemsets):
    # Define an empty list for Zhang's metric
    zhangs_metric = []

    # Loop over lists in itemsets
    for _, itemset in itemsets.iterrows():
        # Extract the antecedent and consequent columns
        antecedent = books[itemset["antecedents"]]
        consequent = books[itemset["consequents"]]

        # Complete Zhang's metric and append it to the list
        zhangs_metric.append(zhang(antecedent, consequent))

    # Print results
    itemsets['zhang'] = zhangs_metric
    print(rules)


if __name__ == "__main__":
    books3 = prepare_books3_dataset()
    # computing_association_and_dissociation(books3)

    books5 = prepare_books5_dataset()
    rules = generating_association_rules(books5.columns)
    applying_zhangs_metric(books5, rules)
