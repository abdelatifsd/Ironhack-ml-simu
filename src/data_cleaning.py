"""
Data Cleaning Module — Contributor A

Your job: Load the raw Telco Churn dataset, clean it up, and save
a clean version that the rest of the team can use.

The raw dataset has some issues:
- The 'TotalCharges' column has some blank strings instead of numbers
- The 'SeniorCitizen' column uses 0/1 instead of 'Yes'/'No' like other columns
- The 'customerID' column is not useful for analysis

Your cleaned dataset should be saved to: data/cleaned/telco_churn_cleaned.csv
"""

import numpy as np
import pandas as pd
from src.utils import RAW_DATA_PATH, CLEANED_DATA_PATH


# DONE
def load_raw_data() -> pd.DataFrame:
    """
    Load the raw telco churn CSV file.

    Returns:
        pd.DataFrame: The raw dataset as-is from the CSV file.

    Example:
        >>> df = load_raw_data()
        >>> print(df.shape)
        (7043, 21)
    """
    # TODO: Use pd.read_csv to load the file at RAW_DATA_PATH

    df = pd.read_csv(RAW_DATA_PATH)
    return df


# DONE
def drop_customer_id(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the 'customerID' column since it's just an identifier,
    not useful for analysis.

    Args:
        df: The raw dataframe.

    Returns:
        pd.DataFrame: Dataframe without the 'customerID' column.

    Example:
        >>> df = drop_customer_id(df)
        >>> 'customerID' in df.columns
        False
    """
    df = df.drop("customerID", axis=1)
    return df
    # TODO: Drop the 'customerID' column
    # Hint: Use df.drop(columns=[...])
    pass


def fix_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fix the 'TotalCharges' column.

    Problem: Some rows have empty strings ' ' instead of numbers in TotalCharges.
    These are new customers with tenure=0 who haven't been charged yet.

    Steps:
        1. Replace empty strings ' ' with 0
        2. Convert the column to float type

    Args:
        df: Dataframe with the raw TotalCharges column.

    Returns:
        pd.DataFrame: Dataframe with TotalCharges as a clean float column.

    Example:
        >>> df = fix_total_charges(df)
        >>> df['TotalCharges'].dtype
        float64
    """
    # Replace the empty string with 0
    df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")

    # Convert the column to float type.
    df["TotalCharges"] = df["TotalCharges"].astype(float)

    return df
    # TODO: Replace ' ' (space) with 0 in TotalCharges, then convert to float
    # Hint: df['TotalCharges'].replace(' ', 0) and .astype(float)
    pass


# Done
def fix_senior_citizen(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'SeniorCitizen' from 0/1 integers to 'No'/'Yes' strings.

    This makes it consistent with other binary columns like 'Partner'
    and 'Dependents' which use 'Yes'/'No'.

    Args:
        df: Dataframe with SeniorCitizen as 0/1.

    Returns:
        pd.DataFrame: Dataframe with SeniorCitizen as 'Yes'/'No'.

    Example:
        >>> df = fix_senior_citizen(df)
        >>> df['SeniorCitizen'].unique()
        array(['No', 'Yes'], dtype=object)
    """
    df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})
    return df
    # TODO: Map 0 -> 'No' and 1 -> 'Yes'
    # Hint: df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    pass


# Done
def check_for_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check for and remove any duplicate rows.

    Args:
        df: The dataframe to check.

    Returns:
        pd.DataFrame: Dataframe with duplicates removed (if any).

    Prints:
        A message saying how many duplicates were found and removed.

    Example:
        >>> df = check_for_duplicates(df)
        Found 0 duplicate rows. No duplicates to remove.
    """
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"Found {duplicate_count} duplicate rows")
        df = df.drop_duplicates()
    else:
        print("Found 0 duplicate rows. No duplicates to remove.")

    return df
    # TODO: Check df.duplicated().sum() and print the count
    # Then drop duplicates if any exist
    pass


# DONE
def save_cleaned_data(df: pd.DataFrame) -> None:
    """
    Save the cleaned dataframe to CSV.

    Args:
        df: The cleaned dataframe to save.

    Saves to: data/cleaned/telco_churn_cleaned.csv (without the index)
    """
    # TODO: Save to CLEANED_DATA_PATH using df.to_csv(..., index=False)

    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Success! Cleaned data saved to: {CLEANED_DATA_PATH}")
    pass


def run_cleaning_pipeline() -> pd.DataFrame:
    """
    Run all cleaning steps in order and save the result.

    This is the main function that chains all the steps together.

    Returns:
        pd.DataFrame: The fully cleaned dataframe.
    """
    print("Starting data cleaning...")
    df = load_raw_data()
    print(f"  Loaded {len(df)} rows, {len(df.columns)} columns")

    df = drop_customer_id(df)
    df = fix_total_charges(df)
    df = fix_senior_citizen(df)
    df = check_for_duplicates(df)

    save_cleaned_data(df)
    print(f"  Cleaned data saved to {CLEANED_DATA_PATH}")
    print("Data cleaning complete!")

    return df
