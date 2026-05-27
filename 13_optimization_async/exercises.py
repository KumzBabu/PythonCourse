# ============================================================
# MODULE 13: Optimization & Async — Exercises
# ============================================================

import asyncio
import time
import concurrent.futures
from functools import lru_cache

# ── EXERCISE 1 ──────────────────────────────────────────────
# Profile and optimize: the function below is slow.
# 1) Measure its execution time using time.perf_counter()
# 2) Identify why it's slow
# 3) Write an optimized version
# 4) Measure the optimized version and compute the speedup
print("=" * 55)
print("Exercise 1: Profile and optimize")
print("=" * 55)

def slow_search(data: list, target: int) -> bool:
    """Returns True if target is in data."""
    for item in data:
        if item == target:
            return True
    return False

# Generate test data
import random
large_list = list(range(1_000_000))
random.shuffle(large_list)
target = 999_999   # worst case — near end

# YOUR CODE HERE ↓
# 1) Time the slow version
# 2) Write optimized_search using a set
# 3) Compare timings


# ── EXERCISE 2 ──────────────────────────────────────────────
# Cache the expensive function using @lru_cache.
# Call it 10 times with the same arguments and show
# that only the first call actually computes.
print("\n" + "=" * 55)
print("Exercise 2: @lru_cache speedup")
print("=" * 55)

def expensive_compute(n: int) -> int:
    """Simulates a slow computation."""
    time.sleep(0.5)   # simulate slow work
    return n * n

# YOUR CODE HERE ↓
# 1) Apply @lru_cache to expensive_compute (or create a cached version)
# 2) Call it 5 times with n=7, measure total time
# 3) Print cache_info() and explain the output


# ── EXERCISE 3 ──────────────────────────────────────────────
# Rewrite list_squares(n) to use a generator instead of a list.
# Show the memory difference using sys.getsizeof().
print("\n" + "=" * 55)
print("Exercise 3: Generator vs list — memory")
print("=" * 55)

import sys

def list_squares(n: int) -> list:
    return [x ** 2 for x in range(n)]

def gen_squares(n: int):
    # YOUR CODE HERE ↓ — convert to generator
    pass

n = 100_000
lst = list_squares(n)
gen = gen_squares(n)

if gen:
    print(f"List: {sys.getsizeof(lst):>10,} bytes")
    print(f"Gen:  {sys.getsizeof(gen):>10,} bytes")


# ── EXERCISE 4 ──────────────────────────────────────────────
# Use ThreadPoolExecutor to download data from 10 "endpoints"
# concurrently. Each endpoint takes 0.3s to respond.
# Compare the time vs sequential execution.
print("\n" + "=" * 55)
print("Exercise 4: ThreadPoolExecutor vs sequential")
print("=" * 55)

def fetch_endpoint(endpoint_id: int) -> dict:
    """Simulate a slow API call (0.3s each)."""
    time.sleep(0.3)
    return {"id": endpoint_id, "data": f"result_{endpoint_id}"}

# YOUR CODE HERE ↓
# Sequential version — time it
# Threaded version with ThreadPoolExecutor — time it
# Print: sequential time, threaded time, speedup ratio


# ── EXERCISE 5 ──────────────────────────────────────────────
# Write an async function fetch_all(urls) that:
# - uses asyncio.sleep(0.2) to simulate network delay per URL
# - fetches all URLs CONCURRENTLY using asyncio.gather()
# - returns a list of results
# Compare with sequential async (awaiting one by one).
print("\n" + "=" * 55)
print("Exercise 5: asyncio.gather() vs sequential await")
print("=" * 55)

FAKE_URLS = [f"https://api.example.com/item/{i}" for i in range(8)]

async def fake_fetch(url: str) -> str:
    """Simulates async HTTP call."""
    await asyncio.sleep(0.2)
    return f"OK: {url.split('/')[-1]}"

async def fetch_sequential(urls: list) -> list:
    # YOUR CODE HERE ↓ — await each one by one
    pass

async def fetch_concurrent(urls: list) -> list:
    # YOUR CODE HERE ↓ — use asyncio.gather()
    pass

async def compare():
    t0 = time.perf_counter()
    seq_results = await fetch_sequential(FAKE_URLS)
    seq_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    con_results = await fetch_concurrent(FAKE_URLS)
    con_time = time.perf_counter() - t0

    print(f"Sequential:  {seq_time:.2f}s")
    print(f"Concurrent:  {con_time:.2f}s")
    print(f"Speedup:     {seq_time/con_time:.1f}x")

asyncio.run(compare())


# ── EXERCISE 6 (CHALLENGE) ──────────────────────────────────
# Implement async retry logic:
# Write async_retry(coro_func, max_retries=3, delay=0.1)
# that wraps a coroutine function and retries it on failure.
# Test with a function that fails the first 2 times.
print("\n" + "=" * 55)
print("Exercise 6 (Challenge): Async retry")
print("=" * 55)

import random

attempt_counter = 0

async def unreliable_fetch(item_id: int) -> str:
    global attempt_counter
    attempt_counter += 1
    if attempt_counter < 3:
        raise ConnectionError(f"Simulated failure #{attempt_counter}")
    return f"Success on attempt #{attempt_counter}"

async def async_retry(coro_func, *args, max_retries=3, delay=0.1, **kwargs):
    # YOUR CODE HERE ↓
    pass

async def run_retry_test():
    global attempt_counter
    attempt_counter = 0
    result = await async_retry(unreliable_fetch, 1, max_retries=5, delay=0.05)
    print(f"Result: {result}")

asyncio.run(run_retry_test())
