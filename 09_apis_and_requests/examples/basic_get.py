# ============================================================
# Example: Basic GET request patterns
# ============================================================

import requests

# 1. Simplest possible GET
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.json())

# 2. With params
r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
print(f"Posts for user 1: {len(r.json())}")

# 3. Inspect headers
print("Content-Type:", r.headers["Content-Type"])
print("Status:", r.status_code)
