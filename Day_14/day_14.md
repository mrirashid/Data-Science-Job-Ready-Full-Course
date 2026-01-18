# Day 14: Classic Programming Problems and Algorithms

## Overview

Day 14 focused on solving classic programming problems and implementing fundamental algorithms in Python. These problems are commonly encountered in coding interviews and help build strong problem-solving skills.

---

## Problems Solved

### 1. Two Sum Problem

**File:** `two_sum.py`

Implemented the classic Two Sum problem using a hash map for O(n) time complexity. Given an array and a target, find two numbers that add up to the target.

```python
def two_sum(nums, target):
    seen = {}  
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
```

**Key Concept:** Using a dictionary to store previously seen values for constant-time lookups.

---

### 2. Palindrome Check with String Slicing

**File:** `slicing.py`

Checked if a string is a palindrome using string slicing and filtering. Handled case-insensitivity and ignored non-alphanumeric characters.

```python
s = 'Race car'
c = ''.join(x.lower() for x in s if x.isalnum())
print(c == c[::-1])  # True
```

**Key Concept:** Using `[::-1]` for string reversal and generator expressions for filtering.

---

### 3. Anagram Detection with Frequency Counting

**File:** `frequency.py`

Detected anagrams using two approaches:
- Using `Counter` from collections module
- Using `sorted()` for character comparison

```python
from collections import Counter
print(Counter('silent') == Counter('listen'))  # True
print(sorted('evil') == sorted('vile'))  # True
```

**Key Concept:** Anagrams have identical character frequencies.

---

### 4. Flatten Nested Lists with Recursion

**File:** `recursion.py`

Implemented a recursive function to flatten arbitrarily nested lists into a single-level list.

```python
def flat(l):
    r = []
    for x in l:
        if isinstance(x, list): r += flat(x)
        else: r.append(x)
    return r

print(flat([1, [2, [3, 4]]]))  # [1, 2, 3, 4]
```

**Key Concept:** Recursive traversal to handle arbitrary nesting depth.

---

### 5. FizzBuzz Problem

**File:** `logic_gate.py`

Solved the classic FizzBuzz problem using conditional expressions and list comprehensions.

```python
for i in range(1, 16):
    print('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)
```

**Key Concept:** Chained ternary operators and divisibility checks.

---

### 6. Remove Duplicates While Preserving Order

**File:** `deduplication.py`

Removed duplicate elements from a list while preserving the original order of first occurrences.

```python
def dedup(l):
    s = set()
    r = []
    for x in l:
        if x not in s:
            s.add(x)
            r.append(x)
    return r
```

**Key Concept:** Using a set for O(1) membership checks while maintaining insertion order with a list.

---

### 7. Binary Search Algorithm

**File:** `binary_search.py`

Implemented the binary search algorithm to find an element in a sorted array with O(log n) time complexity.

```python
def bs(a, t):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == t: return m
        if a[m] < t: l = m + 1
        else: r = m - 1
    return -1
```

**Key Concept:** Divide and conquer approach by repeatedly halving the search space.

---

### 8. Find Missing Number

**File:** `missing_number.py`

Found the missing number in a sequence from 1 to n using the mathematical sum formula.

```python
nums = list(range(1, 101))
nums.remove(57)
n = 100
print(n * (n + 1) // 2 - sum(nums))  # 57
```

**Key Concept:** Using the formula n(n+1)/2 to calculate expected sum and finding the difference.

---

### 9. Group Items by Key

**File:** `grouping.py`

Grouped items by a common key using `itertools.groupby`.

```python
from itertools import groupby
items = [{'c': 'x'}, {'c': 'x'}, {'c': 'y'}]
items = sorted(items, key=lambda x: x['c'])

for k, g in groupby(items, key=lambda x: x['c']):
    print(k, list(g))
```

**Key Concept:** Data must be sorted by the grouping key before using `groupby`.

---

### 10. Merge Two Sorted Arrays

**File:** `merge_sorted.py`

Implemented the merge operation from merge sort to combine two sorted arrays into one sorted array.

```python
def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

**Key Concept:** Two-pointer technique for merging sorted sequences in O(n + m) time.

---

## Files Created

| File | Problem Type |
|------|--------------|
| `two_sum.py` | Hash Map / Array |
| `slicing.py` | String Manipulation |
| `frequency.py` | Anagram Detection |
| `recursion.py` | Recursive Algorithms |
| `logic_gate.py` | FizzBuzz / Conditionals |
| `deduplication.py` | Set Operations |
| `binary_search.py` | Search Algorithms |
| `missing_number.py` | Mathematical Logic |
| `grouping.py` | Data Grouping |
| `merge_sorted.py` | Sorting Algorithms |

---

## Key Takeaways

- Hash maps (dictionaries) provide O(1) lookups and are essential for many optimization problems
- String slicing with `[::-1]` is a Pythonic way to reverse strings
- The `Counter` class simplifies frequency counting operations
- Recursion is powerful for problems with nested or hierarchical structures
- Binary search achieves O(log n) time complexity on sorted data
- Mathematical formulas can solve certain problems more efficiently than iteration
- The `groupby` function requires sorted input to work correctly
- The two-pointer technique is useful for merging and comparing sorted sequences
