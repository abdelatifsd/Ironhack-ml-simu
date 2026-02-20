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
    """

    # Total rows and columns
    total_customers = df.shape[0]
    total_features = df.shape[1]

    # Count churned customers
    churned_count = len(df[df["Churn"] == "Yes"])

    # Retained customers
    retained_count = total_customers - churned_count

    # Churn rate (percentage)
    churn_rate = round((churned_count / total_customers) * 100, 2)

    # Averages
    avg_monthly_charges = round(df["MonthlyCharges"].mean(), 2)
    avg_tenure = round(df["tenure"].mean(), 1)

    # Return summary dictionary
    return {
        "total_customers": total_customers,
        "total_features": total_features,
        "churned_count": churned_count,
        "retained_count": retained_count,
        "churn_rate": churn_rate,
        "avg_monthly_charges": avg_monthly_charges,
        "avg_tenure": avg_tenure,
    }


def get_churn_by_category(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Calculate the churn rate for each unique value in a given column.
    """

    # Step 1 — Count total customers per category
    total = df.groupby(column).size().rename("total")

    # Step 2 — Count churned customers per category
    churned = (
        df[df["Churn"] == "Yes"]
        .groupby(column)
        .size()
        .rename("churned")
    )

    # Step 3 — Combine totals and churned counts
    result = pd.concat([total, churned], axis=1).fillna(0)

    # Ensure churned is integer (after fillna it may become float)
    result["churned"] = result["churned"].astype(int)

    # Step 4 — Calculate churn rate
    result["churn_rate"] = round(
        (result["churned"] / result["total"]) * 100,
        2,
    )

    # Step 5 — Return result
    return result


def get_top_churn_segments(df: pd.DataFrame) -> str:
    """
    Identify and format the top customer segments with the highest churn rates.
    """

    lines = ["Highest churn segments:"]

    analyses = [
        ("Contract", "Contract"),
        ("Internet Service", "InternetService"),
        ("Payment Method", "PaymentMethod"),
    ]

    for label, column in analyses:
        result = get_churn_by_category(df, column)

        # Category with highest churn rate
        top_category = result["churn_rate"].idxmax()
        top_rate = result.loc[top_category, "churn_rate"]

        lines.append(
            f" - {label}: {top_category} ({top_rate:.2f}% churn rate)"
        )

    return "\n".join(lines)


def format_report(
    summary: dict,
    churn_by_contract: pd.DataFrame,
    churn_by_internet: pd.DataFrame,
    top_segments: str,
) -> str:
    """
    Combine all analysis results into a formatted text report.
    """

    report = f"""
==========================================
TELCO CUSTOMER CHURN — SUMMARY REPORT
==========================================

1. DATASET OVERVIEW
-------------------
Total Customers    : {summary['total_customers']:,}
Total Features     : {summary['total_features']:,}
Churned Customers  : {summary['churned_count']:,}
Retained Customers : {summary['retained_count']:,}
Overall Churn Rate : {summary['churn_rate']:.2f}%
Avg Monthly Charges: ${summary['avg_monthly_charges']:.2f}
Avg Customer Tenure: {summary['avg_tenure']:.1f} months

2. CHURN BY CONTRACT TYPE
-------------------------
{churn_by_contract.to_string()}

3. CHURN BY INTERNET SERVICE
----------------------------
{churn_by_internet.to_string()}

4. KEY FINDINGS
---------------
{top_segments}

==========================================
""".strip("\n")

    return report


def save_report(report: str) -> None:
    """
    Save the report to a text file.
    """

    # Create directory if it does not exist
    import os

    os.makedirs(REPORTS_PATH, exist_ok=True)

    # Write report to file
    with open(
        REPORTS_PATH + "churn_summary_report.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(report)


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

    report = format_report(
        summary,
        churn_by_contract,
        churn_by_internet,
        top_segments,
    )

    save_report(report)

    print(f"  Report saved to {REPORTS_PATH}churn_summary_report.txt")
    print("Reporting complete!")