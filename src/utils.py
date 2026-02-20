"""
Shared utility functions for the Telco Churn project.

ALL contributors may add helper functions here.
This file is shared — coordinate with your team if you're adding something!
"""

import pandas as pd


# === File Paths (everyone uses these) ===
RAW_DATA_PATH = "data/raw/telco_churn.csv"
CLEANED_DATA_PATH = "data/cleaned/telco_churn_cleaned.csv"
FIGURES_PATH = "outputs/figures/"
REPORTS_PATH = "outputs/reports/"


def load_raw_data() -> pd.DataFrame:
    """Load the raw Telco Churn dataset from CSV."""
    return pd.read_csv(RAW_DATA_PATH)


def load_cleaned_data() -> pd.DataFrame:
    """Load the cleaned dataset. Raises FileNotFoundError if cleaning hasn't been run yet."""
    return pd.read_csv(CLEANED_DATA_PATH)


# === Add your helper functions below ===
# If you write a function that might be useful to others, put it here!
# Use a comment with your name so we know who added what.
# Example:
# --- Added by Contributor A ---
# def my_helper():
#     pass
