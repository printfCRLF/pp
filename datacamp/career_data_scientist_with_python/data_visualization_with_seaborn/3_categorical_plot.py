import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
from data import load_world_data, load_survey_data, load_student_data, load_mpg_data


def age_category(age):
    if age < 21:
        return "Less than 21"
    else:
        return "21+"


def count_plots(survey_data):
    survey_data["Age Category"] = survey_data["Age"].apply(
        lambda age: "Less than 21" if age < 21 else "21+")
    # Create column subplots based on age category
    sns.catplot(y="Internet usage", data=survey_data,
                kind="count", col="Age Category")

    # Show plot
    plt.show()


def bar_plots(student_data):
    # Turn off the confidence intervals
    sns.catplot(x="study_time", y="G3", data=student_data, kind="bar",
                order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"], ci=None)
    plt.show()


def createa_box_plot(student_data):
    # Specify the category ordering
    study_time_order = ["<2 hours", "2 to 5 hours",
                        "5 to 10 hours", ">10 hours"]
    # Create a box plot and set the order of the categories
    sns.catplot(x="study_time", y="G3", data=student_data,
                order=study_time_order, kind="box")
    plt.show()


def box_plot_without_outliers(student_data):
    # Create a box plot with subgroups and omit the outliers
    sns.catplot(x="internet", y="G3", data=student_data,
                kind="box", hue="location", sym="")
    plt.show()


def adjusting_whiskers(student_data):
    # Set the whiskers to 0.5 * IQR
    sns.catplot(x="romantic", y="G3", data=student_data,
                kind="box",  whis=0.5)
    plt.show()


def point_plot_1(student_data):
    # Create a point plot of family relationship vs. absences
    sns.catplot(x="famrel", y="absences", data=student_data, kind="point")
    plt.show()


def point_plot_2(student_data):
    # Create a point plot of family relationship vs. absences
    sns.catplot(x="famrel", y="absences", data=student_data, kind="point",
                capsize=0.2,  join=False)
    plt.show()


def point_plot_with_subgroups(student_data):
    # Create a point plot with subgroups
    sns.catplot(x="romantic", y="absences",
                data=student_data, kind="point", hue="school",
                ci=None, estimator=median)
    plt.show()


# survey_data = load_survey_data()
# count_plots(survey_data)


student_data = load_student_data()
# bar_plots(student_data)
# createa_box_plot(student_data)
# box_plot_without_outliers(student_data)
# adjusting_whiskers(student_data)
# point_plot_1(student_data)
# point_plot_2(student_data)
point_plot_with_subgroups(student_data)
