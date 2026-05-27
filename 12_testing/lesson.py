# ============================================================
# MODULE 12: Testing with pytest
# Day 8 of 10-Day Python Intensive
# ============================================================
# pip install pytest pytest-cov
# Run tests: pytest test_examples.py -v
# Coverage:  pytest test_examples.py --cov=lesson --cov-report=term
# ============================================================

# ─────────────────────────────────────────────
# FUNCTIONS TO TEST (the "code under test")
# ─────────────────────────────────────────────

def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def fizzbuzz(n: int) -> str:
    """Return 'FizzBuzz', 'Fizz', 'Buzz', or the number as string."""
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n % 15 == 0: return "FizzBuzz"
    if n % 3  == 0: return "Fizz"
    if n % 5  == 0: return "Buzz"
    return str(n)

def celsius_to_fahrenheit(c: float) -> float:
    return round(c * 9 / 5 + 32, 2)

def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def find_max(numbers: list) -> float:
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


# ─────────────────────────────────────────────
# CLASS TO TEST
# ─────────────────────────────────────────────

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self._balance = initial_balance
        self._transactions: list[dict] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append({"type": "deposit", "amount": amount})
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: balance={self._balance}, requested={amount}")
        self._balance -= amount
        self._transactions.append({"type": "withdrawal", "amount": amount})
        return self._balance

    def get_transaction_count(self) -> int:
        return len(self._transactions)

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


# ─────────────────────────────────────────────
# DATA PIPELINE FUNCTION (integration-style)
# ─────────────────────────────────────────────

def process_employee_data(records: list[dict]) -> dict:
    """
    Process a list of employee dicts.
    Returns: { avg_salary, max_salary, dept_counts, flagged_ids }
    """
    if not records:
        return {"avg_salary": 0, "max_salary": 0, "dept_counts": {}, "flagged_ids": []}

    salaries = [r["salary"] for r in records]
    dept_counts = {}
    flagged = []

    for r in records:
        dept = r.get("department", "Unknown")
        dept_counts[dept] = dept_counts.get(dept, 0) + 1
        if r["salary"] < 0:
            flagged.append(r["id"])

    return {
        "avg_salary":  round(sum(salaries) / len(salaries), 2),
        "max_salary":  max(salaries),
        "dept_counts": dept_counts,
        "flagged_ids": flagged,
    }


# ─────────────────────────────────────────────
# TESTING CONCEPTS (see test_examples.py for tests)
# ─────────────────────────────────────────────
"""
PYTEST QUICK REFERENCE
══════════════════════
Install    : pip install pytest pytest-cov
Run all    : pytest
Run file   : pytest test_examples.py
Verbose    : pytest -v
One test   : pytest -v -k "test_divide"
Coverage   : pytest --cov=lesson --cov-report=term-missing

ASSERTIONS
──────────
assert result == expected
assert result > 0
assert "substring" in result
assert result is None
assert isinstance(result, list)
with pytest.raises(ValueError): risky_call()
with pytest.raises(ValueError, match="pattern"): risky_call()

FIXTURES  (@pytest.fixture)
────────────────────────────
def setup resources, yield them, teardown after yield
scope="function"  (default) — new instance per test
scope="module"   — one instance for the whole module
scope="session"  — one instance across all tests

MARKERS
───────
@pytest.mark.skip(reason="...")
@pytest.mark.skipif(condition, reason="...")
@pytest.mark.parametrize("input,expected", [(1,"1"), (3,"Fizz")])

STRUCTURE — AAA pattern
───────────────────────
def test_something():
    # Arrange — set up
    account = BankAccount("Alice", 100)
    # Act — execute
    account.deposit(50)
    # Assert — verify
    assert account.balance == 150
"""
