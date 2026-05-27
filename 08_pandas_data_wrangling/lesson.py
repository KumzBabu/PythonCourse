# ============================================================
# MODULE 8: Pandas & Data Wrangling
# Day 4 of 10-Day Python Intensive
# ============================================================
# pip install pandas matplotlib seaborn
# ============================================================

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# 1. LOADING DATA
# ─────────────────────────────────────────────

# Read CSV
df = pd.read_csv("dataset.csv")

print("── Shape ──")
print(df.shape)          # (rows, columns)

print("\n── First 5 rows ──")
print(df.head())

print("\n── Data types ──")
print(df.dtypes)

print("\n── Quick stats ──")
print(df.describe())


# ─────────────────────────────────────────────
# 2. SELECTING & FILTERING
# ─────────────────────────────────────────────

# Select a single column → Series
ages = df["age"]

# Select multiple columns → DataFrame
subset = df[["name", "department", "salary"]]

# Filter rows where salary > 90,000
high_earners = df[df["salary"] > 90_000]
print("\n── High earners ──")
print(high_earners[["name", "salary"]])

# Combine conditions  (& = AND,  | = OR)
eng_seniors = df[(df["department"] == "Engineering") & (df["age"] > 35)]
print("\n── Senior Engineers ──")
print(eng_seniors[["name", "age", "salary"]])

# .query() — more readable for complex filters
top_performers = df.query("performance_score >= 4.5 and salary > 100000")
print("\n── Top performers with high salary ──")
print(top_performers[["name", "performance_score", "salary"]])


# ─────────────────────────────────────────────
# 3. CLEANING DATA
# ─────────────────────────────────────────────

# Introduce some NaN values for demonstration
df_messy = df.copy()
df_messy.loc[[2, 7, 14], "salary"] = None
df_messy.loc[[5, 12], "performance_score"] = None

# Check for nulls
print("\n── Null counts ──")
print(df_messy.isnull().sum())

# Fill NaN with column mean
df_messy["salary"] = df_messy["salary"].fillna(df_messy["salary"].mean())

# Drop rows with any remaining NaN
df_clean = df_messy.dropna()

# Convert column types
df["hire_date"] = pd.to_datetime(df["hire_date"])
df["hire_year"] = df["hire_date"].dt.year

# Rename columns
df.rename(columns={"performance_score": "score"}, inplace=True)

# Strip whitespace from string columns
df["department"] = df["department"].str.strip()

print("\n── After cleaning (dtypes) ──")
print(df.dtypes)


# ─────────────────────────────────────────────
# 4. TRANSFORMING DATA
# ─────────────────────────────────────────────

# Add a computed column
df["salary_monthly"] = (df["salary"] / 12).round(2)

# Apply a custom function to a column
def classify_salary(sal):
    if sal < 70_000:   return "Junior"
    elif sal < 100_000: return "Mid"
    else:              return "Senior"

df["level"] = df["salary"].apply(classify_salary)

# map() — replace values using a dict
dept_code = {"Engineering": "ENG", "Marketing": "MKT",
             "Sales": "SLS", "HR": "HR", "Management": "MGT"}
df["dept_code"] = df["department"].map(dept_code)

# String operations
df["first_name"] = df["name"].str.split().str[0]
df["name_upper"] = df["name"].str.upper()

print("\n── Transformed columns ──")
print(df[["name", "level", "dept_code", "salary_monthly"]].head())


# ─────────────────────────────────────────────
# 5. GROUPBY & AGGREGATION
# ─────────────────────────────────────────────

# Basic groupby
dept_summary = df.groupby("department")["salary"].agg(
    count="count",
    mean="mean",
    min="min",
    max="max"
).round(2)
print("\n── Department salary summary ──")
print(dept_summary)

# Multiple column groupby
city_dept = df.groupby(["city", "department"]).agg(
    headcount=("name", "count"),
    avg_score=("score", "mean")
).round(2)
print("\n── City + Department breakdown ──")
print(city_dept.head(10))

# transform() — keeps the same index (useful for adding group stats back)
df["dept_avg_salary"] = df.groupby("department")["salary"].transform("mean")
df["salary_vs_avg"] = (df["salary"] - df["dept_avg_salary"]).round(2)

print("\n── Salary vs dept average ──")
print(df[["name", "department", "salary", "dept_avg_salary", "salary_vs_avg"]].head(8))


# ─────────────────────────────────────────────
# 6. SORTING & RANKING
# ─────────────────────────────────────────────

# Sort by salary descending
top5 = df.sort_values("salary", ascending=False).head(5)
print("\n── Top 5 earners ──")
print(top5[["name", "department", "salary"]])

# Rank within department
df["dept_salary_rank"] = df.groupby("department")["salary"].rank(ascending=False)
print("\n── Department salary rank ──")
print(df[["name", "department", "salary", "dept_salary_rank"]].sort_values(
    ["department", "dept_salary_rank"]).head(10))


# ─────────────────────────────────────────────
# 7. MERGING & JOINING
# ─────────────────────────────────────────────

# Create a second DataFrame to merge with
dept_info = pd.DataFrame({
    "department": ["Engineering", "Marketing", "Sales", "HR", "Management"],
    "budget_million": [5.2, 1.8, 2.5, 0.9, 3.1],
    "floor": [3, 2, 1, 2, 4]
})

merged = df.merge(dept_info, on="department", how="left")
print("\n── Merged with dept info ──")
print(merged[["name", "department", "salary", "budget_million"]].head(6))

# concat — stacking DataFrames
df_part1 = df.iloc[:12]
df_part2 = df.iloc[12:]
df_combined = pd.concat([df_part1, df_part2], ignore_index=True)
print(f"\n── Concatenated rows: {len(df_combined)} ──")


# ─────────────────────────────────────────────
# 8. PIVOT TABLES
# ─────────────────────────────────────────────

pivot = df.pivot_table(
    values="salary",
    index="department",
    columns="level",
    aggfunc="mean",
    fill_value=0
).round(0)
print("\n── Pivot: avg salary by dept & level ──")
print(pivot)


# ─────────────────────────────────────────────
# 9. EXPORTING DATA
# ─────────────────────────────────────────────

# Save to CSV (no index)
df.to_csv("output_cleaned.csv", index=False)

# Save to JSON
df[["name", "department", "salary"]].to_json("output_sample.json",
                                               orient="records", indent=2)

print("\n── Files exported: output_cleaned.csv, output_sample.json ──")


# ─────────────────────────────────────────────
# 10. KEY TAKEAWAYS
# ─────────────────────────────────────────────
"""
PANDAS QUICK REFERENCE
══════════════════════
Load         : pd.read_csv(), pd.read_json(), pd.read_excel()
Inspect      : .head(), .tail(), .info(), .describe(), .dtypes
Select       : df["col"], df[["a","b"]], df.iloc[], df.loc[]
Filter       : df[condition], df.query("expr")
Clean        : .fillna(), .dropna(), .astype(), .str.strip()
Transform    : .apply(), .map(), .assign(), string ops via .str
Group        : .groupby().agg(), .groupby().transform()
Sort/Rank    : .sort_values(), .rank()
Merge        : .merge(), pd.concat()
Pivot        : .pivot_table()
Export       : .to_csv(), .to_json(), .to_excel()
"""
