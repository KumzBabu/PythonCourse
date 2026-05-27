# ============================================================
# EXERCISES 3: Functions
# Try to solve each exercise before looking at the solution!
# ============================================================

# Exercise 1: Is Even / Is Odd
# Write a function is_even(n) that returns True if n is even, False if odd.
# Test it with a few numbers.
# YOUR CODE HERE:


# Exercise 2: Factorial
# Write a function factorial(n) that returns n! (n factorial).
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Hint: use a loop (or try recursion if you're feeling adventurous!)
# YOUR CODE HERE:


# Exercise 3: Palindrome Checker
# Write a function is_palindrome(text) that returns True if the
# text reads the same forwards and backwards (ignore case & spaces).
# Example: "racecar" --> True,  "hello" --> False, "A man a plan a canal Panama" --> True
# Hint: clean the string first, then compare it to its reverse (text[::-1])
# YOUR CODE HERE:


# Exercise 4: Calculator Function
# Write a function calculate(a, b, operation) where operation is one of:
# "add", "subtract", "multiply", "divide"
# It should return the result, or "Unknown operation" if operation is invalid.
# Test all 4 operations.
# YOUR CODE HERE:


# Exercise 5: Word Frequency Counter
# Write a function word_count(sentence) that returns a dictionary
# with each word as a key and how many times it appears as the value.
# Example: "the cat sat on the mat" --> {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
# Hint: use .split() and a dict
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS (don't peek until you've tried!)
# ============================================================
"""
# Exercise 1
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# Exercise 2
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120
print(factorial(0))   # 1

# Exercise 3
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))                  # True
print(is_palindrome("hello"))                    # False
print(is_palindrome("A man a plan a canal Panama"))  # True

# Exercise 4
def calculate(a, b, operation):
    if operation == "add":      return a + b
    if operation == "subtract": return a - b
    if operation == "multiply": return a * b
    if operation == "divide":   return a / b if b != 0 else "Cannot divide by zero"
    return "Unknown operation"

print(calculate(10, 5, "add"))       # 15
print(calculate(10, 5, "divide"))    # 2.0
print(calculate(10, 0, "divide"))    # Cannot divide by zero

# Exercise 5
def word_count(sentence):
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count("the cat sat on the mat"))
"""
