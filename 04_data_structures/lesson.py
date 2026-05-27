# ============================================================
# LESSON 4: Data Structures — List, Dict, Tuple, Set
# ============================================================

# ── 1. LIST — ordered, mutable, allows duplicates ────────────
fruits = ["apple", "banana", "cherry"]

# Access
print(fruits[0])    # apple (first)
print(fruits[-1])   # cherry (last)
print(fruits[1:3])  # ['banana', 'cherry'] — slicing

# Modify
fruits.append("mango")      # add to end
fruits.insert(1, "blueberry")  # insert at index 1
fruits.remove("banana")     # remove by value
popped = fruits.pop()       # remove & return last item

print(fruits)
print(f"Popped: {popped}")

# Useful list methods
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(nums))      # returns new sorted list
print(min(nums), max(nums), sum(nums))
print(nums.count(1))     # how many times 1 appears

# List comprehension — Pythonic one-liner!
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")   # [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# ── 2. DICTIONARY — key-value pairs, ordered (Python 3.7+) ───
person = {
    "name": "Kumaresh",
    "age": 25,
    "city": "Chennai"
}

# Access
print(person["name"])              # Kumaresh
print(person.get("phone", "N/A"))  # N/A — safe access with default

# Modify
person["email"] = "k@example.com"  # add new key
person["age"] = 26                  # update existing key
del person["city"]                  # delete key

# Iterate
for key, value in person.items():
    print(f"  {key}: {value}")

print(list(person.keys()))
print(list(person.values()))

# Dict comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ── 3. TUPLE — ordered, IMMUTABLE (can't change after creation)
coordinates = (10, 20)
print(coordinates[0])   # 10
# coordinates[0] = 99   <-- This would cause an error!

# Useful for returning multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 4, 7])
print(f"Min: {low}, Max: {high}")

# ── 4. SET — unordered, unique values, no duplicates ─────────
colors = {"red", "green", "blue", "red", "green"}
print(colors)   # {'red', 'green', 'blue'} — duplicates removed

colors.add("yellow")
colors.discard("green")  # safe remove (no error if not found)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # union:        {1, 2, 3, 4, 5, 6}
print(a & b)   # intersection: {3, 4}
print(a - b)   # difference:   {1, 2}

# Quick duplicate removal trick
nums_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums_with_dupes))
print(unique)

print("\n[DONE] Lesson 4 complete!")
