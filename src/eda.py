"""
Exploratory Data Analysis Module — Contributor B

Your job: Load the cleaned dataset and create visualizations that help
us understand the data and the churn patterns.

Save all figures to: outputs/figures/

You'll create 4 visualizations:
1. Churn distribution (how many customers churned vs stayed)
2. Monthly charges distribution by churn status
3. Churn rate by contract type
4. Churn rate by internet service type
"""

import pandas as pd
import matplotlib.pyplot as plt
from src.utils import load_cleaned_data, FIGURES_PATH


def plot_churn_distribution(df: pd.DataFrame) -> None:
    """
    Create a bar chart showing the count of churned vs non-churned customers.

    The chart should have:
    - Title: "Customer Churn Distribution"
    - X-axis label: "Churn" (the tick labels 'No' and 'Yes' come from the data automatically)
    - Y-axis label: "Number of Customers"
    - Different colors for each bar (matplotlib does this automatically with kind='bar')

    Save to: outputs/figures/churn_distribution.png

    Args:
        df: The cleaned dataframe with a 'Churn' column.

    Example:
        >>> plot_churn_distribution(df)
        # Saves a bar chart to outputs/figures/churn_distribution.png
    """
    # TODO:
    # 1. Count the values in the 'Churn' column using df['Churn'].value_counts()
    # 2. Create a bar chart using .plot(kind='bar', rot=0)
    #    (rot=0 keeps the x-axis labels horizontal — easier to read!)
    # 3. Add a title using plt.title(...)
    # 4. Add axis labels using plt.xlabel(...) and plt.ylabel(...)
    # 5. Save using plt.savefig(FIGURES_PATH + 'churn_distribution.png', bbox_inches='tight')
    # 6. Close the figure with plt.close() — important so figures don't stack up in memory!
    pass


def plot_monthly_charges_by_churn(df: pd.DataFrame) -> None:
    """
    Create a histogram comparing monthly charges for churned vs non-churned customers.

    The chart should have:
    - Title: "Monthly Charges Distribution by Churn Status"
    - X-axis label: "Monthly Charges ($)"
    - Y-axis label: "Number of Customers"
    - Two overlapping histograms (one for Churn=Yes, one for Churn=No)
    - A legend showing which color is which
    - Use alpha=0.5 so both histograms are visible through each other

    Save to: outputs/figures/monthly_charges_by_churn.png

    Args:
        df: The cleaned dataframe.

    Hints:
        - Separate the data into two groups first:
            churned = df[df['Churn'] == 'Yes']['MonthlyCharges']
            retained = df[df['Churn'] == 'No']['MonthlyCharges']
        - Call plt.hist() twice — once for each group — with alpha=0.5 and a label
        - Use plt.legend() to show the legend after plotting both histograms
        - Use bins=30 to get a nice-looking histogram
    """
    # TODO: Implement this visualization
    pass


def plot_churn_by_contract(df: pd.DataFrame) -> None:
    """
    Create a bar chart showing the churn RATE (percentage) for each contract type.

    The chart should have:
    - Title: "Churn Rate by Contract Type"
    - X-axis: Contract types (Month-to-month, One year, Two year)
    - Y-axis label: "Churn Rate (%)"
    - The churn rate as a percentage (0 to 100, e.g., 42.71 not 0.4271)

    Save to: outputs/figures/churn_by_contract.png

    Args:
        df: The cleaned dataframe.

    Hints:
        - The trick: create a boolean column first, then group and average it.
          (df['Churn'] == 'Yes') gives True/False for each row.
          The mean of True/False values is the proportion (e.g., 0.4271).
          Multiply by 100 to get a percentage.
        - In one line:
          churn_rates = df.groupby('Contract').apply(lambda x: (x['Churn'] == 'Yes').mean() * 100)
        - Then plot with churn_rates.plot(kind='bar', rot=15)
    """
    # TODO: Implement this visualization
    pass


def plot_churn_by_internet_service(df: pd.DataFrame) -> None:
    """
    Create a bar chart showing the churn RATE for each internet service type.

    The chart should have:
    - Title: "Churn Rate by Internet Service Type"
    - X-axis: Internet service types (DSL, Fiber optic, No)
    - Y-axis label: "Churn Rate (%)"

    Save to: outputs/figures/churn_by_internet_service.png

    Args:
        df: The cleaned dataframe.

    Hints:
        - Same approach as plot_churn_by_contract, but group by 'InternetService'
        - Use rot=0 since the labels are short enough to be horizontal
    """
    # TODO: Implement this visualization
    pass


def run_eda_pipeline() -> None:
    """
    Run all EDA visualizations and save them.

    This is the main function that creates all plots.
    """
    print("Starting Exploratory Data Analysis...")
    df = load_cleaned_data()
    print(f"  Loaded cleaned data: {len(df)} rows")

    plot_churn_distribution(df)
    print("  Saved: churn_distribution.png")

    plot_monthly_charges_by_churn(df)
    print("  Saved: monthly_charges_by_churn.png")

    plot_churn_by_contract(df)
    print("  Saved: churn_by_contract.png")

    plot_churn_by_internet_service(df)
    print("  Saved: churn_by_internet_service.png")

    print("EDA complete! Check outputs/figures/ for all plots.")
