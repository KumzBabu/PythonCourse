# ============================================================
# EXERCISES 1: Python Basics
# Try to solve each exercise before looking at the solution!
# ============================================================

# Exercise 1: Personal Info
# Create variables for your name, age, and city.
# Print a sentence: "My name is X, I am Y years old, from Z."
# YOUR CODE HERE:
name = "Kumaresh"
age = 25
city = "Chennai"
print(f"My name is {name}, I am {age} years old, from {city}.")
# Exercise 2: Simple Calculator
# Ask the user for two numbers (use input()), add them and print the result.
# Hint: input() returns a string, so you need int() or float() to convert.
# YOUR CODE HERE:
x = float(input("Enter first number: "))
Y = float(input("Enter second number: "))
print(f"{x} + {Y} = {x + Y}")
# Exercise 3: String Magic
# Create a variable with the value "  hello world  "
# Print it: stripped, uppercased, and its length (after stripping)
# YOUR CODE HERE:
s = "  hello world  "
print(s.strip())
print(s.strip().upper())
print(len(s.strip()))# Exercise 4: Temperature Converter
# Write code to convert 100 degrees Celsius to Fahrenheit.
# Formula: F = (C × 9/5) + 32
# Print: "100°C = X°F"
# YOUR CODE HERE:
x = 100
F = (x * 9/5) + 32  
print(f"{x}°C = {F}°F")
# ============================================================
# SOLUTIONS (don't peek until you've tried!)
# ============================================================
"""
# Exercise 1
name = "Kumaresh"
age = 25
city = "Chennai"
print(f"My name is {name}, I am {age} years old, from {city}.")

# Exercise 2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"{a} + {b} = {a + b}")

# Exercise 3
s = "  hello world  "
print(s.strip())
print(s.strip().upper())
print(len(s.strip()))

# Exercise 4
celsius = 100
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
"""
