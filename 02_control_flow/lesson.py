# ============================================================
# LESSON 2: Control Flow — if/else and Loops
# ============================================================

# ── 1. if / elif / else ──────────────────────────────────────
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Comparison operators: == != > < >= <=
# Logical operators:    and  or  not

score = 85
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# ── 2. for Loop ──────────────────────────────────────────────
# Loop over a range of numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10 (step=2)
    print(i, end=" ")
print()

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# ── 3. while Loop ────────────────────────────────────────────
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1   # same as: count = count + 1

# ── 4. break & continue ──────────────────────────────────────
# break: exit the loop early
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("<-- broke at 5")

# continue: skip this iteration
for i in range(10):
    if i % 2 == 0:   # skip even numbers
        continue
    print(i, end=" ")
print("<-- only odd numbers")

# ── 5. Useful Patterns ───────────────────────────────────────
# Sum of 1 to 100
total = sum(range(1, 101))
print(f"Sum 1-100 = {total}")   # 5050

# Find if a number is prime
num = 17
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
print(f"{num} is prime: {is_prime}")

print("\n[DONE] Lesson 2 complete!")
