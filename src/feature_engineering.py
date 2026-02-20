"""
Feature Engineering Module — Contributor C

Your job: Load the cleaned dataset and transform it so the data is
ready for analysis. This means converting text categories into numbers
and creating some new useful columns.

Save the engineered dataset to: data/cleaned/telco_churn_engineered.csv

You'll do 3 things:
1. Encode binary columns (Yes/No -> 1/0)
2. Create a new 'tenure_group' column that groups customers by how long they've stayed
3. Encode multi-category columns into dummy variables
"""

import pandas as pd
from src.utils import load_cleaned_data


ENGINEERED_DATA_PATH = "data/cleaned/telco_churn_engineered.csv"


def encode_binary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert all Yes/No columns to 1/0.

    Many columns in this dataset have 'Yes'/'No' values. Convert them
    to 1/0 so they're numeric.

    Binary columns to convert:
    - 'gender': Female -> 1, Male -> 0
    - 'Partner': Yes -> 1, No -> 0
    - 'Dependents': Yes -> 1, No -> 0
    - 'PhoneService': Yes -> 1, No -> 0
    - 'PaperlessBilling': Yes -> 1, No -> 0
    - 'Churn': Yes -> 1, No -> 0
    - 'SeniorCitizen': Yes -> 1, No -> 0 (already 'Yes'/'No' after cleaning)

    Args:
        df: The cleaned dataframe.

    Returns:
        pd.DataFrame: Dataframe with binary columns as 1/0 integers.

    Example:
        >>> df = encode_binary_columns(df)
        >>> df['Churn'].unique()
        array([0, 1])

    Hints:
        - For gender specifically: df['gender'].map({'Female': 1, 'Male': 0})
        - For all the Yes/No columns: df[col].map({'Yes': 1, 'No': 0})
        - You can use a loop! Define a list of column names, then loop over them:
            yes_no_columns = ['Partner', 'Dependents', ...]
            for col in yes_no_columns:
                df[col] = df[col].map({'Yes': 1, 'No': 0})
        - Remember to handle 'gender' separately since it has different values.
    """
    # TODO: Convert binary columns to 1/0
    pass


def create_tenure_groups(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column 'tenure_group' that categorizes customers
    by how long they've been with the company.

    Groups:
        0-12 months   -> '0-1 year'
        13-24 months  -> '1-2 years'
        25-48 months  -> '2-4 years'
        49-60 months  -> '4-5 years'
        61-72 months  -> '5-6 years'

    Args:
        df: The dataframe with a 'tenure' column (values range from 0 to 72).

    Returns:
        pd.DataFrame: Dataframe with a new 'tenure_group' column added.

    Hints:
        - Use pd.cut() which automatically sorts values into bins:
            pd.cut(
                df['tenure'],
                bins=[0, 12, 24, 48, 60, 72],
                labels=['0-1 year', '1-2 years', '2-4 years', '4-5 years', '5-6 years']
            )
        - pd.cut() returns a special "Categorical" type — convert it to plain strings
          using .astype(str) so it's easier to work with later.
        - Assign the result to df['tenure_group']
    """
    # TODO: Create tenure groups using pd.cut()
    pass


def encode_multi_category_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert multi-category columns into dummy/one-hot encoded columns.

    Some columns have more than 2 categories. For example, 'InternetService'
    has: 'DSL', 'Fiber optic', 'No'. We can't just use 0/1 for these —
    we need a separate column for each option.

    pd.get_dummies() handles this automatically. For example, 'InternetService'
    becomes two new columns: 'InternetService_Fiber optic' and 'InternetService_No'
    (with drop_first=True, one category is dropped to avoid redundancy).

    Multi-category columns to encode:
    'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaymentMethod'

    Args:
        df: Dataframe (with binary columns and tenure_group already added).

    Returns:
        pd.DataFrame: Dataframe with multi-category columns replaced by dummy columns.
                      It will have more columns than before!

    Hints:
        - Use pd.get_dummies() like this:
            pd.get_dummies(df, columns=[list of column names], drop_first=True)
        - drop_first=True avoids redundancy: if there are 3 categories (A, B, C),
          knowing it's not A or B means it must be C — so we only need 2 columns.
        - This returns a new dataframe, so assign the result: df = pd.get_dummies(...)
    """
    # TODO: Create dummy variables for multi-category columns
    pass


def save_engineered_data(df: pd.DataFrame) -> None:
    """
    Save the engineered dataframe to CSV.

    Args:
        df: The engineered dataframe to save.

    Saves to: data/cleaned/telco_churn_engineered.csv (without the index)
    """
    # TODO: Save to ENGINEERED_DATA_PATH using df.to_csv(..., index=False)
    pass


def run_feature_engineering_pipeline() -> pd.DataFrame:
    """
    Run all feature engineering steps in order and save the result.

    Returns:
        pd.DataFrame: The fully engineered dataframe.
    """
    print("Starting Feature Engineering...")
    df = load_cleaned_data()
    print(f"  Loaded cleaned data: {len(df)} rows, {len(df.columns)} columns")

    df = encode_binary_columns(df)
    print("  Encoded binary columns")

    df = create_tenure_groups(df)
    print("  Created tenure groups")

    # Note: We run encode_multi_category_columns AFTER tenure_groups
    # because get_dummies changes the column structure significantly,
    # and it's easier to add 'tenure_group' before that happens.
    df = encode_multi_category_columns(df)
    print(f"  Encoded multi-category columns -> {len(df.columns)} total columns")

    save_engineered_data(df)
    print(f"  Engineered data saved to {ENGINEERED_DATA_PATH}")
    print("Feature Engineering complete!")

    return df
