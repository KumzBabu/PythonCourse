# ============================================================
# MODULE 11: Error Handling & Logging
# Day 8 of 10-Day Python Intensive
# ============================================================
# pip install python-dotenv  (for config section)
# ============================================================

import logging
import logging.config
import traceback
import sys
from pathlib import Path

# ─────────────────────────────────────────────
# 1. EXCEPTION HIERARCHY
# ─────────────────────────────────────────────
"""
BaseException
 └── Exception
      ├── ValueError      — wrong value type (e.g. int("abc"))
      ├── TypeError       — wrong argument type
      ├── KeyError        — dict key not found
      ├── IndexError      — list index out of range
      ├── AttributeError  — object has no such attribute
      ├── FileNotFoundError (IOError)
      ├── ZeroDivisionError
      ├── ImportError / ModuleNotFoundError
      └── RuntimeError    — general runtime problem
"""

# ─────────────────────────────────────────────
# 2. TRY / EXCEPT / ELSE / FINALLY
# ─────────────────────────────────────────────

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        # Runs ONLY if no exception was raised
        print(f"{a} / {b} = {result}")
        return result
    finally:
        # ALWAYS runs (cleanup code goes here)
        print("divide() finished.")

divide(10, 2)
divide(10, 0)
divide(10, "x")


# ─────────────────────────────────────────────
# 3. RAISING EXCEPTIONS
# ─────────────────────────────────────────────

def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0-150, got {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")

# Re-raise after logging
def process_file(path: str):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"File missing: {path}")
        raise   # re-raise the same exception


# ─────────────────────────────────────────────
# 4. CUSTOM EXCEPTIONS
# ─────────────────────────────────────────────

class AppError(Exception):
    """Base class for all application errors."""
    pass

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"[{field}] {message}")

class DatabaseError(AppError):
    def __init__(self, query: str, cause: Exception):
        self.query = query
        super().__init__(f"DB error on '{query}': {cause}")

# Usage
try:
    raise ValidationError("email", "must contain @")
except ValidationError as e:
    print(f"\nValidation failed on field '{e.field}': {e.message}")


# ─────────────────────────────────────────────
# 5. CONTEXT MANAGERS — with statement
# ─────────────────────────────────────────────

# Files — always use 'with' so file is closed even on error
def read_file_safe(path: str) -> str | None:
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

# Custom context manager using __enter__/__exit__
class Timer:
    import time
    def __enter__(self):
        import time
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # don't suppress exceptions

with Timer():
    total = sum(range(1_000_000))


# ─────────────────────────────────────────────
# 6. LOGGING — THE RIGHT WAY
# ─────────────────────────────────────────────

# Logging levels (ascending severity):
# DEBUG < INFO < WARNING < ERROR < CRITICAL

# ── Basic setup ─────────────────────────────
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)   # best practice: use module name

logger.debug("Debug: detailed info for developers")
logger.info("Info: general application flow")
logger.warning("Warning: something unexpected but recoverable")
logger.error("Error: operation failed")
logger.critical("Critical: system might be going down")


# ── Log to file AND console ──────────────────
def setup_logger(name: str, log_file: str, level=logging.DEBUG):
    """Create a logger that writes to both console and file."""
    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    lg = logging.getLogger(name)
    lg.setLevel(level)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    # File handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    lg.addHandler(ch)
    lg.addHandler(fh)
    return lg

app_log = setup_logger("myapp", "config/app.log")
app_log.info("Application started")
app_log.debug("Config loaded from config/settings.py")


# ── Log exceptions with traceback ───────────
def risky_operation():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("Caught division by zero")   # auto-includes traceback
        return None

risky_operation()


# ─────────────────────────────────────────────
# 7. STRUCTURED LOGGING (JSON)
# ─────────────────────────────────────────────

import json
import datetime

class JSONFormatter(logging.Formatter):
    """Emit each log record as a JSON line — ideal for log aggregation."""
    def format(self, record: logging.LogRecord) -> str:
        log_dict = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "level":     record.levelname,
            "logger":    record.name,
            "message":   record.getMessage(),
        }
        if record.exc_info:
            log_dict["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_dict)

json_handler = logging.StreamHandler()
json_handler.setFormatter(JSONFormatter())

json_logger = logging.getLogger("json_logger")
json_logger.addHandler(json_handler)
json_logger.setLevel(logging.INFO)

json_logger.info("User logged in", extra={"user_id": 42})


# ─────────────────────────────────────────────
# 8. PRODUCTION PATTERNS
# ─────────────────────────────────────────────

# Pattern 1: Exception chaining
def load_config(path: str):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise AppError(f"Config file not found: {path}") from e
    except json.JSONDecodeError as e:
        raise AppError(f"Invalid JSON in {path}") from e

# Pattern 2: Graceful degradation
def get_user_data(user_id: int) -> dict:
    try:
        # Simulate DB call
        if user_id == 999:
            raise DatabaseError("SELECT * FROM users", RuntimeError("timeout"))
        return {"id": user_id, "name": "Alice"}
    except DatabaseError as e:
        logger.error(f"DB error: {e}")
        return {}   # return empty rather than crash

# Pattern 3: Global exception handler
def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = global_exception_handler


# ─────────────────────────────────────────────
# KEY TAKEAWAYS
# ─────────────────────────────────────────────
"""
ERROR HANDLING
══════════════
try / except / else / finally
raise ExceptionClass("message")
raise ExceptionClass("msg") from original_exc   # chain
Custom exceptions: inherit from Exception
Always catch specific exceptions, not bare 'except:'

LOGGING
═══════
logger = logging.getLogger(__name__)
Levels : DEBUG < INFO < WARNING < ERROR < CRITICAL
Handler: StreamHandler (console), FileHandler (file)
Format : %(asctime)s | %(levelname)s | %(name)s | %(message)s
logger.exception(msg)  →  logs with full traceback
Use JSON logging in production for log aggregation tools
"""
