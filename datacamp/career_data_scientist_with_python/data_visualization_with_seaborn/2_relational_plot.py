import matplotlib.pyplot as plt
import seaborn as sns
from data import load_world_data, load_survey_data, load_student_data, load_mpg_data


def relational_plots_1(student_data):
    # Change this scatter plot to arrange the plots in rows instead of columns
    sns.relplot(x="absences", y="G3",
                data=student_data,
                kind="scatter",
                row="study_time")

    # Show plot
    plt.show()


def create_two_factor_subplots(student_data):
    # Adjust further to add subplots based on family support
    sns.relplot(x="G1", y="G3",
                data=student_data,
                kind="scatter",
                col="schoolsup",
                col_order=["yes", "no"],
                row="famsup",
                row_order=["yes", "no"])

    # Show plot
    plt.show()


def change_size_of_scatter_plot_points(mpg):
    # Create scatter plot of horsepower vs. mpg
    sns.relplot(x="horsepower", y="mpg",
                data=mpg, kind="scatter",
                size="cylinders", hue="cylinders")

    # Show plot
    plt.show()


def change_style_of_scatter_plot_points(mpg):
    # Create a scatter plot of acceleration vs. mpg
    sns.relplot(x="acceleration", y="mpg", data=mpg,
                kind="scatter", hue="origin", style="origin")
    # Show plot
    plt.show()


def interpreting_line_plots(mpg):
    # Create line plot
    sns.relplot(x="model_year", y="mpg", data=mpg, kind="line")
    # Show plot
    plt.show()


def visualizing_standard_deviation(mpg):
    # Make the shaded area show the standard deviation
    sns.relplot(x="model_year", y="mpg",
                data=mpg, kind="line", ci="sd")

    # Show plot
    plt.show()


def plotting_subgroups_in_line_plots(mpg):
    # Add markers and make each line have the same style
    sns.relplot(x="model_year", y="horsepower",
                data=mpg, kind="line",
                ci=None, style="origin",
                hue="origin", markers=True,
                dashes=False)

    # Show plot
    plt.show()

# student_data = load_student_data()
# relational_plots_1(student_data)
# create_two_factor_subplots(student_data)


mpg = load_mpg_data()
# change_size_of_scatter_plot_points(mpg)
# change_style_of_scatter_plot_points(mpg)

# interpreting_line_plots(mpg)
# visualizing_standard_deviation(mpg)
plotting_subgroups_in_line_plots(mpg)
