import matplotlib.pyplot as plt
import seaborn as sns
from data import load_world_data, load_survey_data, load_student_data


def make_a_scatter_plot(world):
    gdp = world["GDP ($ per capita)"].tolist()
    phones = world["Phones (per 1000)"].tolist()
    percent_literate = world["Literacy (%)"].tolist()

    # Create scatter plot with GDP on the x-axis and number of phones on the y-axis
    sns.scatterplot(x=gdp, y=phones)
    # Show plot
    plt.show()

    # # Change this scatter plot to have percent literate on the y-axis
    # sns.scatterplot(x=gdp, y=percent_literate)
    # # Show plot
    # plt.show()


def making_a_count_plot(world):
    region = world["Region"]
    # Create count plot with region on the y-axis
    sns.countplot(y=region)

    # Show plot
    plt.show()


def making_count_plot_with_dataframe(df):
    # Create a count plot with "Spiders" on the x-axis
    sns.countplot(x="Spiders", data=df)

    # Display the plot
    plt.show()


def hue_and_scatter_plots(student_data):
    # Change the legend order in the scatter plot
    sns.scatterplot(x="absences", y="G3",
                    data=student_data,
                    hue="location",
                    hue_order=["Rural", "Urban"])

    # Show plot
    plt.show()


def hue_and_count_plots(student_data):
    # Create a dictionary mapping subgroup values to colors
    palette_colors = {"Rural": "green", "Urban": "blue"}

    # Create a count plot of school with location subgroups
    sns.countplot(x="school", data=student_data,
                  hue="location", palette=palette_colors)

    # Display plot
    plt.show()


# world = load_world_data()
# make_a_scatter_plot(world)
# making_a_count_plot(world)

# survey = load_survey_data()
# making_count_plot_with_dataframe(survey)

student_data = load_student_data()
# hue_and_scatter_plots(student_data)
hue_and_count_plots(student_data)
