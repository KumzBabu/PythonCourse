# ============================================================
# Benchmark Runner — compare implementations side-by-side
# ============================================================
# Usage: python benchmark_runner.py
# ============================================================

import time
import sys
import statistics
from functools import lru_cache

def benchmark(func, *args, runs=5, label=None):
    """Run a function N times and report timing stats."""
    times = []
    for _ in range(runs):
        t0 = time.perf_counter()
        result = func(*args)
        times.append(time.perf_counter() - t0)
    name = label or func.__name__
    print(f"  {name:<30} | "
          f"mean={statistics.mean(times):.4f}s  "
          f"min={min(times):.4f}s  "
          f"max={max(times):.4f}s")
    return result


print("=" * 70)
print("BENCHMARK 1: List comprehension vs loop")
print("=" * 70)

def loop_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

def comp_squares(n):
    return [i ** 2 for i in range(n)]

def gen_squares(n):
    return list(i ** 2 for i in range(n))

N = 200_000
benchmark(loop_squares, N, label="for-loop append")
benchmark(comp_squares, N, label="list comprehension")
benchmark(gen_squares,  N, label="generator expr")


print("\n" + "=" * 70)
print("BENCHMARK 2: dict lookup vs list search")
print("=" * 70)

import random
data_list = list(range(100_000))
data_set  = set(data_list)
data_dict = {x: True for x in data_list}
targets   = [random.randint(0, 99_999) for _ in range(1000)]

def search_list(items, targets):
    return [t in items for t in targets]

def search_set(items, targets):
    return [t in items for t in targets]

benchmark(search_list, data_list, targets, label="list   (O(n) each)")
benchmark(search_set,  data_set,  targets, label="set    (O(1) each)")
benchmark(search_set,  data_dict, targets, label="dict   (O(1) each)")


print("\n" + "=" * 70)
print("BENCHMARK 3: @lru_cache speedup on fibonacci")
print("=" * 70)

def fib_no_cache(n):
    if n < 2: return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)

@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2: return n
    return fib_cached(n - 1) + fib_cached(n - 2)

benchmark(fib_no_cache, 30, runs=3, label="fibonacci (no cache)")
benchmark(fib_cached,   35, runs=3, label="fibonacci (lru_cache)")


print("\n" + "=" * 70)
print("BENCHMARK 4: String concatenation methods")
print("=" * 70)

WORDS = ["python"] * 10_000

def concat_plus(words):
    s = ""
    for w in words:
        s += w
    return s

def concat_join(words):
    return "".join(words)

def concat_io(words):
    import io
    buf = io.StringIO()
    for w in words:
        buf.write(w)
    return buf.getvalue()

benchmark(concat_plus, WORDS, label="str +=")
benchmark(concat_join, WORDS, label="''.join()")
benchmark(concat_io,   WORDS, label="StringIO.write()")

print("\nDone.")
