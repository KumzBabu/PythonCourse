# Day 10 Capstone: Real-World Data Pipeline Service

A production-grade Python application that demonstrates everything learned
across the 10-day intensive: data wrangling, APIs, databases, error handling,
logging, testing, and async programming.

## What It Does
- Fetches live data from multiple free public APIs
- Cleans and enriches the data with pandas
- Stores results in SQLite with full transaction safety
- Exposes a simple CLI interface
- Fully tested with pytest (>80% coverage target)
- Structured logging throughout

## Project Structure
```
day10_capstone_project/
├── src/
│   ├── __init__.py
│   ├── fetcher.py        # Async HTTP fetching (aiohttp / requests)
│   ├── transformer.py    # Pandas data cleaning & enrichment
│   ├── storage.py        # SQLite persistence layer
│   ├── reporter.py       # Summary & report generation
│   └── cli.py            # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_fetcher.py
│   ├── test_transformer.py
│   └── test_storage.py
├── config/
│   ├── settings.py       # Centralised configuration
│   └── logging.conf      # Logging configuration
├── requirements.txt
└── README.md
```

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
# Full pipeline
python -m src.cli run

# Fetch only
python -m src.cli fetch --source users

# Generate report
python -m src.cli report
```

## Test
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

## Skills Applied
| Module | Applied in |
|--------|------------|
| 08 pandas | `transformer.py` |
| 09 requests/aiohttp | `fetcher.py` |
| 10 SQLite | `storage.py` |
| 11 logging / errors | All modules |
| 12 pytest | `tests/` |
| 13 async | `fetcher.py` |
