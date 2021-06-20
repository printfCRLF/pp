from data import load_homelessness_data


def sorting_rows(homelessness):
    # Sort homelessness by individual
    homelessness_ind = homelessness.sort_values("individuals")
    # Print the top few rows
    print(homelessness_ind.head())

    # Sort homelessness by descending family members
    homelessness_fam = homelessness.sort_values(
        "family_members", ascending=False)
    # Print the top few rows
    print(homelessness_fam.head())

    # Sort homelessness by region, then descending family members
    homelessness_reg_fam = homelessness.sort_values(
        ["region", "family_members"], ascending=[True, False])
    # Print the top few rows
    print(homelessness_reg_fam.head())


def subsetting_columns(homelessness):
    # Select the individuals column
    individuals = homelessness["individuals"]
    # Print the head of the result
    print(individuals.head())

    # Select the state and family_members columns
    state_fam = homelessness[["state", "family_members"]]
    # Print the head of the result
    print(state_fam.head())

    # Select only the individuals and state columns, in that order
    ind_state = homelessness[["individuals", "state"]]
    # Print the head of the result
    print(ind_state.head())


def subsetting_rows(homelessness):
    # Filter for rows where individuals is greater than 10000
    ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
    # See the result
    print(ind_gt_10k)

    # Filter for rows where region is Mountain
    mountain_reg = homelessness[homelessness["region"] == "Mountain"]
    # See the result
    print(mountain_reg)

    # Filter for rows where family_members is less than 1000
    # and region is Pacific
    fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (
        homelessness["region"] == "Pacific")]
    # See the result
    print(fam_lt_1k_pac)


def subsetting_rows_by_categorical_data(homelessness):
    # Subset for rows in South Atlantic or Mid-Atlantic regions
    south_mid_atlantic = homelessness[homelessness.region.isin(
        ["South Atlantic", "Mid-Atlantic"])]

    # See the result
    print(south_mid_atlantic)

    # The Mojave Desert states
    canu = ["California", "Arizona", "Nevada", "Utah"]

    # Filter for rows in the Mojave Desert states
    mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

    # See the result
    print(mojave_homelessness)


homelessness = load_homelessness_data()
sorting_rows(homelessness)
subsetting_columns(homelessness)
subsetting_rows(homelessness)
subsetting_rows_by_categorical_data(homelessness)
