# Day 2: Logic, Control Flow & Truthiness

## DEEP DIVE: Theory - The Floating-Point Trap

**Goal:** Understand why floating-point arithmetic can produce unexpected results and how to handle it safely.

**The Challenge:** Does `0.1 + 0.2 == 0.3`?

```python
if round(0.1 + 0.2, 10) == 0.3:
    print(True)
else:
    print(False)
```

**The Mechanics:**

- Floats are stored in binary IEEE 754 format, which cannot precisely represent many decimal fractions.
- `0.1 + 0.2` actually equals `0.30000000000000004` in binary representation.
- **Solution:** Use `round()` to a reasonable precision (e.g., 10 decimal places) before comparison.
- **Critical for Data Science:** Never use `==` for direct float comparison. Use `math.isclose()` or round to avoid bugs in financial calculations, statistical analysis, or machine learning algorithms.

---

## Syntax Spotlight: Logic & Control Flow

**Goal:** Master efficient conditional logic patterns used in production code.

```python
score = 85

## The Efficient Ladder
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# Ternary Operator (One-Line Logic)
status = "Pass" if score >= 70 else "Fail"
```

**The Mechanics:**

- **if-elif-else ladder:** Python evaluates conditions top-to-bottom and stops at the first `True` condition.
- **Order matters:** Place the most restrictive condition first (e.g., `>= 90` before `>= 80`).
- **Ternary operator:** Compact syntax for simple binary decisions: `value_if_true if condition else value_if_false`.
- **Best Practice:** Use ternary for simple assignments, if-elif-else for complex multi-branch logic.

---

## DEEP DIVE: Micro-Challenge - The Ternary Packet

**Goal:** Use the ternary operator to assign pass/fail status based on a score threshold.

```python
score = 85
status = "Pass" if score >= 70 else "Fail"
print(status)
```

**The Mechanics:**

- The ternary operator is Python's implementation of a **conditional expression**.
- Syntax: `<expression_if_true> if <condition> else <expression_if_false>`
- **Memory Efficiency:** Only the selected expression is evaluated (lazy evaluation).
- **Use Case:** Ideal for quick variable assignments, inline logic in f-strings, or list comprehensions.

---

## DEEP DIVE: Micro-Challenge - Short-Circuiting

**Goal:** Understand how Python optimizes boolean expressions with **short-circuit evaluation**.

```python
user = None
status = "Access Granted" if user is not None and user.has_admin_access else "Access Denied"
print(status)
```

**The Mechanics:**

- **Short-Circuit AND (`and`):** If the first operand is `False`, Python never evaluates the second operand.
- In this example: Since `user is not None` evaluates to `False`, Python skips `user.has_admin_access` (which would raise an `AttributeError`).
- **Short-Circuit OR (`or`):** If the first operand is `True`, the second is never evaluated.
- **Critical Application:** Prevents crashes when accessing attributes/methods on potentially `None` objects.
- **Data Science Use:** Safe DataFrame column access, API response validation, database query results.

---

## DEEP DIVE: Micro-Challenge - The Truthiness Inspector

**Goal:** Understand Python's concept of "truthiness" - how non-boolean values behave in boolean contexts.

```python
data = []
if data:
    print("Data is available")
else:
    print("No data found")
```

**The Mechanics:**
Python evaluates **truthiness** for all objects in boolean contexts:

**Falsy Values** (evaluate to `False`):

- `None`
- `False`
- Zero of any numeric type: `0`, `0.0`, `0j`
- Empty sequences: `''`, `[]`, `()`
- Empty mappings: `{}`
- Custom objects with `__bool__()` or `__len__()` returning `False` or `0`

**Truthy Values** (evaluate to `True`):

- Everything else!
- Non-zero numbers: `1`, `-1`, `3.14`
- Non-empty sequences: `"hello"`, `[1, 2]`, `(1,)`
- Non-empty mappings: `{"key": "value"}`

**Best Practice:**

- Use explicit checks for `None`: `if x is not None:`
- Use truthiness for collections: `if data:` instead of `if len(data) > 0:`
- **Data Science Application:** Check if DataFrames/lists are empty, validate API responses, filter null values.

---

## Key Takeaways - Day 2

1. **Floating-Point Precision:** Always use `round()` or `math.isclose()` for float comparisons.
2. **Efficient Logic:** Order conditions from most to least restrictive in if-elif ladders.
3. **Ternary Operators:** Perfect for simple binary decisions in one line.
4. **Short-Circuiting:** Prevents crashes and improves performance by skipping unnecessary evaluations.
5. **Truthiness:** Leverage Python's implicit boolean conversion for cleaner, more Pythonic code.
