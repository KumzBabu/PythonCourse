# ============================================================
# LESSON 6: Modules, Files & Error Handling
# ============================================================

import os
import json
import math
import random
from datetime import datetime

# ── 1. Using Built-in Modules ────────────────────────────────
print(math.sqrt(144))        # 12.0
print(math.pi)               # 3.14159...
print(random.randint(1, 10)) # random number 1–10
print(random.choice(["heads", "tails"]))

now = datetime.now()
print(f"Today: {now.strftime('%Y-%m-%d %H:%M')}")

# ── 2. File Operations ───────────────────────────────────────
# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: Python\n")
    f.write("Line 3: World\n")

# Reading from a file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# Appending to a file
with open("sample.txt", "a") as f:
    f.write("Line 4: Appended!\n")

# ── 3. JSON ──────────────────────────────────────────────────
data = {
    "name": "Kumaresh",
    "skills": ["Python", "SQL"],
    "level": 1
}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON from file
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])
    print(loaded["skills"])

# ── 4. Error Handling (try / except) ─────────────────────────
# Without error handling — this would crash:
# result = 10 / 0

# With error handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

try:
    num = int("abc")   # ValueError
except ValueError as e:
    print(f"Error: {e}")

# Multiple exceptions + finally
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read file!")
finally:
    print("This always runs, error or not")

# ── 5. Raising Your Own Exceptions ───────────────────────────
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero!")
    return a / b

try:
    print(divide(10, 2))   # works
    print(divide(10, 0))   # raises error
except ValueError as e:
    print(f"Caught: {e}")

# Clean up files we created
os.remove("sample.txt")
os.remove("data.json")

print("\n[DONE] Lesson 6 complete!")
