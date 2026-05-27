# ============================================================
# MODULE 8: Pandas Exercises
# ============================================================
# Run: python exercises.py
# Dataset: dataset.csv (same folder)
# ============================================================

import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
df["hire_date"] = pd.to_datetime(df["hire_date"])
df["performance_score"] = df["performance_score"].astype(float)


# ── EXERCISE 1 ──────────────────────────────────────────────
# Filter all employees from "San Francisco" who earn more
# than the overall average salary. Print their names & salaries.
print("=" * 50)
print("Exercise 1: SF employees above average salary")
print("=" * 50)

# YOUR CODE HERE ↓
avg_salary = None   # compute overall average
sf_above_avg = None # filter
# print(sf_above_avg[["name", "salary"]])


# ── EXERCISE 2 ──────────────────────────────────────────────
# Create a new column "years_at_company" (as of 2025-01-01).
# Find the 3 employees with the most years at the company.
print("\n" + "=" * 50)
print("Exercise 2: Longest-tenured employees")
print("=" * 50)

# YOUR CODE HERE ↓
reference_date = pd.Timestamp("2025-01-01")
# df["years_at_company"] = ...
# top3 = ...
# print(top3[["name", "hire_date", "years_at_company"]])


# ── EXERCISE 3 ──────────────────────────────────────────────
# Group by department and compute:
#   - headcount, average salary, min score, max score
# Sort result by average salary descending.
print("\n" + "=" * 50)
print("Exercise 3: Department summary table")
print("=" * 50)

# YOUR CODE HERE ↓
# dept_summary = df.groupby("department")...
# print(dept_summary)


# ── EXERCISE 4 ──────────────────────────────────────────────
# Identify the top performer (highest performance_score) in
# EACH department. Print their name, dept, and score.
print("\n" + "=" * 50)
print("Exercise 4: Top performer per department")
print("=" * 50)

# YOUR CODE HERE ↓
# Hint: groupby + idxmax  OR  sort_values + drop_duplicates
# top_per_dept = ...
# print(top_per_dept[["name", "department", "performance_score"]])


# ── EXERCISE 5 ──────────────────────────────────────────────
# Add a column "bonus" based on performance_score:
#   score >= 4.5  →  15% of salary
#   score >= 4.0  →  10% of salary
#   score >= 3.5  →  5%  of salary
#   below 3.5     →  0
# Print total bonus payout per department.
print("\n" + "=" * 50)
print("Exercise 5: Bonus calculation")
print("=" * 50)

# YOUR CODE HERE ↓
# def calc_bonus(row): ...
# df["bonus"] = df.apply(calc_bonus, axis=1)
# bonus_by_dept = ...
# print(bonus_by_dept)


# ── EXERCISE 6 ──────────────────────────────────────────────
# Create a pivot table:
#   rows    = city
#   columns = department
#   values  = average salary (round to nearest $1000)
#   fill missing with 0
print("\n" + "=" * 50)
print("Exercise 6: Pivot — avg salary by city & dept")
print("=" * 50)

# YOUR CODE HERE ↓
# pivot = pd.pivot_table(...)
# print(pivot)


# ── EXERCISE 7 (CHALLENGE) ──────────────────────────────────
# Detect salary "outliers" within each department using the
# IQR method (values < Q1 - 1.5*IQR  or  > Q3 + 1.5*IQR).
# Print any outlier employees found.
print("\n" + "=" * 50)
print("Exercise 7 (Challenge): Salary outliers per dept")
print("=" * 50)

# YOUR CODE HERE ↓
def find_outliers(group):
    Q1 = group["salary"].quantile(0.25)
    Q3 = group["salary"].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    return group[(group["salary"] < lower) | (group["salary"] > upper)]

# outliers = df.groupby("department", group_keys=False).apply(find_outliers)
# print(outliers[["name", "department", "salary"]] if not outliers.empty else "No outliers found")


# ── EXPECTED OUTPUT HINTS ───────────────────────────────────
"""
Ex1: Should find employees like Carol White, Frank Miller, Karen Anderson, etc.
Ex2: Tina Walker, Frank Miller, Karen Anderson (hired earliest)
Ex3: Management has highest avg salary
Ex4: Tina Walker leads Management, Carol White leads Engineering
Ex5: Total bonus for Engineering should be largest
Ex6: Pivot shows NaN/0 where no employees in that city+dept combo
Ex7: Depends on data distribution — small dataset may show none
"""
