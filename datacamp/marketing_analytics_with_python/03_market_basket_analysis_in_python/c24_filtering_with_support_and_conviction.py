

def filtering_with_support_and_conviction(rules):
    # Preview the rules DataFrame using the .head() method
    print(rules.head())

    # Select the subset of rules with antecedent support greater than 0.05
    rules = rules[rules['antecedent support'] > 0.05]

    # Select the subset of rules with a consequent support greater than 0.02
    rules = rules[rules['consequent support'] > 0.02]

    # Select the subset of rules with a conviction greater than 1.01
    rules = rules[rules['conviction'] > 1.01]

    # Print remaining rules
    print(rules)


def using_multi_metric_filtering_to_cross_promote_books(rules):
    # Set the lift threshold to 1.5
    rules = rules[rules['lift'] > 1.5]

    # Set the conviction threshold to 1.0
    rules = rules[rules['conviction'] > 1.0]

    # Set the threshold for Zhang's rule to 0.65
    rules = rules[rules['zhang'] > 0.65]

    # Print rule
    print(rules[['antecedents', 'consequents']])
