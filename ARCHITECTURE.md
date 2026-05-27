# Python Intensive — 10-Day Curriculum Architecture

## 🗺 Learning Path Overview

```
WEEK 1: FOUNDATIONS → DATA → INTEGRATION
──────────────────────────────────────────
Day 1  │ 01_basics + 02_control_flow      → Syntax, flow control
Day 2  │ 03_functions + 04_data_structures → Functions, comprehensions
Day 3  │ 05_oop + 06_modules_and_files    → OOP, file I/O, imports
Day 4  │ 08_pandas_data_wrangling         → Data analysis
Day 5  │ 09_apis_and_requests             → HTTP, REST APIs
Day 6  │ 10_databases_sql                 → SQLite, SQL
Day 7  │ 07_projects/01_data_pipeline     → MINI-PROJECT (Days 4-6)
Day 8  │ 11_error_handling + 12_testing   → Production quality
Day 9  │ 13_optimization_async            → Performance
Day 10 │ day10_capstone_project           → Full app
```

## 📦 Module Map

| # | Module | Day | Key Concepts | Files |
|---|--------|-----|-------------|-------|
| 01 | Basics | 1 | Variables, types, strings, I/O | lesson.py, exercises.py |
| 02 | Control Flow | 1 | if/elif, for, while, match | lesson.py, exercises.py |
| 03 | Functions | 2 | def, \*args, \*\*kwargs, decorators, closures | lesson.py, exercises.py |
| 04 | Data Structures | 2 | list/dict/set/tuple, comprehensions | lesson.py, exercises.py |
| 05 | OOP | 3 | Classes, inheritance, dunder methods | lesson.py, exercises.py |
| 06 | Modules & Files | 3 | import, pathlib, venv, JSON/CSV | lesson.py, exercises.py |
| 07 | Projects | varies | Integrated projects | 01_data_pipeline/ |
| **08** | **Pandas** | **4** | **DataFrame, groupby, merge, pivot** | **lesson.py, exercises.py, dataset.csv** |
| **09** | **APIs** | **5** | **requests, auth, error handling, sessions** | **lesson.py, exercises.py, examples/** |
| **10** | **Databases** | **6** | **SQLite, SQL, joins, transactions** | **lesson.py, exercises.py** |
| **11** | **Errors+Logging** | **8** | **try/except, custom exceptions, logging** | **lesson.py, exercises.py, config/** |
| **12** | **Testing** | **8** | **pytest, fixtures, parametrize, mock** | **lesson.py, test_examples.py** |
| **13** | **Optimization** | **9** | **async/await, threading, lru_cache** | **lesson.py, exercises.py, benchmarks/** |
| **D10** | **Capstone** | **10** | **Full app: fetch+transform+store+test** | **src/, tests/, config/** |

> **Bold** = new modules added in this roadmap expansion

## 🔗 Dependency Graph

```
01_basics
    └─► 02_control_flow
            └─► 03_functions ─────────────────────────────────┐
            └─► 04_data_structures ───────────────────────────┤
                    └─► 05_oop ────────────────────────────────┤
                    └─► 06_modules_and_files ──────────────────┤
                                │                              │
                                ▼                              │
                    08_pandas_data_wrangling                   │
                    09_apis_and_requests      ──► 07_projects/01_data_pipeline
                    10_databases_sql                           │
                                │                              │
                                ▼                              ▼
                    11_error_handling_logging          day10_capstone_project
                    12_testing                                 ▲
                    13_optimization_async ─────────────────────┘
```

## 🎯 Skills Progression

### After Day 3 (Basics complete)
- Write clean, Pythonic code
- Use OOP to model real problems
- Read/write files, work with JSON/CSV

### After Day 6 (Data stack)
- Wrangle datasets with pandas
- Call any REST API reliably
- Query and update databases with SQL

### After Day 8 (Production quality)
- Write code that handles failures gracefully
- Log events properly at every level
- Write tests that give you confidence to refactor

### After Day 10 (Full-stack Python)
- Build a complete data pipeline from scratch
- Profile and optimize bottlenecks
- Write async code for high-concurrency scenarios

## 📚 Resources
- [Official Python docs](https://docs.python.org/3/)
- [pandas docs](https://pandas.pydata.org/docs/)
- [pytest docs](https://docs.pytest.org/)
- [Real Python](https://realpython.com/)
- [asyncio guide](https://docs.python.org/3/library/asyncio.html)
