from data import load_homelessness_data


def adding_new_columns(homelessness):
    # Add total col as sum of individuals and family_members
    homelessness["total"] = homelessness["individuals"] + \
        homelessness["family_members"]

    # Add p_individuals col as proportion of individuals
    homelessness["p_individuals"] = homelessness["individuals"] / \
        homelessness["total"]
    # See the result
    print(homelessness)

    return homelessness


def combo_attach(homelessness):
    # Create indiv_per_10k col as homeless individuals per 10k state pop
    homelessness["indiv_per_10k"] = 10000 * \
        homelessness["individuals"] / homelessness["state_pop"]

    # Subset rows for indiv_per_10k greater than 20
    high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

    # Sort high_homelessness by descending indiv_per_10k
    high_homelessness_srt = high_homelessness.sort_values(
        "indiv_per_10k", ascending=False)

    # From high_homelessness_srt, select the state and indiv_per_10k cols
    result = high_homelessness_srt[["state", "indiv_per_10k"]]

    # See the result
    print(result)


homelessness = load_homelessness_data()
homelessness_pct_individuals = adding_new_columns(homelessness)
combo_attach(homelessness_pct_individuals)
