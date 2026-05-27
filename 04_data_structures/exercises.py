# ============================================================
# EXERCISES 4: Data Structures (List, Dict, Tuple, Set)
# Try to solve each exercise before looking at the solution!
# ============================================================

# Exercise 1: List Operations
# Start with: numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
# a) Print the list sorted in descending order (don't modify original)
# b) Print the max, min, and average
# c) Print only numbers greater than 5 (use list comprehension)
# YOUR CODE HERE:


# Exercise 2: Shopping Cart
# Create an empty list called cart.
# Add: "apple", "banana", "milk", "eggs"
# Remove "banana"
# Print the final cart and total item count.
# YOUR CODE HERE:


# Exercise 3: Student Grades Dictionary
# Create a dict with 5 students and their scores:
#   {"Alice": 85, "Bob": 92, "Carol": 78, "Dave": 95, "Eve": 88}
# a) Print the student with the highest score.
# b) Print all students who scored above 85.
# c) Add a new student "Frank" with score 73.
# d) Print the class average.
# YOUR CODE HERE:


# Exercise 4: Count Unique Words
# Given the sentence below, find how many UNIQUE words it contains.
# (ignore case, treat "the" and "The" as the same word)
# sentence = "To be or not to be that is the question to be answered"
# Hint: use a set!
# YOUR CODE HERE:


# Exercise 5: Merge and De-duplicate
# You have two lists:
#   list1 = [1, 2, 3, 4, 5]
#   list2 = [4, 5, 6, 7, 8]
# Create a new list that contains all unique numbers from BOTH lists, sorted.
# Expected: [1, 2, 3, 4, 5, 6, 7, 8]
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS (don't peek until you've tried!)
# ============================================================
"""
# Exercise 1
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(sorted(numbers, reverse=True))
print(f"Max: {max(numbers)}, Min: {min(numbers)}, Avg: {sum(numbers)/len(numbers):.1f}")
print([n for n in numbers if n > 5])

# Exercise 2
cart = []
for item in ["apple", "banana", "milk", "eggs"]:
    cart.append(item)
cart.remove("banana")
print(cart)
print(f"Total items: {len(cart)}")

# Exercise 3
grades = {"Alice": 85, "Bob": 92, "Carol": 78, "Dave": 95, "Eve": 88}

top = max(grades, key=lambda s: grades[s])
print(f"Highest: {top} ({grades[top]})")

above_85 = [name for name, score in grades.items() if score > 85]
print(f"Above 85: {above_85}")

grades["Frank"] = 73
avg = sum(grades.values()) / len(grades)
print(f"Average: {avg:.1f}")

# Exercise 4
sentence = "To be or not to be that is the question to be answered"
unique_words = set(sentence.lower().split())
print(f"Unique words: {len(unique_words)}")

# Exercise 5
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged = sorted(set(list1) | set(list2))
print(merged)
"""
