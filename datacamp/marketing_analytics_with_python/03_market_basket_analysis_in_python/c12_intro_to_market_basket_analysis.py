import pandas as pd
from itertools import permutations

def preparing_data_for_market_basket_analysis():
    groceries_path = 'https://assets.datacamp.com/production/repositories/5654/datasets/5992818fd324b0de7d48311ee43fa038f7614ee5/small_grocery_store.csv'
    groceries = pd.read_csv(groceries_path)
    transactions = groceries["Transaction"].apply(lambda t: t.split(","))
    transactions = list(transactions)
    #print(transactions)

    return transactions


def generating_association_rules(transactions):
    f = [i for t in transactions for i in t]
    flattened = [i for t in transactions for i in t]
    groceries = list(set(flattened))

    rules = list(permutations(groceries, 2))
    print(rules)
    print(len(rules))

if __name__ == "__main__":
    transactions = preparing_data_for_market_basket_analysis()
    generating_association_rules(transactions)