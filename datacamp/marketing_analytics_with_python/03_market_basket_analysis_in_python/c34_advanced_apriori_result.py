from mlxtend.frequent_patterns import apriori, association_rules
from util import zhangs_rule2


def aggregating_and_filtering(aggregated):
    # Apply the apriori algorithm with a minimum support of 0.0001
    frequent_itemsets = apriori(
        aggregated, min_support=0.0001, use_colnames=True)

    # Generate the initial set of rules using a minimum support of 0.0001
    rules = association_rules(frequent_itemsets,
                              metric="support", min_threshold=0.0001)

    # Set minimum antecedent support to 0.35
    rules = rules[rules['antecedent support'] > 0.35]

    # Set maximum consequent support to 0.35
    rules = rules[rules['consequent support'] < 0.35]

    # Print the remaining rules
    print(rules)


def applying_zhangs_rule(frequent_itemsets):
    # Generate the initial set of rules using a minimum lift of 1.00
    rules = association_rules(
        frequent_itemsets, metric="lift", min_threshold=1.00)

    # Set antecedent support to 0.005
    rules = rules[rules['antecedent support'] > 0.005]

    # Set consequent support to 0.005
    rules = rules[rules['consequent support'] > 0.005]

    # Compute Zhang's rule
    rules['zhang'] = zhangs_rule2(rules)

    # Set the lower bound for Zhang's rule to 0.98
    rules = rules[rules['zhang'] > 0.98]
    print(rules[['antecedents', 'consequents']])


def advanced_filtering_with_multiple_metrics(onehot):
    # Apply the Apriori algorithm with a minimum support threshold of 0.001
    frequent_itemsets = apriori(onehot, min_support=0.001, use_colnames=True)

    # Recover association rules using a minium support threshold of 0.001
    rules = association_rules(
        frequent_itemsets, metric='support', min_threshold=0.001)

    # Apply a 0.002 antecedent support threshold, 0.60 confidence threshold, and 2.50 lift threshold
    filtered_rules = rules[(rules['antecedent support'] > 0.002) &
                           (rules['consequent support'] > 0.01) &
                           (rules['confidence'] > 0.60) &
                           (rules['lift'] > 2.50)]

    # Print remaining rule
    print(filtered_rules[['antecedents', 'consequents']])


if __name__ == "__main__":
    aggregating_and_filtering(aggregated)
    applying_zhangs_rule(frequent_itemsets)
    advanced_filtering_with_multiple_metrics(onehot)
