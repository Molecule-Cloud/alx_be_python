# Python Functions and Data Structures Assignment

This project focuses on mastering fundamental Python concepts including functions, data structures, modules, and variable scope management.

## Project Objectives

By completing this project, you will:

- Define and construct functions using `def` and `lambda` keywords
- Work with function parameters, arguments, default values, and keyword arguments
- Understand return values and variable scope (local vs global)
- Apply the LEGB rule (Local, Enclosing, Global, Built-in) for variable scope
- Master Python data structures: Lists, Tuples, Sets, and Dictionaries
- Create and use custom modules and import standard/external libraries
- Implement best practices for writing clean, maintainable, and reusable code

## Repository Structure

```
alx_be_python/
└── fns_and_dsa/
    ├── arithmetic_operations.py
    ├── shopping_list_manager.py
    ├── explore_datetime.py
    └── temp_conversion_tool.py
```

## Tasks

### Task 0: Arithmetic Operations Function

**File:** `arithmetic_operations.py`

Create a function `perform_operation(num1, num2, operation)` that performs basic arithmetic operations.

**Requirements:**
- Parameters: `num1` (float), `num2` (float), `operation` (string)
- Supported operations: 'add', 'subtract', 'multiply', 'divide'
- Handle division by zero appropriately
- Return the result of the operation

**Example Usage:**
```python
from arithmetic_operations import perform_operation

result = perform_operation(5, 6, 'add')
print(f"Result: {result}")  # Output: Result: 11.0
```

### Task 1: Shopping List Manager

**File:** `shopping_list_manager.py`

Build an interactive shopping list manager using Python lists.

**Features:**
- Add items to the shopping list
- Remove items from the list
- View current list contents
- Exit the program

**Menu Options:**
1. Add Item
2. Remove Item
3. View List
4. Exit

### Task 2: Explore `datetime` Module

**File:** `explore_datetime.py`

Demonstrate usage of Python's `datetime` module.

**Part 1:** Display Current Date and Time
- Create function `display_current_datetime()`
- Format output as "YYYY-MM-DD HH:MM:SS"

**Part 2:** Calculate Future Date
- Create function `calculate_future_date()`
- Prompt user for number of days to add
- Display future date in "YYYY-MM-DD" format

**Example Output:**
```
Current date and time: 2024-03-25 15:30:45
Enter the number of days to add to the current date: 10
Future date: 2024-04-04
```

### Task 3: Temperature Conversion Tool

**File:** `temp_conversion_tool.py`

Create a temperature converter demonstrating variable scope with global conversion factors.

**Requirements:**
- Define global variables:
  - `FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9`
  - `CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5`
- Implement `convert_to_celsius(fahrenheit)`
- Implement `convert_to_fahrenheit(celsius)`
- Handle invalid input with error message: "Invalid temperature. Please enter a numeric value."

**Example Output:**
```
Enter the temperature to convert: 100
Is this temperature in Celsius or Fahrenheit? (C/F): F
100.0°F is 37.77777777777778°C
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/alx_be_python.git
cd alx_be_python/fns_and_dsa
```

2. Run individual scripts:
```bash
python arithmetic_operations.py
python shopping_list_manager.py
python explore_datetime.py
python temp_conversion_tool.py
```

## Key Concepts Covered

- **Functions:** Definition, parameters, return values
- **Data Structures:** Lists, Tuples, Sets, Dictionaries
- **Modules:** Creating custom modules, importing standard libraries
- **Variable Scope:** Local, global, LEGB rule, namespaces
- **Best Practices:** Clean code, maintainability, reusability

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python datetime Module](https://docs.python.org/3/library/datetime.html)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

