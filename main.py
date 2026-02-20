"""
Telco Customer Churn — Collaborative Project

This is the main entry point. It runs each pipeline step in order.
As each contributor completes their work and their PR is merged,
the instructor will uncomment the relevant section below.

Usage:
    python main.py
"""

from src.data_cleaning import run_cleaning_pipeline
from src.eda import run_eda_pipeline
from src.feature_engineering import run_feature_engineering_pipeline
from src.reporting import run_reporting_pipeline


def main():
    print("=" * 50)
    print("  Telco Customer Churn Analysis Pipeline")
    print("=" * 50)
    print()

    # Step 1: Data Cleaning (Contributor A)
    # Uncomment when Contributor A's PR is merged:
    # cleaned_df = run_cleaning_pipeline()
    # print()

    # Step 2: Exploratory Data Analysis (Contributor B)
    # Uncomment when Contributor B's PR is merged (requires Step 1):
    # run_eda_pipeline()
    # print()

    # Step 3: Feature Engineering (Contributor C)
    # Uncomment when Contributor C's PR is merged (requires Step 1):
    # engineered_df = run_feature_engineering_pipeline()
    # print()

    # Step 4: Reporting (Contributor D)
    # Uncomment when Contributor D's PR is merged (requires Step 1):
    # run_reporting_pipeline()
    # print()

    print("=" * 50)
    print("  Pipeline complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
