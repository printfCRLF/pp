import pandas as pd
from data import load_telco_data
from sklearn.preprocessing import StandardScaler


def investigate_the_data(telco_raw):
    # Print the data types of telco_raw dataset
    print(telco_raw.dtypes)

    # Print the header of telco_raw dataset
    print(telco_raw.head())

    # Print the number of unique values in each telco_raw column
    print(telco_raw.nunique())


def seperate_numerical_and_categorical_columns(telco_raw):
    # Store customerID and Churn column names
    custid = ['customerID']
    target = ['Churn']

    # Store categorical column names
    categorical_cols = telco_raw.nunique(
    )[telco_raw.nunique() < 5].keys().tolist()

    # Remove target from the list of categorical variables
    categorical_cols.remove(target[0])

    # Store numerical column names
    numerical_cols = [
        x for x in telco_raw.columns if x not in custid + target + categorical_cols]

    return categorical_cols, numerical_cols


def encoding_categorical_and_scale_numerical_variables(telco_raw, categorical, numerical):
    telco_raw = pd.get_dummies(
        data=telco_raw, columns=categorical, drop_first=True)

    # Initialize StandardScaler instance
    scaler = StandardScaler()

    # Fit and transform the scaler on numerical columns
    scaled_numerical = scaler.fit_transform(telco_raw[numerical])

    # Build a DataFrame from scaled_numerical
    scaled_numerical = pd.DataFrame(scaled_numerical, columns=numerical)

    telco_raw = telco_raw.drop(columns=numerical, axis=1)
    telco = telco_raw.merge(right=scaled_numerical, how="left",
                            left_index=True, right_index=True)
    return telco


def encoding_categorical_and_scale_numerical_variables2(telco_raw, categorical_cols, numerical_cols):
    # Perform one-hot encoding to categorical variables
    telco_raw_onehot = pd.get_dummies(
        data=telco_raw, columns=categorical_cols, drop_first=True)

    # Initialize StandardScaler instance
    scaler = StandardScaler()
    # Fit and transform the scaler on numerical columns
    scaled_numerical = scaler.fit_transform(telco_raw_onehot[numerical_cols])

    # Build a DataFrame from scaled_numerical
    scaled_numerical_df = pd.DataFrame(
        scaled_numerical, columns=numerical_cols)

    df_without_num = telco_raw_onehot.drop(
        axis="columns", columns=numerical_cols)
    merged = df_without_num.merge(right=scaled_numerical_df, how="left",
                                  left_index=True, right_index=True)

    return merged


if __name__ == "__main__":
    telco_raw = load_telco_data()
    investigate_the_data(telco_raw)
    categorical, numerical = seperate_numerical_and_categorical_columns(
        telco_raw)
    encoding_categorical_and_scale_numerical_variables(
        telco_raw, categorical, numerical)
