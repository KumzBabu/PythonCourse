# ============================================================
# LESSON 3: Functions
# ============================================================

# ── 1. Defining & Calling Functions ──────────────────────────
def greet():
    print("Hello!")

greet()   # Call the function

# ── 2. Parameters & Return Values ────────────────────────────
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# ── 3. Default Parameters ────────────────────────────────────
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_person("Kumaresh")            # Hello, Kumaresh!
greet_person("Kumaresh", "Hi")     # Hi, Kumaresh!

# ── 4. Keyword Arguments ─────────────────────────────────────
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe(age=25, city="Chennai", name="Kumaresh")   # order doesn't matter

# ── 5. *args — variable number of arguments ──────────────────
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100

# ── 6. **kwargs — keyword arguments as a dict ─────────────────
def show_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

show_info(name="Kumaresh", role="Developer", level="Beginner")

# ── 7. Lambda (Anonymous) Functions ──────────────────────────
square = lambda x: x ** 2
print(square(5))   # 25

# Often used with built-ins like sorted(), map(), filter()
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(nums))                        # ascending
print(sorted(nums, reverse=True))          # descending

words = ["banana", "apple", "cherry"]
print(sorted(words, key=lambda w: len(w))) # sort by length

# ── 8. Scope: local vs global ────────────────────────────────
x = 10   # global variable

def change():
    x = 99   # this is a NEW local variable, doesn't affect global x
    print(f"Inside function: {x}")

change()
print(f"Outside function: {x}")   # still 10

print("\n[DONE] Lesson 3 complete!")
