from mlxtend.frequent_patterns import apriori, association_rules
from data import prepare_online_retail_data, onehot_online_retail_data
from c32_the_apriori_algorithm import identifying_frequent_itemsets_with_apriori,  selecting_a_support_threshold


def generating_association_rules(frequent_itemsets_1, frequent_itemsets_2):
    # Compute all association rules for frequent_itemsets_1
    rules_1 = association_rules(frequent_itemsets_1,
                                metric="support",
                                min_threshold=0.0015)

    # Compute all association rules for frequent_itemsets_2
    rules_2 = association_rules(frequent_itemsets_2,
                                metric="support",
                                min_threshold=0.0015)

    # Print the number of association rules generated
    print(len(rules_1), len(rules_2))


def pruning_with_lift(onehot):
    # Compute frequent itemsets using the Apriori algorithm
    frequent_itemsets = apriori(onehot, min_support=0.001,
                                max_len=2, use_colnames=True)

    # Compute all association rules for frequent_itemsets
    rules = association_rules(frequent_itemsets,
                              metric="lift",
                              min_threshold=1.0)

    # Print association rules
    print(rules)


def pruning_with_confidence(onehot):
    # Compute frequent itemsets using the Apriori algorithm
    frequent_itemsets = apriori(onehot, min_support=0.0015,
                                max_len=2, use_colnames=True)

    # Compute all association rules using confidence
    rules = association_rules(frequent_itemsets,
                              metric="confidence",
                              min_threshold=0.5)

    # Print association rules
    print(rules)


if __name__ == "__main__":
    retail_data = prepare_online_retail_data()
    onehot = onehot_online_retail_data(retail_data)
    # frequent_itemsets_1, frequent_itemsets_2 = selecting_a_support_threshold(
    #     onehot)
    # generating_association_rules(frequent_itemsets_1, frequent_itemsets_2)

    # pruning_with_lift(onehot)

    pruning_with_confidence(onehot)
