# ============================================================
# MODULE 12: pytest Test Suite
# ============================================================
# Run: pytest test_examples.py -v
# With coverage: pytest test_examples.py --cov=lesson -v
# ============================================================

import pytest
from lesson import (
    add, divide, fizzbuzz, celsius_to_fahrenheit,
    is_palindrome, find_max, BankAccount, process_employee_data
)


# ─────────────────────────────────────────────
# 1. BASIC TESTS
# ─────────────────────────────────────────────

class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_zero(self):
        assert add(0, 5) == 5

    def test_floats(self):
        assert add(1.1, 2.2) == pytest.approx(3.3)   # floating-point safe


class TestDivide:
    def test_normal_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(1, 3) == pytest.approx(0.333, rel=1e-3)

    def test_zero_division_raises(self):
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)

    def test_zero_division_message(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_negative_divisor(self):
        assert divide(-10, 2) == -5.0


# ─────────────────────────────────────────────
# 2. PARAMETRIZE — test many inputs at once
# ─────────────────────────────────────────────

@pytest.mark.parametrize("n, expected", [
    (1,  "1"),
    (2,  "2"),
    (3,  "Fizz"),
    (5,  "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (9,  "Fizz"),
    (25, "Buzz"),
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected

def test_fizzbuzz_type_error():
    with pytest.raises(TypeError):
        fizzbuzz("3")

@pytest.mark.parametrize("c, f", [
    (0,   32.0),
    (100, 212.0),
    (-40, -40.0),
    (37,  98.6),
])
def test_celsius_to_fahrenheit(c, f):
    assert celsius_to_fahrenheit(c) == pytest.approx(f, rel=1e-3)

@pytest.mark.parametrize("s, expected", [
    ("racecar",     True),
    ("hello",       False),
    ("A man a plan a canal Panama", True),
    ("Was it a car or a cat I saw", True),
    ("Python",      False),
    ("",            True),
    ("a",           True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected


# ─────────────────────────────────────────────
# 3. FIXTURES — reusable setup / teardown
# ─────────────────────────────────────────────

@pytest.fixture
def empty_account():
    """A fresh account with $0."""
    return BankAccount("Test User", 0)

@pytest.fixture
def funded_account():
    """An account with $500."""
    return BankAccount("Alice", 500.0)

@pytest.fixture
def account_with_history(funded_account):
    """Account that already has some transactions."""
    funded_account.deposit(200)
    funded_account.withdraw(100)
    return funded_account


class TestBankAccount:
    def test_initial_balance(self, funded_account):
        assert funded_account.balance == 500.0

    def test_initial_balance_zero(self, empty_account):
        assert empty_account.balance == 0.0

    def test_negative_initial_balance_raises(self):
        with pytest.raises(ValueError):
            BankAccount("X", -1)

    def test_deposit_increases_balance(self, funded_account):
        funded_account.deposit(100)
        assert funded_account.balance == 600.0

    def test_deposit_returns_new_balance(self, funded_account):
        new_bal = funded_account.deposit(50)
        assert new_bal == 550.0

    def test_deposit_zero_raises(self, empty_account):
        with pytest.raises(ValueError, match="positive"):
            empty_account.deposit(0)

    def test_deposit_negative_raises(self, empty_account):
        with pytest.raises(ValueError):
            empty_account.deposit(-50)

    def test_withdraw_decreases_balance(self, funded_account):
        funded_account.withdraw(200)
        assert funded_account.balance == 300.0

    def test_withdraw_returns_new_balance(self, funded_account):
        bal = funded_account.withdraw(100)
        assert bal == 400.0

    def test_withdraw_insufficient_funds_raises(self, funded_account):
        with pytest.raises(ValueError, match="Insufficient funds"):
            funded_account.withdraw(1000)

    def test_transaction_count(self, account_with_history):
        # fixture already did deposit + withdraw = 2 transactions
        assert account_with_history.get_transaction_count() == 2

    def test_multiple_deposits(self, empty_account):
        empty_account.deposit(100)
        empty_account.deposit(200)
        empty_account.deposit(300)
        assert empty_account.balance == 600.0
        assert empty_account.get_transaction_count() == 3


# ─────────────────────────────────────────────
# 4. TESTING EDGE CASES & DATA PIPELINES
# ─────────────────────────────────────────────

class TestFindMax:
    def test_basic(self):
        assert find_max([3, 1, 4, 1, 5, 9]) == 9

    def test_single_element(self):
        assert find_max([42]) == 42

    def test_negative_numbers(self):
        assert find_max([-5, -1, -10]) == -1

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="empty"):
            find_max([])


class TestProcessEmployeeData:
    @pytest.fixture
    def sample_records(self):
        return [
            {"id": 1, "name": "Alice", "department": "Engineering", "salary": 95000},
            {"id": 2, "name": "Bob",   "department": "Marketing",   "salary": 62000},
            {"id": 3, "name": "Carol", "department": "Engineering", "salary": 120000},
        ]

    def test_average_salary(self, sample_records):
        result = process_employee_data(sample_records)
        assert result["avg_salary"] == pytest.approx(92333.33, rel=1e-3)

    def test_max_salary(self, sample_records):
        result = process_employee_data(sample_records)
        assert result["max_salary"] == 120000

    def test_dept_counts(self, sample_records):
        result = process_employee_data(sample_records)
        assert result["dept_counts"] == {"Engineering": 2, "Marketing": 1}

    def test_empty_input(self):
        result = process_employee_data([])
        assert result["avg_salary"] == 0
        assert result["dept_counts"] == {}

    def test_flags_negative_salaries(self):
        records = [
            {"id": 1, "department": "Eng", "salary": 80000},
            {"id": 99, "department": "Eng", "salary": -500},
        ]
        result = process_employee_data(records)
        assert 99 in result["flagged_ids"]
        assert 1 not in result["flagged_ids"]


# ─────────────────────────────────────────────
# 5. MOCKING (requires pytest-mock or unittest.mock)
# ─────────────────────────────────────────────

from unittest.mock import MagicMock, patch

def test_mock_bank_account_method():
    """Test code that depends on an external call."""
    account = BankAccount("Mock User", 100)
    account.deposit = MagicMock(return_value=999.0)

    result = account.deposit(100)
    account.deposit.assert_called_once_with(100)
    assert result == 999.0

def test_patch_builtin():
    """Patch open() to avoid real file I/O."""
    mock_data = '{"key": "value"}'
    with patch("builtins.open", create=True) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = mock_data
        # Any code here that calls open() will get mock_data back


# ─────────────────────────────────────────────
# 6. SKIP & XFAIL MARKERS
# ─────────────────────────────────────────────

@pytest.mark.skip(reason="Feature not implemented yet")
def test_transfer_between_accounts():
    pass

@pytest.mark.skipif(True, reason="Only runs on Linux CI")
def test_file_permissions():
    pass

@pytest.mark.xfail(reason="Known bug — fix in v2.0")
def test_known_broken():
    assert add(1, 1) == 3   # intentionally wrong
