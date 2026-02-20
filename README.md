# Telco Customer Churn — Collaborative Analysis Project

Welcome! This is a team project where you'll analyze a real-world telecom dataset to understand why customers leave (or stay). You'll each own one part of the codebase, submit your work via Pull Requests, and practice the Git workflow used by professional data science teams.

---

## Project Overview

A telecommunications company wants to understand what drives customer churn — when a customer stops using their service. By analyzing patterns in customer data, we can identify which customers are at risk and why.

This project is structured as a collaborative exercise:
- **You** implement the functions in your assigned file
- **Your instructor** reviews your Pull Request and merges it into the main codebase
- **Together**, the four pipeline steps combine into a complete analysis

---

## Dataset Description

**File:** `data/raw/telco_churn.csv`
**Source:** IBM Telco Customer Churn dataset (7,043 customers, 21 columns)

Each row is one customer. Here's what each column means:

### Demographics
| Column | Description |
|--------|-------------|
| `customerID` | Unique customer identifier (not useful for analysis) |
| `gender` | Customer gender: `Female` or `Male` |
| `SeniorCitizen` | Whether the customer is a senior citizen: `0` = No, `1` = Yes |
| `Partner` | Whether the customer has a partner: `Yes` or `No` |
| `Dependents` | Whether the customer has dependents: `Yes` or `No` |

### Account Information
| Column | Description |
|--------|-------------|
| `tenure` | How many months the customer has been with the company |
| `Contract` | Contract type: `Month-to-month`, `One year`, or `Two year` |
| `PaperlessBilling` | Whether the customer uses paperless billing: `Yes` or `No` |
| `PaymentMethod` | How the customer pays: `Electronic check`, `Mailed check`, `Bank transfer (automatic)`, or `Credit card (automatic)` |
| `MonthlyCharges` | The amount charged each month (dollars) |
| `TotalCharges` | Total amount charged over the customer's lifetime (dollars) |

### Services
| Column | Description |
|--------|-------------|
| `PhoneService` | Whether the customer has phone service: `Yes` or `No` |
| `MultipleLines` | Whether the customer has multiple phone lines: `Yes`, `No`, or `No phone service` |
| `InternetService` | Internet service type: `DSL`, `Fiber optic`, or `No` |
| `OnlineSecurity` | Whether the customer has online security add-on: `Yes`, `No`, or `No internet service` |
| `OnlineBackup` | Whether the customer has online backup add-on: `Yes`, `No`, or `No internet service` |
| `DeviceProtection` | Whether the customer has device protection add-on: `Yes`, `No`, or `No internet service` |
| `TechSupport` | Whether the customer has tech support add-on: `Yes`, `No`, or `No internet service` |
| `StreamingTV` | Whether the customer streams TV: `Yes`, `No`, or `No internet service` |
| `StreamingMovies` | Whether the customer streams movies: `Yes`, `No`, or `No internet service` |

### Target Variable
| Column | Description |
|--------|-------------|
| `Churn` | Whether the customer left in the last month: `Yes` or `No` — this is what we're trying to understand |

---

## Team Roles

| Contributor | Branch | Owns | Task |
|-------------|--------|------|------|
| **Contributor A** | `feature/data-cleaning` | `src/data_cleaning.py` | Load the raw CSV, fix data quality issues, and save a clean dataset that everyone else will use |
| **Contributor B** | `feature/eda` | `src/eda.py` | Load the cleaned data and create 4 visualizations exploring churn patterns |
| **Contributor C** | `feature/feature-engineering` | `src/feature_engineering.py` | Transform text categories into numbers and create new useful columns |
| **Contributor D** | `feature/reporting` | `src/reporting.py` | Calculate key statistics and write a formatted summary report |

> All contributors may also add shared helper functions to `src/utils.py` — just coordinate with your team first!

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd telco-churn-collab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:
- **Mac/Linux:** `source .venv/bin/activate`
- **Windows:** `.venv\Scripts\activate`

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Verify everything works

```bash
python main.py
```

You should see:
```
==================================================
  Telco Customer Churn Analysis Pipeline
==================================================

==================================================
  Pipeline complete!
==================================================
```

If you see this, you're all set! The pipeline steps are commented out — each one gets uncommented as contributors finish their work.

---

## Project Workflow

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full step-by-step Git workflow guide — including how to create your branch, commit your work, and open a Pull Request.

---

## Project Structure

```
telco-churn-collab/
├── README.md               ← You are here
├── CONTRIBUTING.md         ← Git workflow guide
├── requirements.txt        ← Python packages to install
├── .gitignore
├── data/
│   ├── raw/
│   │   └── telco_churn.csv         ← Original dataset (do not modify)
│   └── cleaned/
│       └── telco_churn_cleaned.csv ← Created by Contributor A
├── src/
│   ├── utils.py                    ← Shared utilities (everyone can use)
│   ├── data_cleaning.py            ← Contributor A
│   ├── eda.py                      ← Contributor B
│   ├── feature_engineering.py      ← Contributor C
│   └── reporting.py                ← Contributor D
├── outputs/
│   ├── figures/                    ← Plots saved by Contributor B
│   └── reports/                    ← Report saved by Contributor D
└── main.py                         ← Runs the full pipeline
```
