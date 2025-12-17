# Day 3: Loops & Iteration Patterns

## DEEP DIVE: Theory - Loop Fundamentals

**Goal:** Master Python's two core loop constructs: `for` (definite iteration) and `while` (indefinite iteration).

**Key Concepts:**

**1. For Loops:** Used when you know how many iterations you need (iterate over sequences or ranges).

**2. While Loops:** Used when iteration depends on a condition (you don't know how many iterations upfront).

**3. Loop Control:**

- `break`: Immediately exits the loop entirely.
- `continue`: Skips the rest of the current iteration and jumps to the next one.

---

## Syntax Spotlight: Loop Basics

**Goal:** Understand the syntax and use cases for `for` and `while` loops.

```python
# The Infinite Input Pattern
while True:
    pwd = input("set password (min 5 chars):")
    if len(pwd) >= 5:
        print("password set")
        break  # Exit the loop
    print("Too short! Try again")
```

**The Mechanics:**

- **while True:** Creates an infinite loop that runs until explicitly broken.
- **break statement:** Terminates the loop when the condition is satisfied.
- **Use Case:** Input validation, menu systems, server loops, or any scenario requiring repeated attempts until success.
- **Critical Pattern:** This is the foundation for robust user input validation in production code.

---

## DEEP DIVE: Micro-Challenge - The String Walker

**Goal:** Iterate through each character in a string and print it on a new line.

```python
## Create a string word to every letter in new line.
word = "DATA"
for i in word:
    print(i)
```

**The Mechanics:**

- Strings are **iterable sequences** in Python - each character is an element.
- The `for` loop automatically unpacks each character one by one.
- **Memory Efficiency:** Python doesn't create a copy of the string; it references each character directly.
- **Data Science Application:** Text preprocessing, character-level tokenization for NLP, parsing CSV data, cleaning strings.

---

## DEEP DIVE: Micro-Challenge - The Efficient Skipper

**Goal:** Loop through numbers 1 to 10, but skip the number 5.

```python
## Loop through numbers 1 to 10, but skip the 5.
for i in range(1, 10):
    if i == 5:
        continue
    print(f"Number: {i}")
```

**The Mechanics:**

- **continue statement:** Immediately jumps to the next iteration, skipping all code below it.
- **Difference from break:** `break` exits the loop entirely; `continue` only skips the current iteration.
- **Use Case:** Filtering data during iteration, skipping invalid entries, handling exceptions in batch processing.
- **Data Science Application:** Skip missing values, filter outliers during data processing, ignore corrupted records in datasets.

---

## DEEP DIVE: Micro-Challenge - The Infinite Guardian

**Goal:** Ask the user for input repeatedly until they type "stop".

```python
# Ask the user for the password repeatedly
while True:
    pwd = input("Type anything: ")
    if pwd == "stop":
        print("loop stopped")
        break  # It will stop the loop immediately.
    else:
        print(f"You have typed: {pwd}")
```

**The Mechanics:**

- **Infinite Loop Pattern:** `while True` runs indefinitely until a `break` is encountered.
- **Sentinel Value:** "stop" acts as a sentinel - a special value that signals termination.
- **Comparison to For Loops:** For loops need a predefined range; while loops can run based on dynamic conditions.
- **Real-World Application:** Chat interfaces, command-line tools, streaming data processors, game loops.

---

## DEEP DIVE: Micro-Challenge - The Accumulator Pattern

**Goal:** Calculate the sum of all numbers from 1 to N (user input).

```python
# Sum of the number from 1 to N numbers
number = 0
user = int(input("Input a number: "))
for i in range(1, user + 1):
    number += i

print(number)
```

**The Mechanics:**

- **Accumulator Pattern:** Initialize a variable (`number = 0`), then update it in each iteration (`number += i`).
- **range(1, user + 1):** Generates numbers from 1 to user (inclusive). Remember: `range()` is exclusive at the end.
- **Mathematical Note:** This could be solved with the formula `n * (n + 1) // 2`, but loops demonstrate the pattern.
- **Critical Pattern:** The accumulator is fundamental to aggregations, running totals, cumulative statistics.
- **Data Science Application:** Calculate means, sums, rolling averages, cumulative returns in financial data, gradient descent in machine learning.

**Variations:**

- **Product accumulator:** Start with `product = 1`, then `product *= i` (factorial calculation).
- **List accumulator:** Start with `results = []`, then `results.append(processed_item)`.
- **String accumulator:** Start with `text = ""`, then `text += char`.

---

## Key Takeaways - Day 3

1. **For Loops:** Use when you know the number of iterations (iterate over ranges, lists, strings).
2. **While Loops:** Use when iterations depend on a condition (input validation, infinite loops with break).
3. **break vs continue:** `break` exits the loop; `continue` skips to the next iteration.
4. **Accumulator Pattern:** Initialize, iterate, and aggregate - foundational for data processing.
5. **String Iteration:** Strings are iterable sequences; you can loop through characters directly.
6. **Infinite Loop Pattern:** `while True` + `break` is the standard for input validation and event loops.
