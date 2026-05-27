# ============================================================
# EXERCISES 5: Object-Oriented Programming
# Try to solve each exercise before looking at the solution!
# ============================================================

# Exercise 1: Rectangle Class
# Create a class Rectangle with:
#   - __init__(self, width, height)
#   - area() method that returns width * height
#   - perimeter() method that returns 2 * (width + height)
#   - __str__ that prints: "Rectangle(5 x 3)"
# Test it with a few different sizes.
# YOUR CODE HERE:


# Exercise 2: Student Class
# Create a class Student with:
#   - __init__(self, name, grades=[])  where grades is a list of numbers
#   - add_grade(self, grade) to add a grade
#   - average(self) that returns the average of all grades
#   - is_passing(self) that returns True if average >= 60
#   - __str__ that shows name and average: "Alice - Avg: 85.0"
# YOUR CODE HERE:


# Exercise 3: Inheritance — Shape Hierarchy
# Create a base class Shape with:
#   - name attribute
#   - area() method that returns 0 (to be overridden)
#   - describe() method that prints "I am a {name} with area {area:.2f}"
#
# Then create two subclasses:
#   - Circle(Shape): takes radius, area = pi * r^2  (use math.pi)
#   - Triangle(Shape): takes base and height, area = 0.5 * base * height
#
# Create one of each and call describe() on them.
# YOUR CODE HERE:


# Exercise 4: Simple Bank Account
# Create a BankAccount class with:
#   - __init__(self, owner, balance=0)
#   - deposit(amount)  -- add money, print new balance
#   - withdraw(amount) -- remove money, but print "Insufficient funds!" if not enough
#   - __str__          -- "Account[Alice]: Rs.500"
#
# Test it: open an account, deposit 1000, withdraw 300, then try to withdraw 800.
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS (don't peek until you've tried!)
# ============================================================
"""
# Exercise 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

r = Rectangle(5, 3)
print(r)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")

# Exercise 2
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def is_passing(self):
        return self.average() >= 60

    def __str__(self):
        return f"{self.name} - Avg: {self.average():.1f}"

s = Student("Alice")
s.add_grade(85)
s.add_grade(92)
s.add_grade(78)
print(s)
print(f"Passing: {s.is_passing()}")

# Exercise 3
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def describe(self):
        print(f"I am a {self.name} with area {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

Circle(5).describe()
Triangle(6, 4).describe()

# Exercise 4
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited Rs.{amount}. Balance: Rs.{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew Rs.{amount}. Balance: Rs.{self.__balance}")

    def __str__(self):
        return f"Account[{self.owner}]: Rs.{self.__balance}"

acc = BankAccount("Alice")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(800)
print(acc)
"""
