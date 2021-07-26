import pandas as pd
import numpy as np
from data import load_stackoverflow_data


def how_sparse_is_my_data(so_survey_df):
    # Subset the DataFrame
    sub_df = so_survey_df[["Age", "Gender"]]
    # Print the number of non-missing values
    print(sub_df.info())

    # Print the top 10 entries of the DataFrame
    print(sub_df.head(10))
    # Print the locations of the missing values
    print(sub_df.head(10).isnull())
    # Print the locations of the non-missing values
    print(sub_df.head(10).notnull())


def list_wise_deletion(so_survey_df):
    # Print the number of rows and columns
    print(so_survey_df.shape)

    # Create a new DataFrame dropping all incomplete rows
    no_missing_values_rows = so_survey_df.dropna()
    # Print the shape of the new DataFrame
    print(no_missing_values_rows.shape)

    # Create a new DataFrame dropping all columns with incomplete rows
    no_missing_values_cols = so_survey_df.dropna(how="any", axis=1)
    # Print the shape of the new DataFrame
    print(no_missing_values_cols.shape)

    # Drop all rows where Gender is missing
    no_gender = so_survey_df.dropna(subset=['Gender'])
    # Print the shape of the new DataFrame
    print(no_gender.shape)


def replacing_missing_value_with_constants(so_survey_df):
    # Print the count of occurrences
    print(so_survey_df['Gender'].value_counts())

    # Replace missing values
    so_survey_df['Gender'].fillna(value="Not Given", inplace=True)

    # Print the count of each value
    print(so_survey_df['Gender'].value_counts())


def filling_continuous_missing_values(so_survey_df):
    # Print the first five rows of StackOverflowJobsRecommend column
    print(so_survey_df["StackOverflowJobsRecommend"].head())

    # Fill missing values with the mean
    so_survey_df['StackOverflowJobsRecommend'].fillna(
        so_survey_df['StackOverflowJobsRecommend'].mean(), inplace=True)
    # Print the first five rows of StackOverflowJobsRecommend column
    print(so_survey_df['StackOverflowJobsRecommend'].head())

    # Fill missing values with the mean
    so_survey_df['StackOverflowJobsRecommend'].fillna(
        so_survey_df['StackOverflowJobsRecommend'].mean(), inplace=True)
    # Round the StackOverflowJobsRecommend values
    so_survey_df['StackOverflowJobsRecommend'] = round(
        so_survey_df['StackOverflowJobsRecommend'])
    # Print the top 5 rows
    print(so_survey_df['StackOverflowJobsRecommend'].head())


def dealing_with_stray_characters(so_survey_df):
    # Remove the commas in the column
    so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace(',', '')
    # Remove the dollar signs in the column
    so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace("$", "")

    # Attempt to convert the column to numeric values
    numeric_vals = pd.to_numeric(so_survey_df['RawSalary'], errors='coerce')
    # Find the indexes of missing values
    idx = numeric_vals.isnull()
    # Print the relevant rows
    print(so_survey_df['RawSalary'][idx])
    # Replace the offending characters
    so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace("£", "")
    # Convert the column to float
    so_survey_df['RawSalary'] = so_survey_df['RawSalary'].astype("float")
    # Print the column
    print(so_survey_df['RawSalary'])


def method_chaining(so_survey_df):
    # Use method chaining
    so_survey_df['RawSalary'] = so_survey_df['RawSalary']\
        .str.replace(",", "")\
        .str.replace("$", "")\
        .str.replace("£", "")\
        .astype("float")

    # Print the RawSalary column
    print(so_survey_df['RawSalary'])


so_survey_df = load_stackoverflow_data()
# how_sparse_is_my_data(so_survey_df)
# list_wise_deletion(so_survey_df)
# replacing_missing_value_with_constants(so_survey_df)
# filling_continuous_missing_values(so_survey_df)
# dealing_with_stray_characters(so_survey_df)
method_chaining(so_survey_df)
