# ============================================================
# >>> Python Quick Cheat Sheet
# Keep this open as a reference while you learn!
# ============================================================

# ── VARIABLES & TYPES ────────────────────────────────────────
x = 42          # int
y = 3.14        # float
name = "Alice"  # str
flag = True     # bool  (True / False — capital!)
nothing = None  # NoneType (like null)

# ── STRING TRICKS ────────────────────────────────────────────
s = "hello world"
s.upper()          # "HELLO WORLD"
s.title()          # "Hello World"
s.replace("o","0") # "hell0 w0rld"
s.split(" ")       # ["hello", "world"]
s.startswith("he") # True
" hi ".strip()     # "hi"
len(s)             # 11
f"My name is {name}"          # f-string
"Name: {}".format(name)       # .format()

# ── MATH ─────────────────────────────────────────────────────
10 / 3    # 3.333  (float division)
10 // 3   # 3      (floor division)
10 % 3    # 1      (modulo / remainder)
2 ** 10   # 1024   (power)
abs(-5)   # 5
round(3.7)# 4

# ── LIST ─────────────────────────────────────────────────────
lst = [1, 2, 3]
lst.append(4)       # [1,2,3,4]
lst.insert(0, 0)    # [0,1,2,3,4]
lst.remove(2)       # [0,1,3,4]
lst.pop()           # removes & returns last --> 4
lst[0]              # 0 (first)
lst[-1]             # last
lst[1:3]            # slice [1,3]
len(lst)            # length
sorted(lst)         # sorted copy
lst.sort()          # sort in-place
[x**2 for x in lst] # list comprehension

# ── DICT ─────────────────────────────────────────────────────
d = {"a": 1, "b": 2}
d["a"]              # 1
d.get("c", 0)       # 0 (default if missing)
d["c"] = 3          # add/update
del d["a"]          # delete key
d.keys()            # dict_keys(['b','c'])
d.values()          # dict_values([2,3])
d.items()           # dict_items([('b',2),('c',3)])
"b" in d            # True

# ── CONTROL FLOW ─────────────────────────────────────────────
# if/elif/else
if x > 0:
    pass
elif x == 0:
    pass
else:
    pass

# ternary
result = "yes" if x > 0 else "no"

# for
for i in range(5): pass          # 0..4
for item in lst: pass            # each item
for i, item in enumerate(lst): pass  # index + item

# while
while x > 0:
    x -= 1

# ── FUNCTIONS ────────────────────────────────────────────────
def func(a, b=10, *args, **kwargs):
    return a + b

lambda x: x * 2     # anonymous function

# ── ERROR HANDLING ───────────────────────────────────────────
try:
    risky_code = 1/0
except ZeroDivisionError as e:
    print(e)
except (TypeError, ValueError):
    pass
finally:
    pass   # always runs

# ── FILE I/O ─────────────────────────────────────────────────
with open("file.txt", "w") as f: f.write("hello")
with open("file.txt", "r") as f: content = f.read()
# modes: "r"=read, "w"=write (overwrites), "a"=append, "rb"=binary

# ── COMMON BUILT-INS ─────────────────────────────────────────
print(), input(), len(), type(), range()
int(), float(), str(), bool(), list(), dict(), set()
sum(), min(), max(), abs(), round()
zip(), enumerate(), map(), filter()
sorted(), reversed()

# ── IMPORTS ──────────────────────────────────────────────────
import os
import sys
import json
import math
import random
from datetime import datetime
from pathlib import Path
