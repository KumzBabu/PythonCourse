# ============================================================
# EXERCISES 2: Control Flow
# Try to solve each exercise before looking at the solution!
# ============================================================

# Exercise 1: Grade Calculator
# Ask the user to enter a score (0–100).
# Print the grade: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
# YOUR CODE HERE:


# Exercise 2: FizzBuzz (Classic!)
# Print numbers 1 to 50.
# But: print "Fizz" for multiples of 3,
#      print "Buzz" for multiples of 5,
#      print "FizzBuzz" for multiples of BOTH 3 and 5.
# Hint: use the % (modulo) operator
# YOUR CODE HERE:


# Exercise 3: Multiplication Table
# Ask the user for a number.
# Print its multiplication table from 1 to 10.
# Example output for 5:
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
# YOUR CODE HERE:


# Exercise 4: Guess the Number
# Generate a random number between 1 and 10 (use: import random; n = random.randint(1,10))
# Keep asking the user to guess until they get it right.
# Print "Too high!", "Too low!", or "Correct! You got it in X tries!"
# YOUR CODE HERE:


# Exercise 5: Sum of Digits
# Ask the user to enter any number.
# Calculate and print the sum of its digits.
# Example: 1234 --> 1+2+3+4 = 10
# Hint: convert to string and loop over each character
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS (don't peek until you've tried!)
# ============================================================
"""
# Exercise 1
score = int(input("Enter score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Exercise 2
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 3
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Exercise 4
import random
secret = random.randint(1, 10)
tries = 0
while True:
    guess = int(input("Guess (1-10): "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {tries} tries!")
        break

# Exercise 5
num = input("Enter a number: ")
total = sum(int(d) for d in num if d.isdigit())
print(f"Sum of digits: {total}")
"""
