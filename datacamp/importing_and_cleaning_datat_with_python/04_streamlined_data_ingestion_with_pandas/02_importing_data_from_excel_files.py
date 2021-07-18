import pandas as pd
import matplotlib.pyplot as plt 

file_name = "data/fcc-new-coder-survey.xlsx"

def import_data_from_excel_file():
    survey_responses = pd.read_excel(file_name)
    print(survey_responses.head())

    col_string = "AD, AW:BA"
    survey_responses = pd.read_excel(file_name,
                                     skiprows=2,
                                     usecols=col_string)
    print(survey_responses.columns)


def select_a_single_sheet():
    # Create df from second worksheet by referencing its position
    responses_2017 = pd.read_excel(file_name, sheet_name=1)

    # Graph where people would like to get a developer job
    job_prefs = responses_2017.groupby("JobPref").JobPref.count()
    job_prefs.plot.barh()
    plt.show()


def select_multiple_sheets():
    all_survey_data = pd.read_excel(file_name, sheet_name=["2016", "2017"])
    print(type(all_survey_data))

    all_survey_data = pd.read_excel(file_name, sheet_name=[0, "2017"])
    print(all_survey_data.keys())

    all_survey_data = pd.read_excel(file_name, sheet_name=None)
    print(all_survey_data.keys())


def work_with_multiple_spreadsheets():
    responses = pd.read_excel(file_name, skiprows=2, sheet_name=None)
    all_responses = pd.DataFrame()

    # Set up for loop to iterate through values in responses
    for df in responses.values():
        # Print the number of rows being added
        print("Adding {} rows".format(df.shape[0]))
        # Append df to all_responses, assign result
        all_responses = all_responses.append(df)

    # Graph employment statuses in sample
    counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
    counts.plot.barh()
    plt.show()

def modifying_boolean_values(): 
    survey_subset = pd.read_excel(file_name,
                                dtype={"HasDebt": bool,
                                "AttendedBootCampYesNo": bool},
                                true_values=["Yes"],
                                false_values=["No"])

    # View the data
    print(survey_subset.head())

def modifying_imports_for_datetime(): 
    datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}
    survey_data = pd.read_excel(file_name, parse_dates=datetime_cols)
    print(survey_data.Part2Start.describe())

    survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                    format="%m%d%Y %H:%M:%S")
    print(survey_data["Part2EndTime"].head())


#select_multiple_sheets()
#import_data_from_excel_file()
work_with_multiple_spreadsheets()
