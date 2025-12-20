# Day 6: Functions & Scope

## DEEP DIVE: Theory - Functions as Building Blocks

**Goal:** Master Python functions - the fundamental building blocks for code reusability, modularity, and clean data science pipelines.

**Key Concepts:**

**1. Functions Promote Reusability:** Write once, use many times - eliminates code duplication.

**2. Functions Enable Abstraction:** Hide implementation details behind a simple interface.

**3. Functions Aid Testing:** Isolated units of code are easier to test and debug.

**4. Functions Support Composition:** Small functions combine to create complex workflows.

---

## Syntax Spotlight: Function Fundamentals

**Goal:** Understand core function syntax including parameters, return values, and type hints.

```python
def calculate_area(radius: float) -> float:
    """Returns area of circle. Input float."""
    if radius < 0:
        return 0
    return 3.14 * (radius**2)

# Main execution
r = 5
print(calculate_area(r))
```

**The Mechanics:**

- **Function definition:** `def function_name(parameters):` declares a reusable code block.
- **Type hints:** `radius: float` and `-> float` document expected types (not enforced at runtime).
- `radius: float`: Parameter type annotation - indicates input should be float.
- `-> float`: Return type annotation - indicates function returns float.
- **Docstring:** `"""..."""` documents function purpose for users and IDEs.
- **Return statement:** Exits function and sends value back to caller.
- **Guard clause:** `if radius < 0: return 0` validates input and prevents invalid calculations.

---

## DEEP DIVE: Micro-Challenge - The Logic Gate

**Goal:** Build a simple boolean function that checks if a number is even - demonstrating the power of single-purpose functions.

```python
# Finding even number using function
def is_even(num):
    return num % 2 == 0

result = is_even(20)
print(result)
```

**The Mechanics:**

- **Single Responsibility:** Function does one thing well - checks if number is even.
- **Modulo operator:** `num % 2 == 0` returns True if no remainder, False otherwise.
- **Boolean return:** Function returns True/False, ideal for conditional logic.
- **Result:** `True` - because 20 is divisible by 2 with no remainder.
- **Reusability:** Can be used in loops, filters, conditionals throughout your code.

**Alternative Implementations:**

```python
# Bitwise AND (faster for large numbers)
def is_even(num):
    return num & 1 == 0

# Lambda function (one-liner)
is_even = lambda num: num % 2 == 0

# With type hints (production code)
def is_even(num: int) -> bool:
    """Check if integer is even."""
    return num % 2 == 0
```

**Data Science Application:** Filtering even/odd indices, splitting datasets, conditional feature engineering, binary classification logic.

---

## DEEP DIVE: Micro-Challenge - The Default Gateway

**Goal:** Use default parameter values to create flexible functions with sensible fallbacks.

```python
# Function connect the port
def connect(port=3306):
    print(f"Connect the port: {port}")

connect()
print(connect(5432))
```

**The Mechanics:**

- **Default parameter:** `port=3306` provides fallback value when argument not supplied.
- **First call:** `connect()` uses default MySQL port 3306.
- **Second call:** `connect(5432)` overrides default with PostgreSQL port 5432.
- **The Problem:** Second `print()` prints `None` because `connect()` doesn't return a value.
- **Function Side Effects:** `print()` inside function is a side effect, not a return value.

**Critical Understanding:**

```python
# INCORRECT - Trying to print None
print(connect(5432))  # Prints: "Connect the port: 5432" then "None"

# CORRECT - Function handles its own output
connect(5432)  # Prints: "Connect the port: 5432"

# BETTER - Return value for flexibility
def connect(port=3306):
    return f"Connect the port: {port}"

result = connect(5432)
print(result)  # Prints: "Connect the port: 5432"
```

**Data Science Application:** Database connections with default configs, API calls with default parameters, model training with default hyperparameters, configuration management.

---

## DEEP DIVE: Micro-Challenge - The Pure Returns

**Goal:** Understand the difference between printing and returning - a critical distinction for function composition.

```python
# Write a function to add (a, b) and prints it
res = add(5, 5)
print(res)  # It shows None

# Proper way to define it using function
def add(a, b):
    return a + b

res = add(5, 5)
print(res)
```

**The Mechanics:**

- **The Problem:** Original function prints result but doesn't return it - can't use result in calculations.
- **The Solution:** `return a + b` sends value back to caller for reuse.
- **Return vs Print:** `return` makes values available; `print()` only displays them.
- **Function Composition:** Returned values can be used as inputs to other functions.
- **Result:** `10` - sum of 5 + 5 properly returned and printed.

**Function Purity Comparison:**

```python
# IMPURE - Side effect (print), no return
def add_impure(a, b):
    print(a + b)  # Can't reuse result

# PURE - Returns value, no side effects
def add_pure(a, b):
    return a + b  # Result can be reused

# Why it matters
result1 = add_impure(5, 5)  # Prints 10, result1 = None
result2 = add_pure(5, 5)    # result2 = 10

# Composition requires returns
total = add_pure(5, 5) + add_pure(3, 3)  # 10 + 6 = 16
total = add_impure(5, 5) + add_impure(3, 3)  # Error! Can't add None
```

**Data Science Application:**

- **Pure functions:** Data transformations, feature engineering, metric calculations
- **Testability:** Pure functions are easier to test (no side effects)
- **Pipeline building:** Chain transformations using return values
- **Debugging:** Returned values can be inspected at each step

---

## DEEP DIVE: Micro-Challenge - The Scope Fortress

**Goal:** Understand variable scope - local vs global variables and why functions can't modify global variables by default.

```python
# Create a global variable and change in function
x = 10

def change_x():
    x = 20
    return x

change_x()
print(x)  # It prints 10 not 20
```

**The Mechanics:**

- **Global scope:** `x = 10` creates variable accessible throughout module.
- **Local scope:** `x = 20` inside function creates NEW local variable (doesn't modify global).
- **Scope isolation:** Function's `x` is separate from global `x` - protects against accidental changes.
- **Result:** Global `x` remains 10 because function created local copy.
- **Return value:** `change_x()` returns 20, but we don't capture it.

**Scope Resolution (LEGB Rule):**

```python
# L - Local (function)
# E - Enclosing (nested functions)
# G - Global (module)
# B - Built-in (Python)

x = 10  # Global

def change_x():
    x = 20  # Local (shadows global)
    return x

print(change_x())  # 20 (local value)
print(x)           # 10 (global unchanged)

# To modify global (not recommended)
def change_x_global():
    global x
    x = 20
    return x

change_x_global()
print(x)  # 20 (global modified)

# BETTER - Return new value
def change_x_pure(value):
    return value + 10

x = change_x_pure(x)  # x = 20 (explicit assignment)
```

**Best Practices:**

```python
# BAD - Modifying global state
total = 0
def add_to_total(n):
    global total
    total += n

# GOOD - Pure function with return
def add(a, b):
    return a + b

total = 0
total = add(total, 5)  # Explicit, clear, testable
```

**Data Science Application:**

- **Avoid global state:** Prevents bugs in data pipelines and parallel processing
- **Pure functions:** Make code predictable and testable
- **Function parameters:** Pass data explicitly rather than relying on globals
- **Configuration:** Use function parameters or class attributes instead of global variables

---

## Key Takeaways - Day 6

1. **Functions Enable Reusability:** Write once, use many times - eliminates duplication and reduces bugs.
2. **Return vs Print:** Always `return` values for reusability; `print()` is only for display/debugging.
3. **Default Parameters:** Provide sensible defaults while allowing customization when needed.
4. **Type Hints:** Document expected types with `param: type` and `-> return_type` (not enforced).
5. **Scope Isolation:** Local variables don't affect global variables - protects against side effects.
6. **Pure Functions:** No side effects, same input = same output - easier to test and reason about.
7. **Single Responsibility:** Functions should do one thing well - promotes modularity and composition.

---

## Common Function Patterns

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# Type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Multiple parameters
def add(a: int, b: int) -> int:
    return a + b

# Variable arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

# Keyword arguments (**kwargs)
def print_info(**info):
    for key, val in info.items():
        print(f"{key}: {val}")

# Docstrings
def calculate_area(radius: float) -> float:
    """
    Calculate area of circle.

    Args:
        radius: Circle radius (must be non-negative)

    Returns:
        Area of circle (pi * r^2)
    """
    return 3.14 * radius ** 2

# Lambda functions (anonymous)
square = lambda x: x ** 2
add = lambda a, b: a + b

# Guard clauses (early returns)
def divide(a, b):
    if b == 0:
        return None  # Guard clause
    return a / b

# Function composition
def clean_data(data):
    return remove_nulls(normalize(validate(data)))
```

---

## Scope Examples

```python
# Global scope
x = 10

# Local scope
def func():
    y = 20  # Local to func
    return y

# Enclosing scope (nested functions)
def outer():
    z = 30
    def inner():
        return z  # Accesses enclosing scope
    return inner()

# Built-in scope
print(len([1, 2, 3]))  # len is built-in

# LEGB lookup order
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # Prints: "local"

    inner()
    print(x)  # Prints: "enclosing"

outer()
print(x)  # Prints: "global"
```
