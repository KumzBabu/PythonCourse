# ============================================================
# MODULE 9: APIs & the requests Library
# Day 5 of 10-Day Python Intensive
# ============================================================
# pip install requests python-dotenv
# ============================================================

import requests
import json
from urllib.parse import urlencode

# ─────────────────────────────────────────────
# 1. WHAT IS AN API?
# ─────────────────────────────────────────────
"""
API = Application Programming Interface
REST API: uses HTTP methods (GET, POST, PUT, DELETE, PATCH)
  GET    → fetch data
  POST   → create data
  PUT    → replace data
  PATCH  → update data
  DELETE → remove data

Response formats: JSON (most common), XML, plain text
Status codes:
  2xx → success (200 OK, 201 Created, 204 No Content)
  3xx → redirect
  4xx → client error (400 Bad Request, 401 Unauthorized, 404 Not Found)
  5xx → server error (500 Internal Server Error)
"""

# ─────────────────────────────────────────────
# 2. SIMPLE GET REQUEST
# ─────────────────────────────────────────────

# Public API — no auth required
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")

# Parse JSON
users = response.json()
print(f"\nFetched {len(users)} users")
print(f"First user: {users[0]['name']} — {users[0]['email']}")


# ─────────────────────────────────────────────
# 3. QUERY PARAMETERS
# ─────────────────────────────────────────────

# Passing params as a dict (requests URL-encodes them automatically)
params = {"userId": 1, "_limit": 5}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(f"\n── Posts for userId=1 (limit 5) ──")
print(f"URL called: {response.url}")
posts = response.json()
for post in posts:
    print(f"  [{post['id']}] {post['title'][:50]}")


# ─────────────────────────────────────────────
# 4. POST — SENDING DATA
# ─────────────────────────────────────────────

new_post = {
    "title": "My First API Post",
    "body": "This was created via the requests library.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post          # sets Content-Type: application/json automatically
)

print(f"\n── POST response ──")
print(f"Status: {response.status_code}")   # 201 Created
print(f"Created: {response.json()}")


# ─────────────────────────────────────────────
# 5. PUT & DELETE
# ─────────────────────────────────────────────

# PUT — replace resource
update = {"id": 1, "title": "Updated Title", "body": "New body", "userId": 1}
r = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update)
print(f"\nPUT status: {r.status_code}")

# DELETE
r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(f"DELETE status: {r.status_code}")   # 200


# ─────────────────────────────────────────────
# 6. HEADERS & AUTHENTICATION
# ─────────────────────────────────────────────

# Bearer token auth (common pattern)
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN",
    "Accept": "application/json",
    "X-Custom-Header": "my-app/1.0"
}

# Example with GitHub API (no token for public endpoints)
gh_headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(
    "https://api.github.com/repos/python/cpython",
    headers=gh_headers,
    timeout=10
)
if r.status_code == 200:
    repo = r.json()
    print(f"\n── GitHub CPython repo ──")
    print(f"Stars: {repo['stargazers_count']:,}")
    print(f"Forks: {repo['forks_count']:,}")
    print(f"Language: {repo['language']}")


# ─────────────────────────────────────────────
# 7. ERROR HANDLING
# ─────────────────────────────────────────────

def safe_get(url, **kwargs):
    """Fetch a URL with proper error handling."""
    try:
        response = requests.get(url, timeout=10, **kwargs)
        response.raise_for_status()    # raises HTTPError for 4xx/5xx
        return response.json()
    except requests.exceptions.Timeout:
        print(f"❌ Timeout fetching {url}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection failed for {url}")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP {e.response.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
    return None

data = safe_get("https://jsonplaceholder.typicode.com/users/1")
if data:
    print(f"\n── Safe fetch ──")
    print(f"User: {data['name']}, City: {data['address']['city']}")

# 404 test
bad = safe_get("https://jsonplaceholder.typicode.com/users/9999")


# ─────────────────────────────────────────────
# 8. SESSIONS — Reuse connections & headers
# ─────────────────────────────────────────────

with requests.Session() as session:
    session.headers.update({"User-Agent": "PythonCourse/1.0"})
    session.headers.update({"Accept": "application/json"})

    # Multiple requests share the same TCP connection + headers
    r1 = session.get("https://jsonplaceholder.typicode.com/posts/1")
    r2 = session.get("https://jsonplaceholder.typicode.com/posts/2")

    print(f"\n── Session requests ──")
    print(f"Post 1: {r1.json()['title'][:40]}")
    print(f"Post 2: {r2.json()['title'][:40]}")


# ─────────────────────────────────────────────
# 9. WORKING WITH REAL APIs — Weather Example
# ─────────────────────────────────────────────
"""
Open-Meteo is a FREE weather API — no key required!
"""

def get_weather(latitude, longitude, city_name="Unknown"):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "temperature_unit": "celsius"
    }
    data = safe_get(url, params=params)
    if data and "current_weather" in data:
        cw = data["current_weather"]
        print(f"\n🌤  Weather in {city_name}:")
        print(f"   Temperature : {cw['temperature']}°C")
        print(f"   Wind speed  : {cw['windspeed']} km/h")
    return data

# get_weather(51.5074, -0.1278, "London")
# get_weather(40.7128, -74.0060, "New York")


# ─────────────────────────────────────────────
# 10. RATE LIMITING & RETRIES
# ─────────────────────────────────────────────

import time

def get_with_retry(url, max_retries=3, backoff=2, **kwargs):
    """Retry with exponential backoff."""
    for attempt in range(max_retries):
        try:
            r = requests.get(url, timeout=10, **kwargs)
            if r.status_code == 429:           # Too Many Requests
                wait = int(r.headers.get("Retry-After", backoff ** attempt))
                print(f"Rate limited. Waiting {wait}s…")
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait = backoff ** attempt
                print(f"Attempt {attempt+1} failed. Retrying in {wait}s…")
                time.sleep(wait)
            else:
                print(f"All {max_retries} attempts failed: {e}")
    return None


# ─────────────────────────────────────────────
# KEY TAKEAWAYS
# ─────────────────────────────────────────────
"""
REQUESTS QUICK REFERENCE
════════════════════════
GET     : requests.get(url, params={}, headers={}, timeout=10)
POST    : requests.post(url, json=data, headers={})
PUT     : requests.put(url, json=data)
DELETE  : requests.delete(url)

Response : .status_code  .json()  .text  .headers  .url
Errors   : raise_for_status() → HTTPError
           ConnectionError, Timeout, RequestException
Session  : requests.Session()  →  shared headers/cookies/TCP
"""
