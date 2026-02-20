import pandas as pd
import matplotlib.pyplot as plt
from src.utils import load_cleaned_data, FIGURES_PATH


def plot_churn_distribution(df: pd.DataFrame) -> None:
    churn_counts=df["Churn"].value_counts()
    churn_counts.plot(kind="bar",rot=0)
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.savefig(FIGURES_PATH + 'churn_distribution.png', bbox_inches='tight')
    plt.close()


def plot_monthly_charges_by_churn(df: pd.DataFrame) -> None:
    churned=df[df["Churn"]=="Yes"]["MonthlyCharges"]
    retained=df[df["Churn"]=="No"]["MonthlyCharges"]
    plt.hist(churned,alpha=0.5,label="Churned",bins=30)
    plt.hist(retained,alpha=0.5,label="Retained",bins=30)
    plt.title("Monthly Charges Distribution by Churn Status")
    plt.xlabel("Monthly Charges ($)")
    plt.ylabel("Number of Customers")
    plt.legend()
    plt.savefig(FIGURES_PATH + 'monthly_charges_by_churn.png', bbox_inches='tight')
    plt.close()
    

def plot_churn_by_contract(df: pd.DataFrame) -> None:
    churn_rates=df.groupby("Contract").apply(lambda x: (x["Churn"]=="Yes").mean()*100,include_groups="False")
    churn_rates.plot(kind="bar",rot=15)
    plt.title("Churn Rate by Contract Type")
    plt.xlabel("Contract types (Month-to-month, One year, Two year)")
    plt.ylabel("Churn Rate (%)")
    plt.savefig(FIGURES_PATH + 'churn_by_contract.png', bbox_inches='tight')
    plt.close() 
       



def plot_churn_by_internet_service(df: pd.DataFrame) -> None:
    churn_rates=df.groupby("InternetService").apply(lambda x: (x["Churn"]=="Yes").mean()*100,include_groups="False")
    churn_rates.plot(kind="bar",rot=0)
    plt.title("Churn Rate by Internet Service Type")
    plt.xlabel("Internet service types (DSL, Fiber optic, No)")
    plt.ylabel("Churn Rate (%)")
    plt.savefig(FIGURES_PATH + 'churn_by_internet_service.png', bbox_inches='tight')
    plt.close()  
    



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
