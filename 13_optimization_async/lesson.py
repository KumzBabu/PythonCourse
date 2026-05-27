# ============================================================
# MODULE 13: Optimization & Async Programming
# Day 9 of 10-Day Python Intensive
# ============================================================
# pip install aiohttp asyncpg
# ============================================================

import asyncio
import time
import threading
import concurrent.futures
from functools import lru_cache

# ─────────────────────────────────────────────
# 1. PROFILING — find the bottleneck first
# ─────────────────────────────────────────────

import cProfile
import pstats
import io

def slow_function():
    total = 0
    for i in range(500_000):
        total += i ** 2
    return total

# Quick timing
start = time.perf_counter()
slow_function()
elapsed = time.perf_counter() - start
print(f"slow_function: {elapsed:.4f}s")

# Full profiling
def profile(func, *args):
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(10)
    print(s.getvalue())
    return result

# profile(slow_function)   # uncomment to see detailed stats


# ─────────────────────────────────────────────
# 2. CACHING — @lru_cache
# ─────────────────────────────────────────────

@lru_cache(maxsize=256)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

t0 = time.perf_counter()
print(f"\nfib(35) = {fibonacci(35)}")
print(f"Time: {time.perf_counter()-t0:.6f}s")
print(f"Cache info: {fibonacci.cache_info()}")

# functools.cache (Python 3.9+) — unbounded, simpler
from functools import cache

@cache
def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


# ─────────────────────────────────────────────
# 3. GENERATORS — memory efficiency
# ─────────────────────────────────────────────

# List vs Generator — memory comparison
import sys

big_list = [x ** 2 for x in range(1_000_000)]
big_gen  = (x ** 2 for x in range(1_000_000))

print(f"\nList size: {sys.getsizeof(big_list):>12,} bytes")
print(f"Gen size:  {sys.getsizeof(big_gen):>12,} bytes")

def read_large_file(path: str):
    """Process a file line-by-line without loading it all into memory."""
    with open(path) as f:
        for line in f:
            yield line.strip()

def infinite_counter(start=0, step=1):
    """Infinite generator — pull values lazily."""
    n = start
    while True:
        yield n
        n += step

counter = infinite_counter(0, 2)
evens = [next(counter) for _ in range(5)]
print(f"\nFirst 5 evens: {evens}")


# ─────────────────────────────────────────────
# 4. THREADING — I/O-bound parallelism
# ─────────────────────────────────────────────
"""
Python GIL: only one thread executes Python bytecode at a time.
  ✅ Threading IS useful for: network I/O, file I/O, waiting
  ❌ Threading WON'T help for: CPU-bound tasks (use multiprocessing)
"""

import time
import threading

def fetch_data(url_id: int, results: list):
    """Simulate a slow network request."""
    time.sleep(0.3)   # simulate I/O
    results.append(f"data_{url_id}")

# Sequential
t0 = time.perf_counter()
results = []
for i in range(5):
    fetch_data(i, results)
print(f"\nSequential: {time.perf_counter()-t0:.2f}s  → {results}")

# Threaded
t0 = time.perf_counter()
threads = []
results = []
lock = threading.Lock()

def fetch_thread(i):
    time.sleep(0.3)
    with lock:
        results.append(f"data_{i}")

for i in range(5):
    t = threading.Thread(target=fetch_thread, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Threaded:   {time.perf_counter()-t0:.2f}s  → {sorted(results)}")


# ─────────────────────────────────────────────
# 5. ThreadPoolExecutor — cleaner API
# ─────────────────────────────────────────────

def simulate_api_call(endpoint_id: int) -> str:
    time.sleep(0.2)
    return f"response_{endpoint_id}"

t0 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    futures = [pool.submit(simulate_api_call, i) for i in range(10)]
    responses = [f.result() for f in concurrent.futures.as_completed(futures)]

print(f"\nThreadPool (10 tasks): {time.perf_counter()-t0:.2f}s")
print(f"Results: {sorted(responses)}")


# ─────────────────────────────────────────────
# 6. MULTIPROCESSING — CPU-bound parallelism
# ─────────────────────────────────────────────

import multiprocessing

def cpu_intensive(n: int) -> int:
    """Simulate heavy CPU work."""
    return sum(i ** 2 for i in range(n))

if __name__ == "__main__":   # required guard for multiprocessing
    numbers = [500_000] * 4

    t0 = time.perf_counter()
    serial = [cpu_intensive(n) for n in numbers]
    print(f"\nSerial (4 tasks): {time.perf_counter()-t0:.2f}s")

    t0 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        parallel = list(pool.map(cpu_intensive, numbers))
    print(f"Parallel (4 tasks): {time.perf_counter()-t0:.2f}s")


# ─────────────────────────────────────────────
# 7. ASYNCIO — cooperative concurrency
# ─────────────────────────────────────────────
"""
async/await = coroutines = cooperative multitasking
Perfect for: many I/O-bound tasks (HTTP, DB, websockets)
Event loop: one thread, switches between coroutines at 'await' points
"""

async def async_fetch(url_id: int) -> str:
    """Simulate async network call."""
    await asyncio.sleep(0.3)   # yields control to event loop
    return f"response_{url_id}"

async def main_sequential():
    t0 = time.perf_counter()
    results = []
    for i in range(5):
        r = await async_fetch(i)
        results.append(r)
    print(f"\nAsync sequential: {time.perf_counter()-t0:.2f}s → {results}")

async def main_concurrent():
    t0 = time.perf_counter()
    # asyncio.gather runs all coroutines CONCURRENTLY
    results = await asyncio.gather(*[async_fetch(i) for i in range(5)])
    print(f"Async concurrent: {time.perf_counter()-t0:.2f}s → {list(results)}")

asyncio.run(main_sequential())
asyncio.run(main_concurrent())


# ─────────────────────────────────────────────
# 8. ASYNC WITH aiohttp (HTTP client)
# ─────────────────────────────────────────────

async def fetch_url(session, url: str) -> dict:
    """Fetch a URL asynchronously."""
    try:
        import aiohttp
        async with session.get(url) as resp:
            return await resp.json()
    except ImportError:
        await asyncio.sleep(0.1)   # simulate
        return {"url": url, "simulated": True}

async def fetch_many(urls: list[str]) -> list:
    try:
        import aiohttp
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            return await asyncio.gather(*tasks)
    except ImportError:
        return [{"url": u, "note": "install aiohttp"} for u in urls]

# asyncio.run(fetch_many([
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
# ]))


# ─────────────────────────────────────────────
# 9. ASYNC GENERATORS & CONTEXT MANAGERS
# ─────────────────────────────────────────────

async def async_range(n: int):
    """Async generator — yield values with async delays."""
    for i in range(n):
        await asyncio.sleep(0.01)
        yield i

async def use_async_gen():
    async for value in async_range(5):
        print(f"  got: {value}", end=" ")
    print()

asyncio.run(use_async_gen())


# ─────────────────────────────────────────────
# 10. OPTIMIZATION CHECKLIST
# ─────────────────────────────────────────────
"""
PERFORMANCE DECISION TREE
═════════════════════════
1. Profile first — don't guess where the bottleneck is
2. Algorithm & data structures — O(n) > O(n²), set > list for lookups
3. Built-ins and standard library — faster than pure Python
4. @lru_cache / @cache — avoid redundant computation
5. Generators — avoid loading large data into memory
6. I/O bound?
     → asyncio (many concurrent tasks, modern pattern)
     → ThreadPoolExecutor (simpler, compatible with sync libs)
7. CPU bound?
     → ProcessPoolExecutor / multiprocessing
     → NumPy for numerical work
8. NumPy / pandas — vectorized operations over Python loops
9. Profile again — confirm improvement

WHEN TO USE WHAT
────────────────
asyncio          → 100s of concurrent HTTP/DB calls (modern services)
threading        → legacy code, wrapping blocking libs (requests)
multiprocessing  → heavy math, image/video processing, ML
"""
