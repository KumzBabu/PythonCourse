# ============================================================
# EXERCISES 6: Modules, Files & Error Handling
# Try to solve each exercise before looking at the solution!
# ============================================================

# Exercise 1: File Word Counter
# Write code that:
#   a) Creates a file called "story.txt" with at least 3 lines of any text
#   b) Reads it back and prints:
#      - Total number of lines
#      - Total number of words
#      - Total number of characters
# YOUR CODE HERE:


# Exercise 2: Safe Division
# Write a function safe_divide(a, b) that:
#   - Returns the result of a / b
#   - If b is 0, raises a ValueError with message "Cannot divide by zero"
#   - If either a or b is not a number, raises a TypeError with message "Both inputs must be numbers"
# Test it with normal values, zero, and a string.
# YOUR CODE HERE:


# Exercise 3: JSON Contact Book
# Build a simple contact book saved to "contacts.json":
#   - Start with an empty dict {}
#   - Add 3 contacts: each has "name", "phone", "email"
#   - Save to contacts.json
#   - Read it back and print each contact nicely
# YOUR CODE HERE:


# Exercise 4: Random Password Generator
# Use the random and string modules to write a function:
#   generate_password(length=12) --> returns a random password
# The password must contain:
#   - Uppercase letters
#   - Lowercase letters
#   - Digits
#   - Special characters (!@#$%^&*)
# Test by generating 5 passwords.
# YOUR CODE HERE:


# Exercise 5: Error Handling Chain
# Write a function load_number_from_file(filename) that:
#   - Opens the file and reads the first line
#   - Converts it to a float and returns it
#   - If file not found: prints "File not found" and returns None
#   - If content can't be converted: prints "Invalid number in file" and returns None
# Test it with a valid file, a missing file, and a file with text content.
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS (don't peek until you've tried!)
# ============================================================
"""
# Exercise 1
with open("story.txt", "w") as f:
    f.write("Once upon a time in a land far away.\n")
    f.write("There lived a brave Python programmer.\n")
    f.write("Who wrote clean code every single day.\n")

lines = words = chars = 0
with open("story.txt") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")
import os; os.remove("story.txt")

# Exercise 2
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

for test in [(10, 2), (10, 0), ("x", 2)]:
    try:
        print(safe_divide(*test))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

# Exercise 3
import json
contacts = {}
contacts["Alice"] = {"phone": "9876543210", "email": "alice@email.com"}
contacts["Bob"]   = {"phone": "9123456780", "email": "bob@email.com"}
contacts["Carol"] = {"phone": "9988776655", "email": "carol@email.com"}

with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=2)

with open("contacts.json") as f:
    loaded = json.load(f)
for name, info in loaded.items():
    print(f"{name}: {info['phone']} | {info['email']}")
import os; os.remove("contacts.json")

# Exercise 4
import random, string

def generate_password(length=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

for _ in range(5):
    print(generate_password())

# Exercise 5
def load_number_from_file(filename):
    try:
        with open(filename) as f:
            return float(f.readline().strip())
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError:
        print("Invalid number in file")
        return None

with open("num.txt", "w") as f: f.write("42.5\n")
print(load_number_from_file("num.txt"))       # 42.5
print(load_number_from_file("missing.txt"))   # File not found
with open("bad.txt", "w") as f: f.write("hello\n")
print(load_number_from_file("bad.txt"))       # Invalid number in file
import os; os.remove("num.txt"); os.remove("bad.txt")
"""
