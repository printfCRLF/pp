# Import apriori from mlxtend
from mlxtend.frequent_patterns import apriori
from data import prepare_online_retail_data, onehot_online_retail_data


def identifying_frequent_itemsets_with_apriori(onehot):
    # Compute frequent itemsets using the Apriori algorithm
    frequent_itemsets = apriori(onehot,
                                min_support=0.006,
                                max_len=3,
                                use_colnames=True)

    # Print a preview of the frequent itemsets
    print(frequent_itemsets.head())


if __name__ == "__main__":
    retail_data = prepare_online_retail_data()
    onehot = onehot_online_retail_data(retail_data)
    identifying_frequent_itemsets_with_apriori(onehot)
