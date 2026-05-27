# ============================================================
# MODULE 9: APIs & requests — Exercises
# ============================================================
# All exercises use FREE public APIs (no keys required).
# Public APIs used:
#   jsonplaceholder.typicode.com  — fake REST API
#   open-meteo.com                — free weather
#   catfact.ninja                 — cat facts
#   api.github.com                — GitHub (unauthenticated)
# ============================================================

import requests
import json
import time


# ── EXERCISE 1 ──────────────────────────────────────────────
# Fetch all "todos" for userId=3 from JSONPlaceholder.
# Count how many are completed vs pending.
# Print a summary: "Completed: X / Total: Y"
print("=" * 55)
print("Exercise 1: Todo completion summary")
print("=" * 55)

# URL: https://jsonplaceholder.typicode.com/todos?userId=3
# YOUR CODE HERE ↓


# ── EXERCISE 2 ──────────────────────────────────────────────
# Fetch 5 cat facts from https://catfact.ninja/facts?limit=5
# Print each fact numbered (1. …  2. … etc.)
print("\n" + "=" * 55)
print("Exercise 2: Cat facts")
print("=" * 55)

# YOUR CODE HERE ↓


# ── EXERCISE 3 ──────────────────────────────────────────────
# Use the Open-Meteo API to get the current temperature
# for THREE cities of your choice.
# Print: "City: X°C"
# Open-Meteo docs: https://open-meteo.com/en/docs
# Endpoint: https://api.open-meteo.com/v1/forecast
# Required params: latitude, longitude, current_weather=true
print("\n" + "=" * 55)
print("Exercise 3: Multi-city weather")
print("=" * 55)

cities = [
    {"name": "London",    "lat": 51.5074, "lon": -0.1278},
    {"name": "Tokyo",     "lat": 35.6762, "lon": 139.6503},
    {"name": "New York",  "lat": 40.7128, "lon": -74.0060},
]

# YOUR CODE HERE ↓
# Loop over cities, fetch weather, print result


# ── EXERCISE 4 ──────────────────────────────────────────────
# POST a new "comment" to JSONPlaceholder.
# Endpoint: POST https://jsonplaceholder.typicode.com/comments
# Body: { postId, name, email, body }
# Assert response status is 201 and print the created ID.
print("\n" + "=" * 55)
print("Exercise 4: POST a comment")
print("=" * 55)

# YOUR CODE HERE ↓
new_comment = {
    "postId": 1,
    "name": "Your Name",
    "email": "you@example.com",
    "body": "This is my first API POST!"
}
# response = ...
# assert response.status_code == 201
# print(f"Created comment ID: {response.json()['id']}")


# ── EXERCISE 5 ──────────────────────────────────────────────
# Write a function `search_github_users(query, max_results=5)`
# that hits https://api.github.com/search/users?q=<query>
# and returns a list of dicts: [{ login, url, followers_url }]
# Then call it with "guido" and print the results.
print("\n" + "=" * 55)
print("Exercise 5: GitHub user search")
print("=" * 55)

def search_github_users(query: str, max_results: int = 5) -> list:
    """Search GitHub for users matching query."""
    # YOUR CODE HERE ↓
    pass

results = search_github_users("guido")
if results:
    for user in results:
        print(f"  {user}")


# ── EXERCISE 6 ──────────────────────────────────────────────
# Build a CLI-style "API explorer" for JSONPlaceholder:
# Prompt the user to choose a resource (posts/users/todos/comments)
# then choose an ID (or 'all').
# Fetch and pretty-print the result.
print("\n" + "=" * 55)
print("Exercise 6: JSONPlaceholder CLI Explorer")
print("=" * 55)

BASE_URL = "https://jsonplaceholder.typicode.com"

def explore():
    resources = ["posts", "users", "todos", "comments"]
    print(f"Available resources: {', '.join(resources)}")
    resource = input("Enter resource: ").strip().lower()

    if resource not in resources:
        print("Invalid resource.")
        return

    resource_id = input("Enter ID (or press Enter for all): ").strip()
    url = f"{BASE_URL}/{resource}"
    if resource_id:
        url += f"/{resource_id}"

    # YOUR CODE HERE ↓
    # Fetch and pretty-print (use json.dumps with indent=2)
    pass

# explore()   # Uncomment to run interactively


# ── EXERCISE 7 (CHALLENGE) ──────────────────────────────────
# Write a function that checks if a list of URLs are "up"
# (return 2xx status). Use a requests.Session for efficiency.
# Return a dict: { url: True/False }
print("\n" + "=" * 55)
print("Exercise 7 (Challenge): URL health checker")
print("=" * 55)

def check_urls(urls: list) -> dict:
    """Return {url: is_up} for each URL."""
    results = {}
    # YOUR CODE HERE ↓
    # Use a Session, catch exceptions, set is_up = True/False
    return results

test_urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/nonexistent",
    "https://catfact.ninja/fact",
    "https://this-domain-does-not-exist-abc123.com",
]

health = check_urls(test_urls)
for url, is_up in health.items():
    status = "✅ UP" if is_up else "❌ DOWN"
    print(f"  {status}  {url}")
