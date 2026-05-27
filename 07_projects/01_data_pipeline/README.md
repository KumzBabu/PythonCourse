# Mini-Project: Data Pipeline
**Days 4–6 | Modules 8, 9, 10**

## Overview
Build an end-to-end data pipeline that:
1. Fetches employee/company data from a public API
2. Cleans and transforms it with pandas
3. Stores results in a SQLite database
4. Generates a summary report

## Tasks

### Step 1 — Fetch Data (Module 9)
- Use `requests` to pull data from JSONPlaceholder or Open-Meteo
- Handle errors and timeouts gracefully

### Step 2 — Clean & Transform (Module 8)
- Load into a pandas DataFrame
- Handle missing values
- Add computed columns (e.g. categorise by salary range)
- Export cleaned CSV

### Step 3 — Store to Database (Module 10)
- Create tables: `users`, `posts`, `summary`
- Insert cleaned records using parameterised queries
- Use transactions

### Step 4 — Report
- Query the DB to generate a text summary
- Print stats: total records, avg values, top items

## Files
- `pipeline.py`  — main script (create this!)
- `output/`      — generated CSVs and reports

## Run
```bash
pip install requests pandas
python pipeline.py
```
