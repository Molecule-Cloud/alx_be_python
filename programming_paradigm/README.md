# Programming Paradigms & Exception Handling

**Weight:** 1  
**Project Duration:** Nov 24, 2025 12:00 AM - Dec 1, 2025 12:00 AM

## Overview

This project introduces fundamental concepts of Object-Oriented Programming (OOP) in Python and Exception Handling. You'll learn about classes, objects, error handling, and basic testing practices through hands-on implementation.

## Learning Objectives

By the end of this project, you will be able to:

- Explain core OOP concepts: classes, objects, encapsulation, and abstraction
- Discuss the significance of OOP in software development
- Define classes and create objects in Python
- Understand class attributes, instance methods, and the `self` keyword
- Differentiate between syntax errors and exceptions
- Identify common Python exceptions and their causes
- Utilize `try`, `except`, `else`, and `finally` blocks effectively
- Raise exceptions and create custom exceptions
- Explain the importance of testing in software development
- Write basic unit tests using Python's `unittest` module

## Repository Structure

```
alx_be_python/
└── programming_paradigm/
    ├── bank_account.py
    ├── main-0.py
    ├── robust_division_calculator.py
    ├── main.py
    ├── simple_calculator.py
    ├── test_simple_calculator.py
    └── library_management.py
```

## Tasks

### Task 0: Simple Bank Account Class

**Files:** `bank_account.py`, `main-0.py`

Create a `BankAccount` class that encapsulates banking operations with command-line interaction.

**Features:**
- Initialize account with optional starting balance (default: 0)
- Deposit funds
- Withdraw funds (with sufficient balance check)
- Display current balance

**Usage Examples:**

```bash
# Deposit money
python main-0.py deposit:50
# Output: Deposited: $50

# Withdraw money
python main-0.py withdraw:20
# Output: Withdrew: $20

# Attempt withdrawal with insufficient funds
python main-0.py withdraw:150
# Output: Insufficient funds.

# Display balance
python main-0.py display
# Output: Current Balance: $[amount]
```

**Implementation Requirements:**
- Use encapsulation principles
- Implement `__init__`, `deposit()`, `withdraw()`, and `display_balance()` methods
- Handle insufficient funds gracefully

---

### Task 1: Robust Division Calculator

**Files:** `robust_division_calculator.py`, `main.py`

Implement a division calculator with comprehensive error handling.

**Features:**
- Handle division by zero
- Handle non-numeric inputs
- Provide clear error messages

**Usage Examples:**

```bash
# Normal division
python main.py 10 5
# Output: The result of the division is 2.0

# Division by zero
python main.py 10 0
# Output: Error: Cannot divide by zero.

# Invalid input
python main.py ten 5
# Output: Error: Please enter numeric values only.
```

**Implementation Requirements:**
- Create `safe_divide(numerator, denominator)` function
- Use `try-except` blocks to catch `ZeroDivisionError` and `ValueError`
- Return appropriate messages for all scenarios

---

### Task 2: Unit Tests for Simple Calculator

**Files:** `simple_calculator.py` (provided), `test_simple_calculator.py`

Write comprehensive unit tests for the `SimpleCalculator` class.

**Testing Requirements:**
- Test all four operations: add, subtract, multiply, divide
- Include edge cases (especially division by zero)
- Use `unittest.TestCase` and assertions

**Running Tests:**

```bash
python -m unittest test_simple_calculator.py
```

**Test Structure Example:**

```python
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
```

**Implementation Requirements:**
- Test positive, negative, and zero values
- Test division by zero returns `None`
- Cover multiple scenarios for each operation

---

### Task 3: Library Management System

**Files:** `library_management.py`, `main.py` (provided)

Implement a basic library system using OOP principles.

**Classes to Implement:**

**Book Class:**
- Public attributes: `title`, `author`
- Private attribute: `_is_checked_out`
- Methods to check out and return books

**Library Class:**
- Private list: `_books`
- Methods: `add_book()`, `check_out_book(title)`, `return_book(title)`, `list_available_books()`

**Expected Output:**

```
Available books after setup:
Brave New World by Aldous Huxley
1984 by George Orwell

Available books after checking out '1984':
Brave New World by Aldous Huxley

Available books after returning '1984':
Brave New World by Aldous Huxley
1984 by George Orwell
```

**Implementation Requirements:**
- Use encapsulation (private attributes)
- Manage book availability states
- Track collection of book instances

## Key Concepts Covered

### Object-Oriented Programming
- **Classes and Objects:** Blueprint vs instances
- **Encapsulation:** Hiding internal state, using private attributes
- **Abstraction:** Exposing only necessary functionality
- **Methods:** Instance methods, `self` keyword

### Exception Handling
- **Common Exceptions:** `ValueError`, `ZeroDivisionError`
- **Try-Except Blocks:** Catching and handling errors
- **Custom Exceptions:** Creating specific error types
- **Finally Block:** Cleanup code that always runs

### Testing
- **Unit Testing:** Testing individual components
- **Test Cases:** Structured test methods
- **Assertions:** Verifying expected outcomes
- **Test Runners:** Executing test suites

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/your-username/alx_be_python.git
cd alx_be_python/programming_paradigm
```

2. Complete each task in order

3. Test your implementations using the provided test scripts

4. Run unit tests to verify correctness

## Tips for Success

- Start with the simplest implementation, then refine
- Test each method as you implement it
- Use meaningful variable and method names
- Comment your code for clarity
- Handle edge cases thoughtfully
- Run tests frequently during development

## Resources

- Python Official Documentation
- unittest Module Documentation
- OOP Best Practices in Python
- Exception Handling Guidelines

---

**Repository:** [alx_be_python](https://github.com/your-username/alx_be_python)  
**Directory:** programming_paradigm