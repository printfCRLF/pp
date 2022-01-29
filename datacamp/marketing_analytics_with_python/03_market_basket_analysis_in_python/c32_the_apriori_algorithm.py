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


def selecting_a_support_threshold(onehot):
    # Compute frequent itemsets using a support of 0.003 and length of 3
    frequent_itemsets_1 = apriori(onehot, min_support=0.003,
                                  max_len=3, use_colnames=True)
    print("frequent itemsets 1 length: ", len(frequent_itemsets_1))

    # Compute frequent itemsets using a support of 0.001 and length of 3
    frequent_itemsets_2 = apriori(onehot, min_support=0.001,
                                  max_len=3, use_colnames=True)

    # Print the number of freqeuent itemsets
    print("frequent itemsets 2 length: ", len(frequent_itemsets_2))

    return frequent_itemsets_1, frequent_itemsets_2


if __name__ == "__main__":
    retail_data = prepare_online_retail_data()
    onehot = onehot_online_retail_data(retail_data)
    # identifying_frequent_itemsets_with_apriori(onehot)
    selecting_a_support_threshold(onehot)
