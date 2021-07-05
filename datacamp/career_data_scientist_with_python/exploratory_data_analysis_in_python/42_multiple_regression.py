import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from data import load_gss_data


def plot_income_and_education(gss):
    # Group by educ
    grouped = gss.groupby("educ")

    # Compute mean income in each group
    mean_income_by_educ = grouped["realinc"].mean()

    # Plot mean income as a scatter plot
    plt.plot(mean_income_by_educ, 'o', alpha=0.5)

    # Label the axes
    plt.xlabel('Education (years)')
    plt.ylabel('Income (1986 $)')
    plt.show()


def non_lineaer_model_of_education(gss):
    # Add a new column with educ squared
    gss['educ2'] = gss["educ"] ** 2
    gss['age2'] = gss["age"] ** 2

    # Run a regression model with educ, educ2, age, and age2
    results = smf.ols("realinc ~ educ + educ2 + age + age2", data=gss).fit()

    # Print the estimated parameters
    print(results.params)


gss = load_gss_data()
plot_income_and_education(gss)
non_lineaer_model_of_education(gss)
