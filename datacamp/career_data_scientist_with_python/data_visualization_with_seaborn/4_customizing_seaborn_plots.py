import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
from data import load_survey_data


def box_plot_with_subgroups(survey_data):
    survey_data["Interested in Pets"] = survey_data["Pets"].apply(
        lambda p: "Yes" if p > 3 else "No")

    sns.set_palette("Blues")
    # Adjust to add subgroups based on "Interested in Pets"
    g = sns.catplot(x="Gender",
                    y="Age", data=survey_data,
                    kind="box", hue="Interested in Pets")

    g.fig.suptitle("Age of Those Interested in Pets vs. Not")
    plt.show()


def bar_lot_with_subplots(survey_data):
    survey_data["Likes Techno"] = survey_data["Techno"].apply(
        lambda t: True if t > 3 else False)
    sns.set_style("dark")

    # Adjust to add subplots per gender
    g = sns.catplot(x="Village - town", y="Likes Techno",
                    data=survey_data, kind="bar",
                    col="Gender")

    # Add title and axis labels
    g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
    g.set(xlabel="Location of Residence",
          ylabel="% Who Like Techno")
    plt.show()


survey_data = load_survey_data()
box_plot_with_subgroups(survey_data)
bar_lot_with_subplots(survey_data)
