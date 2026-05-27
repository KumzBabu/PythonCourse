# ============================================================
# Example: Common authentication patterns
# ============================================================
# NOTE: Replace placeholder tokens with real values.
# ============================================================

import requests
import os

# ── 1. Bearer Token (most common) ───────────────────────────
token = os.getenv("API_TOKEN", "your-token-here")

r = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {token}"}
)

# ── 2. Basic Auth ────────────────────────────────────────────
r = requests.get(
    "https://api.example.com/secure",
    auth=("username", "password")
)

# ── 3. API Key in query param ────────────────────────────────
r = requests.get(
    "https://api.example.com/data",
    params={"api_key": "your-key", "q": "python"}
)

# ── 4. API Key in header ─────────────────────────────────────
r = requests.get(
    "https://api.example.com/data",
    headers={"X-API-Key": "your-key"}
)

# ── 5. Session with persistent auth ─────────────────────────
with requests.Session() as s:
    s.headers["Authorization"] = f"Bearer {token}"
    r1 = s.get("https://api.example.com/endpoint1")
    r2 = s.get("https://api.example.com/endpoint2")
    # Token sent automatically on every request
