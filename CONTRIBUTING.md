# Contributing Guide — Telco Customer Churn Project

Welcome to the team! This guide walks you through exactly how to contribute your code using Git and GitHub. Follow these steps carefully — this is the same workflow used by professional developers every day.

---

## Initial Setup (do this once)

### 1. Clone the repository

```bash
git clone <repo-url>
cd telco-churn-collab
```

### 2. Set up your Python environment

**Using Anaconda?** You're already done. Anaconda's base environment includes pandas and matplotlib — just make sure it's activated and skip to step 4.

> To check: run `conda activate base` (or whatever your DS environment is named), then `python -c "import pandas; import matplotlib"`. If no error, you're good.

**Not using Anaconda?** Create a virtual environment:

### 2a. Create a virtual environment

A virtual environment keeps your project's packages isolated from your system Python.

```bash
python -m venv .venv
```

Activate it:
- **Mac/Linux:** `source .venv/bin/activate`
- **Windows:** `.venv\Scripts\activate`

> You'll need to activate it every time you open a new terminal.

### 3. Install the required packages (venv only — skip if using Anaconda)

```bash
pip install -r requirements.txt
```

### 4. Verify everything works

```bash
python main.py
```

Expected output:
```
==================================================
  Telco Customer Churn Analysis Pipeline
==================================================

==================================================
  Pipeline complete!
==================================================
```

If you see this, your setup is complete. If you see an error, ask your instructor before continuing.

---

## Your Workflow (follow these steps every time you work)

### Step 1: Always start from the latest main branch

Before you do anything, make sure you have the latest version of the project:

```bash
git checkout main
git pull origin main
```

This ensures you're building on top of everyone else's latest merged work, not an outdated version.

### Step 2: Create your feature branch

Each contributor works on their own branch. Create yours like this (replace `<your-role>` with your actual role):

```bash
git checkout -b feature/data-cleaning      # Contributor A
git checkout -b feature/eda                # Contributor B
git checkout -b feature/feature-engineering  # Contributor C
git checkout -b feature/reporting          # Contributor D
```

You only need to do this once. After that, you'll already be on your branch.

> **What is a branch?** A branch is like your own personal copy of the project. You can make changes without affecting anyone else's work. When you're done, you'll merge your branch back into `main` via a Pull Request.

### Step 3: Do your work

Open your assigned file and implement the functions:

| Your Role | Your File |
|-----------|-----------|
| Contributor A | `src/data_cleaning.py` |
| Contributor B | `src/eda.py` |
| Contributor C | `src/feature_engineering.py` |
| Contributor D | `src/reporting.py` |

Read the docstrings carefully — they explain exactly what each function should do, what arguments it takes, what it should return, and provide hints on how to implement it.

### Step 4: Test your code

After implementing your functions, run the main script to check for errors:

```bash
python main.py
```

As pipeline steps get completed and merged, more sections will be uncommented in `main.py`. For now, focus on making sure your file has no syntax errors (you can import it directly to test):

```bash
python -c "from src.data_cleaning import run_cleaning_pipeline"   # Contributor A
python -c "from src.eda import run_eda_pipeline"                  # Contributor B
python -c "from src.feature_engineering import run_feature_engineering_pipeline"  # Contributor C
python -c "from src.reporting import run_reporting_pipeline"      # Contributor D
```

If this runs with no output, your file imports correctly.

### Step 5: Stage and commit your changes

When you've finished implementing your functions (or made meaningful progress), save your work with a commit:

```bash
# Stage only your file (don't add other people's files by accident)
git add src/data_cleaning.py        # Contributor A
git add src/eda.py                  # Contributor B
git add src/feature_engineering.py  # Contributor C
git add src/reporting.py            # Contributor D

# If you also added something to utils.py:
git add src/utils.py

# Commit with a clear message
git commit -m "Implement fix_total_charges and fix_senior_citizen functions"
```

You can (and should!) make multiple commits as you work — don't wait until you're completely done.

### Step 6: Push your branch to GitHub

Upload your branch so your instructor can see it:

```bash
git push origin feature/data-cleaning      # Contributor A
git push origin feature/eda                # Contributor B
git push origin feature/feature-engineering  # Contributor C
git push origin feature/reporting          # Contributor D
```

You can push as many times as you want — each push just updates your branch on GitHub.

### Step 7: Open a Pull Request

1. Go to the repository on GitHub
2. You should see a banner saying **"Your branch had recent pushes"** — click **"Compare & pull request"**
3. Fill in the PR form:
   - **Title:** Something descriptive like `"Implement data cleaning pipeline (Contributor A)"`
   - **Description:** Briefly describe what you implemented and any decisions you made
4. Click **"Create pull request"**

> A Pull Request (PR) is how you ask the instructor to review your code and merge it into `main`. Think of it as saying: "I'm done with my part — please check it!"

### Step 8: Wait for review

Your instructor will review your code and either:
- **Approve and merge it** — great job! Your code is now in `main`.
- **Request changes** — they'll leave comments explaining what to fix. Make the changes on your branch, commit, and push again. The PR will update automatically.

---

## Commit Message Guidelines

A good commit message tells your teammates (and your future self) what you did and why.

**Format:** Start with a verb, be specific.

| Good | Bad |
|------|-----|
| `Implement drop_customer_id and fix_total_charges functions` | `did stuff` |
| `Fix TotalCharges conversion — replace blank strings with 0` | `changes` |
| `Add plot_churn_by_contract visualization` | `update eda` |
| `Update docstring for encode_binary_columns` | `fix` |

**Quick rule:** If you can't describe what you did in one sentence, your commit might be too large — consider breaking it into smaller commits.

---

## If You Need to Update Your Branch

If someone else's PR was merged into `main` while you were working, you'll want to bring those changes into your branch. Here's how:

```bash
# 1. Switch to main and get the latest changes
git checkout main
git pull origin main

# 2. Switch back to your branch
git checkout feature/data-cleaning   # (or your branch name)

# 3. Merge main into your branch
git merge main
```

Most of the time this will work automatically. If you see a message like:

```
CONFLICT (content): Merge conflict in src/utils.py
```

That means two people edited the same part of the same file. **Don't panic — just ask your instructor.** They'll help you resolve it. Merge conflicts are normal and a core part of learning collaborative development.

---

## Important Rules

**Only edit your assigned file.** Every contributor owns exactly one file:

| Your File | Don't Touch |
|-----------|------------|
| `src/data_cleaning.py` | `src/eda.py`, `src/feature_engineering.py`, `src/reporting.py` |
| `src/eda.py` | `src/data_cleaning.py`, `src/feature_engineering.py`, `src/reporting.py` |
| `src/feature_engineering.py` | `src/data_cleaning.py`, `src/eda.py`, `src/reporting.py` |
| `src/reporting.py` | `src/data_cleaning.py`, `src/eda.py`, `src/feature_engineering.py` |

**Everyone can edit `src/utils.py`** — but coordinate with your team first! If two people add functions at the same time, you might get a merge conflict. Use your group chat to say "I'm adding something to utils.py" before you do it.

**Don't commit the data files.** The dataset is already in the repo. Git will ignore your generated files (`data/cleaned/`, `outputs/`) automatically via `.gitignore`.

**Don't use `git push --force`.** This can overwrite other people's work. If you feel like you need to force push, ask your instructor first.

**Ask if you're unsure.** It's always better to ask than to guess and create a problem. There are no dumb questions — Git is confusing at first for everyone.

---

## Quick Reference

```bash
# See what branch you're on and what files you've changed
git status

# See your recent commits
git log --oneline

# Undo changes to a file (careful — this erases your edits!)
git checkout -- src/data_cleaning.py

# See the difference between your changes and the last commit
git diff src/data_cleaning.py
```
