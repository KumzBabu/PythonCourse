# ============================================================
# Capstone Project — Centralised Configuration
# ============================================================

import os
from pathlib import Path

# ── Paths ─────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
DATA_DIR  = BASE_DIR / "data"
LOG_DIR   = BASE_DIR / "logs"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# ── Database ──────────────────────────────────
DATABASE_PATH = str(DATA_DIR / "capstone.db")

# ── APIs ──────────────────────────────────────
API_TIMEOUT   = 10    # seconds
MAX_RETRIES   = 3
RETRY_BACKOFF = 1.5   # exponential backoff multiplier

ENDPOINTS = {
    "users":    "https://jsonplaceholder.typicode.com/users",
    "posts":    "https://jsonplaceholder.typicode.com/posts",
    "todos":    "https://jsonplaceholder.typicode.com/todos",
    "weather":  "https://api.open-meteo.com/v1/forecast",
}

# ── Logging ───────────────────────────────────
LOG_LEVEL  = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE   = str(LOG_DIR / "capstone.log")
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
LOG_DATE   = "%Y-%m-%d %H:%M:%S"

# ── Processing ────────────────────────────────
BATCH_SIZE       = 50
MAX_WORKERS      = 4
HIGH_SALARY_THRESHOLD = 90_000
