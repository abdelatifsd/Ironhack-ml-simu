"""
Reporting Module — Contributor D

Your job: Load the cleaned dataset and generate a summary report
that brings together key findings about the data.

Save the report to: outputs/reports/churn_summary_report.txt

You'll create functions that:
1. Generate basic dataset statistics
2. Calculate churn rates across different customer segments
3. Identify the top factors associated with churn
4. Write everything into a formatted text report
"""

import pandas as pd
from src.utils import load_cleaned_data, REPORTS_PATH


def get_dataset_summary(df: pd.DataFrame) -> dict:
    """
    Calculate basic summary statistics about the dataset.

    Returns a dictionary with these keys:
    - 'total_customers': total number of rows (int)
    - 'total_features': total number of columns (int)
    - 'churned_count': number of customers who churned (int)
    - 'retained_count': number of customers who did NOT churn (int)
    - 'churn_rate': percentage of customers who churned, rounded to 2 decimals (float)
    - 'avg_monthly_charges': average MonthlyCharges, rounded to 2 decimals (float)
    - 'avg_tenure': average tenure in months, rounded to 1 decimal (float)

    Args:
        df: The cleaned dataframe.

    Returns:
        dict: Summary statistics.

    Example:
        >>> summary = get_dataset_summary(df)
        >>> print(summary['total_customers'])
        7043
        >>> print(summary['churn_rate'])
        26.54

    Hints:
        - Total customers: len(df) or df.shape[0]
        - Churned customers: df[df['Churn'] == 'Yes']  — count them with len()
        - Churn rate: (churned_count / total_customers) * 100 — round with round(..., 2)
        - Average monthly charges: df['MonthlyCharges'].mean() — round with round(..., 2)
        - Average tenure: df['tenure'].mean() — round with round(..., 1)
        - Return all values in a dictionary: {'key': value, 'key2': value2, ...}
    """
    # TODO: Calculate all the statistics and return as a dictionary
    pass


def get_churn_by_category(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Calculate the churn rate for each unique value in a given column.

    Args:
        df: The cleaned dataframe.
        column: The column name to group by (e.g., 'Contract', 'InternetService').

    Returns:
        pd.DataFrame: A dataframe with these columns:
            - The category column (as the index)
            - 'total': count of customers in that category
            - 'churned': count of churned customers in that category
            - 'churn_rate': percentage who churned, rounded to 2 decimals

    Example:
        >>> result = get_churn_by_category(df, 'Contract')
        >>> print(result)
                          total  churned  churn_rate
        Contract
        Month-to-month    3875     1655       42.71
        One year          1473      166       11.27
        Two year          1695       48        2.83

    Hints:
        Step 1 — Count total customers per category:
            total = df.groupby(column).size().rename('total')

        Step 2 — Count churned customers per category:
            churned = df[df['Churn'] == 'Yes'].groupby(column).size().rename('churned')

        Step 3 — Combine them into one dataframe:
            result = pd.concat([total, churned], axis=1)

        Step 4 — Calculate the churn rate:
            result['churn_rate'] = round((result['churned'] / result['total']) * 100, 2)

        Step 5 — Return result
    """
    # TODO: Calculate churn rates by category
    pass


def get_top_churn_segments(df: pd.DataFrame) -> str:
    """
    Identify and format the top customer segments with the highest churn rates.

    Analyze churn rate by these columns:
    - 'Contract'
    - 'InternetService'
    - 'PaymentMethod'

    For each column, find the category with the highest churn rate
    and include it in the output string.

    Args:
        df: The cleaned dataframe.

    Returns:
        str: A formatted string describing the highest-churn segments.

    Example output:
        "Highest churn segments:
         - Contract: Month-to-month (42.71% churn rate)
         - Internet Service: Fiber optic (41.89% churn rate)
         - Payment Method: Electronic check (45.29% churn rate)"

    Hints:
        Step 1 — Use get_churn_by_category() to get the churn rates for each column.

        Step 2 — Find the row with the maximum churn rate using .idxmax():
            result = get_churn_by_category(df, 'Contract')
            top_category = result['churn_rate'].idxmax()  # e.g., 'Month-to-month'
            top_rate = result.loc[top_category, 'churn_rate']  # e.g., 42.71

        Step 3 — Build the string using an f-string:
            line = f"- Contract: {top_category} ({top_rate}% churn rate)"

        Step 4 — Combine all lines into one string and return it.
            You can build a list of lines, then join them:
            lines = ["Highest churn segments:"]
            lines.append(f"  - Contract: ...")
            lines.append(f"  - Internet Service: ...")
            return "\\n".join(lines)
    """
    # TODO: Find the highest-churn category for each analysis column
    pass


def format_report(
    summary: dict,
    churn_by_contract: pd.DataFrame,
    churn_by_internet: pd.DataFrame,
    top_segments: str,
) -> str:
    """
    Combine all analysis results into a formatted text report.

    The report should look professional and readable. Use this structure:

        ==========================================
        TELCO CUSTOMER CHURN — SUMMARY REPORT
        ==========================================

        1. DATASET OVERVIEW
        -------------------
        Total Customers   : 7,043
        Total Features    : 20
        Churned Customers : 1,869
        Retained Customers: 5,174
        Overall Churn Rate: 26.54%
        Avg Monthly Charges: $64.76
        Avg Customer Tenure: 32.4 months

        2. CHURN BY CONTRACT TYPE
        -------------------------
        (churn_by_contract printed as a table)

        3. CHURN BY INTERNET SERVICE
        ----------------------------
        (churn_by_internet printed as a table)

        4. KEY FINDINGS
        ---------------
        (top_segments string)

        ==========================================

    Args:
        summary: Dictionary from get_dataset_summary()
        churn_by_contract: DataFrame from get_churn_by_category(df, 'Contract')
        churn_by_internet: DataFrame from get_churn_by_category(df, 'InternetService')
        top_segments: String from get_top_churn_segments()

    Returns:
        str: The complete formatted report as a single string.

    Hints:
        - Use triple-quoted f-strings for multi-line text blocks:
            report = f\"\"\"
            ==========================================
            ...
            Total Customers: {summary['total_customers']:,}
            ...
            \"\"\"
        - The :, format adds thousands separators: f"{7043:,}" gives "7,043"
        - Use .to_string() to convert DataFrames to nicely formatted strings:
            churn_by_contract.to_string()
        - You can build the report in sections and concatenate them with +
    """
    # TODO: Build the report string
    pass


def save_report(report: str) -> None:
    """
    Save the report to a text file.

    Args:
        report: The formatted report string.

    Saves to: outputs/reports/churn_summary_report.txt
    """
    # TODO: Write the report string to a file
    # Hint:
    #   with open(REPORTS_PATH + 'churn_summary_report.txt', 'w') as f:
    #       f.write(report)
    pass


def run_reporting_pipeline() -> None:
    """
    Run the full reporting pipeline and save the report.
    """
    print("Starting Report Generation...")
    df = load_cleaned_data()
    print(f"  Loaded cleaned data: {len(df)} rows")

    summary = get_dataset_summary(df)
    print(f"  Overall churn rate: {summary['churn_rate']}%")

    churn_by_contract = get_churn_by_category(df, "Contract")
    churn_by_internet = get_churn_by_category(df, "InternetService")
    top_segments = get_top_churn_segments(df)

    report = format_report(summary, churn_by_contract, churn_by_internet, top_segments)
    save_report(report)

    print(f"  Report saved to {REPORTS_PATH}churn_summary_report.txt")
    print("Reporting complete!")
