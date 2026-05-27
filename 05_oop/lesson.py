# ============================================================
# LESSON 5: Object-Oriented Programming (OOP)
# ============================================================

# ── 1. Defining a Class ──────────────────────────────────────
class Dog:
    # Class variable — shared by ALL instances
    species = "Canis familiaris"

    # __init__ is the constructor — runs when you create an object
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says: Woof!"

    def description(self):
        return f"{self.name} is {self.age} years old"

    # __str__ — what print(obj) shows
    def __str__(self):
        return f"Dog({self.name}, {self.age})"


# Create objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.description())
print(dog1)            # calls __str__
print(Dog.species)     # class variable

# ── 2. Inheritance ───────────────────────────────────────────
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self) -> str:
        return "..."   # base class — override in subclasses

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Cat(Animal):         # Cat inherits from Animal
    def speak(self) -> str:       # override the speak method
        return f"{self.name} says: Meow!"


class Parrot(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Squawk!"


animals = [Cat("Whiskers"), Parrot("Polly"), Cat("Mittens")]

for animal in animals:
    print(animal.speak())   # each calls its own speak()

# ── 3. Encapsulation ─────────────────────────────────────────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # __ makes it "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. New balance: Rs.{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.__balance}")

    def get_balance(self):
        return self.__balance   # controlled access to private data


account = BankAccount("Kumaresh", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: Rs.{account.get_balance()}")
# print(account.__balance)  <-- This would cause an AttributeError

# ── 4. Class & Static Methods ────────────────────────────────
class MathHelper:
    pi = 3.14159

    @classmethod
    def circle_area(cls, radius):      # cls = the class itself
        return cls.pi * radius ** 2

    @staticmethod
    def is_even(number):               # no self or cls needed
        return number % 2 == 0


print(f"Area: {MathHelper.circle_area(5):.2f}")
print(f"Is 4 even? {MathHelper.is_even(4)}")

print("\n[DONE] Lesson 5 complete!")
