# ============================================================
# LESSON 1: Python Basics
# Run this file and read the output alongside the code!
# ============================================================

# ── 1. Print & Comments ─────────────────────────────────────
print("Hello, World!")        # This is a comment — Python ignores it
print("Welcome to Python!")

# ── 2. Variables ────────────────────────────────────────────
# No need to declare types — Python figures it out
name = "Kumaresh"
age = 25
height = 5.9
is_student = True

print(name, age, height, is_student)

# ── 3. Data Types ────────────────────────────────────────────
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# ── 4. String Operations ─────────────────────────────────────
greeting = "Hello, " + name + "!"
print(greeting)

# f-strings: the modern, clean way
greeting2 = f"Hello, {name}! You are {age} years old."
print(greeting2)

# Useful string methods
sentence = "  python is awesome  "
print(sentence.strip())         # remove whitespace
print(sentence.strip().upper()) # PYTHON IS AWESOME
print(sentence.strip().title()) # Python Is Awesome
print(len(sentence.strip()))    # 18 — length

# ── 5. Numbers & Math ────────────────────────────────────────
x = 10
y = 3
print(x + y)   # 13  — addition
print(x - y)   # 7   — subtraction
print(x * y)   # 30  — multiplication
print(x / y)   # 3.333... — division (always float)
print(x // y)  # 3   — floor division (integer result)
print(x % y)   # 1   — modulo (remainder)
print(x ** y)  # 1000 — power (10³)

# ── 6. User Input ────────────────────────────────────────────
# Uncomment these lines to try interactive input:
# user_name = input("What is your name? ")
# print(f"Nice to meet you, {user_name}!")

# ── 7. Type Conversion ───────────────────────────────────────
num_str = "42"
num_int = int(num_str)     # string → int
num_float = float(num_str) # string → float
back_to_str = str(100)     # int → string

print(num_int + 8)   # 50
print(num_float)     # 42.0
print(back_to_str)   # "100"

print("\n[DONE] Lesson 1 complete!")
