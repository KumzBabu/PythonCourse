# ============================================================
# MODULE 11: Error Handling & Logging — Exercises
# ============================================================

import logging
import json
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)-8s | %(name)s | %(message)s")
logger = logging.getLogger("exercises")


# ── EXERCISE 1 ──────────────────────────────────────────────
# Write a function parse_number(value) that:
#   - tries to convert value to float
#   - returns the float on success
#   - returns 0.0 on ValueError, with a WARNING log
#   - returns None on TypeError, with an ERROR log
print("=" * 55)
print("Exercise 1: parse_number with logging")
print("=" * 55)

def parse_number(value):
    # YOUR CODE HERE ↓
    pass

print(parse_number("3.14"))     # → 3.14
print(parse_number("abc"))      # → 0.0, logs warning
print(parse_number(None))       # → None, logs error
print(parse_number(42))         # → 42.0


# ── EXERCISE 2 ──────────────────────────────────────────────
# Create a custom exception hierarchy:
#   AppError (base)
#     ├── NetworkError   (add: url, status_code attrs)
#     └── ParseError     (add: line_number attr)
# Then write a simulate_fetch(url) function that raises
# NetworkError if url contains "bad" and ParseError if
# url contains "malformed". Test all three paths.
print("\n" + "=" * 55)
print("Exercise 2: Custom exception hierarchy")
print("=" * 55)

# YOUR CODE HERE ↓
class AppError(Exception):
    pass

# class NetworkError(AppError): ...
# class ParseError(AppError): ...

def simulate_fetch(url: str) -> str:
    # YOUR CODE HERE ↓
    pass

for url in ["https://good.api.com/data", "https://bad.api.com", "https://malformed.api.com"]:
    try:
        result = simulate_fetch(url)
        print(f"OK: {result}")
    except AppError as e:
        print(f"AppError [{type(e).__name__}]: {e}")


# ── EXERCISE 3 ──────────────────────────────────────────────
# Write a safe_json_load(path) function that reads a JSON file.
# Use exception chaining:
#   FileNotFoundError  → raise AppError("File not found: path") from e
#   JSONDecodeError    → raise AppError("Invalid JSON: path") from e
# Test with: a valid file, missing file, and invalid JSON.
print("\n" + "=" * 55)
print("Exercise 3: Exception chaining with file I/O")
print("=" * 55)

# Create test files first
Path("valid.json").write_text('{"name": "Alice", "age": 30}')
Path("bad.json").write_text("this is not json {{{{")

def safe_json_load(path: str) -> dict:
    # YOUR CODE HERE ↓
    pass

for p in ["valid.json", "bad.json", "missing.json"]:
    try:
        data = safe_json_load(p)
        print(f"Loaded {p}: {data}")
    except Exception as e:
        print(f"Error loading {p}: {e}")
        if e.__cause__:
            print(f"  Caused by: {e.__cause__}")

# Cleanup
for f in ["valid.json", "bad.json"]:
    Path(f).unlink(missing_ok=True)


# ── EXERCISE 4 ──────────────────────────────────────────────
# Build a RetryError exception and a retry(func, times=3) decorator.
# The decorator retries func up to `times` times on any exception.
# Log each attempt. Raise RetryError if all attempts fail.
print("\n" + "=" * 55)
print("Exercise 4: Retry decorator")
print("=" * 55)

import random

class RetryError(Exception):
    pass

def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # YOUR CODE HERE ↓
            pass
        return wrapper
    return decorator

# Test function that randomly fails
@retry(times=3)
def flaky_api_call():
    if random.random() < 0.7:   # 70% chance of failure
        raise ConnectionError("API unreachable")
    return "Success!"

try:
    result = flaky_api_call()
    print(f"Result: {result}")
except RetryError as e:
    print(f"All retries exhausted: {e}")


# ── EXERCISE 5 ──────────────────────────────────────────────
# Set up a logger that:
#   - writes DEBUG+ to "config/debug.log"
#   - writes WARNING+ to console
# Then log one message at each level and verify behavior.
print("\n" + "=" * 55)
print("Exercise 5: Dual-handler logger")
print("=" * 55)

import sys
Path("config").mkdir(exist_ok=True)

def create_dual_logger(name: str) -> logging.Logger:
    # YOUR CODE HERE ↓
    pass

dual_log = create_dual_logger("dual")
if dual_log:
    dual_log.debug("This should only be in the file")
    dual_log.info("This should only be in the file")
    dual_log.warning("This should appear in console AND file")
    dual_log.error("This too")
    print("Check config/debug.log for all messages")


# ── EXERCISE 6 (CHALLENGE) ──────────────────────────────────
# Implement a context manager class DatabaseConnection that:
#   - __enter__: prints "Connecting to DB…", returns self
#   - __exit__: on no error → commit + "Committed"
#              on exception → rollback + "Rolled back" + return False
# Test with both success and failure cases.
print("\n" + "=" * 55)
print("Exercise 6 (Challenge): DatabaseConnection context manager")
print("=" * 55)

class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.committed = False

    def execute(self, query: str):
        print(f"  Executing: {query}")

    def __enter__(self):
        # YOUR CODE HERE ↓
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE ↓
        pass

# Success path
print("Success path:")
with DatabaseConnection("mydb") as db:
    db.execute("INSERT INTO users VALUES (1, 'Alice')")

# Failure path
print("\nFailure path:")
try:
    with DatabaseConnection("mydb") as db:
        db.execute("UPDATE accounts SET balance = -1")
        raise ValueError("Negative balance not allowed!")
except ValueError as e:
    print(f"Caught outside: {e}")
