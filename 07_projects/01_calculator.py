# ============================================================
# PROJECT 1: Simple Calculator
# Concepts used: functions, loops, conditionals, error handling
# ============================================================

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    print("=" * 30)
    print("   [CALC] Simple Calculator")
    print("=" * 30)

    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    while True:
        print("\nOperations:")
        for key, (symbol, _) in operations.items():
            print(f"  {key}. {symbol}")
        print("  5. Quit")

        choice = input("\nChoose operation: ").strip()

        if choice == "5":
            print("Goodbye! ")
            break

        if choice not in operations:
            print("Invalid choice. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            symbol, func = operations[choice]
            result = func(a, b)
            print(f"\n  {a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    calculator()
