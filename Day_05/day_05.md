# Day 5: Dictionaries, Sets & Hash Tables

## DEEP DIVE: Theory - Dictionaries as Key-Value Stores

**Goal:** Master Python dictionaries - the fundamental data structure for mapping relationships and fast lookups in data science.

**Key Concepts:**

**1. Dictionaries are Mutable:** Can add, remove, or modify key-value pairs after creation.

**2. Dictionaries use Hash Tables:** O(1) average time complexity for lookups, insertions, and deletions.

**3. Keys must be Immutable:** Strings, numbers, and tuples can be keys; lists cannot.

**4. Dictionaries are Unordered (Python < 3.7):** As of Python 3.7+, dictionaries maintain insertion order.

---

## Syntax Spotlight: Dictionary Fundamentals

**Goal:** Understand core dictionary operations including safe access and iteration.

```python
user = {"id": 1, "name": "Rashid"}

# Safe Access (.get)
# Returns None if key missing, prevents crash
email = user.get("email", "NOT FOUND")

# Iteration
for key, val in user.items():
    print(f"{key}: {val}")
```

**The Mechanics:**

- **Dictionary syntax:** `{key: value}` creates key-value mappings.
- **`.get(key, default)`:** Safe way to access values without KeyError exceptions.
- `key`: The dictionary key to look up.
- `default`: Value returned if key doesn't exist (defaults to None).
- **`.items()`:** Returns key-value pairs for iteration.
- **Memory Efficiency:** Hash tables provide constant-time lookups regardless of dictionary size.

---

## DEEP DIVE: Micro-Challenge - The Frequency Counter

**Goal:** Build a character frequency counter using dictionary patterns - a foundational technique for text analysis.

```python
# Input a string and create a dictionary
input_text = 'banana'  # defined the banana as input

# Empty frequency to count characters
frequency = {}

for characters in input_text:
    if characters in frequency:
        frequency[characters] += 1
    else:
        frequency[characters] = 1

print(f"frequency is {frequency}")
```

**The Mechanics:**

- **Pattern:** Check if key exists, increment if yes, initialize if no.
- **`if characters in frequency`:** O(1) lookup to check key existence.
- **Result:** `{'b': 1, 'a': 3, 'n': 2}` - counts each character occurrence.
- **Alternative (Modern Python):** Use `.get()` for cleaner code: `frequency[char] = frequency.get(char, 0) + 1`.
- **Even Better:** Use `collections.Counter(input_text)` for production code.
- **Data Science Application:** Word frequency analysis, feature extraction for NLP, histogram generation, categorical data counting.

**Optimized Version:**

```python
from collections import Counter
frequency = Counter('banana')
# Counter({'a': 3, 'n': 2, 'b': 1})
```

---

## DEEP DIVE: Micro-Challenge - The Safe Vault

**Goal:** Use `.get()` method to safely access dictionary values and prevent runtime errors.

```python
# Create a dictionary to access user email
user = {"id": 1, "name": "Rashidul"}

email = user.get("email", "email not found")  # to access the email

# Check the access
for key, value in user.items():
    print(f"The key is {key} and the value is {value}")
```

**The Mechanics:**

- **The Problem:** `user["email"]` would raise `KeyError` since "email" key doesn't exist.
- **The Solution:** `.get("email", "email not found")` returns default value instead of crashing.
- **Safe Access Pattern:** Always use `.get()` when a key might not exist.
- **Iteration with `.items()`:** Returns tuples of (key, value) pairs for easy unpacking.
- **Output:** Prints each key-value pair: `id: 1`, `name: Rashidul`.

**Critical Understanding:**

```python
# RISKY - Crashes if key missing
email = user["email"]  # KeyError!

# SAFE - Returns default value
email = user.get("email", "email not found")  # "email not found"

# SAFE - Check existence first
if "email" in user:
    email = user["email"]
else:
    email = "email not found"
```

**Data Science Application:** Accessing nested JSON/API responses, handling missing data fields, configuration management, feature extraction from sparse data.

---

## DEEP DIVE: Micro-Challenge - The Speed Trap

**Goal:** Compare performance of membership testing between lists and sets using hash-based lookups.

```python
# Create a list of 1 million numbers
numbers_list = list(range(1, 1000001))  # created list of 1 million

# Create a set of the same numbers
numbers_set = set(numbers_list)

# Check if -1 exists in list
if -1 in numbers_list:
    print("−1 exists in the list")
else:
    print("−1 does NOT exist in the list")

# Check if -1 exists in set
if -1 in numbers_set:
    print("−1 exists in the set")
else:
    print("−1 does NOT exist in the set")
```

**The Mechanics:**

- **List Lookup:** O(n) - must scan entire list to check membership.
- **Set Lookup:** O(1) - uses hash table for instant lookup.
- **Performance Difference:** For 1 million items, set lookup is ~1000x faster than list.
- **Memory Trade-off:** Sets use more memory than lists due to hash table overhead.
- **Result:** Both print "−1 does NOT exist" but set completes nearly instantly.

**Performance Comparison:**

```python
# List: O(n) - Linear time
# Worst case: scans all 1,000,000 elements
-1 in numbers_list  # ~50ms

# Set: O(1) - Constant time
# Hash lookup: instant regardless of size
-1 in numbers_set   # ~0.00005ms
```

**Data Science Application:**

- **Sets for membership testing:** Checking unique values, removing duplicates, validation
- **Lists for ordered data:** When you need indexing, sorting, or duplicate values
- **Data cleaning:** Finding unique categories, deduplication, set operations (union, intersection)

---

## DEEP DIVE: Micro-Challenge - The Database Merger

**Goal:** Merge dictionaries using `.update()` method to combine configurations or datasets.

```python
# Merge the dictionary
# First dictionary
defaults = {"theme": "light", "audio": "on"}
user_pref = {"theme": "dark"}

defaults.update(user_pref)

print(f"Updated the defaults Dictionary: {defaults}")
```

**The Mechanics:**

- **`.update(other_dict)`:** Merges other_dict into the original, overwriting duplicate keys.
- **In-place Operation:** Modifies `defaults` directly, doesn't create new dictionary.
- **Key Behavior:** Existing keys get overwritten, new keys get added.
- **Result:** `{'theme': 'dark', 'audio': 'on'}` - user preference overwrites default.

**Modern Python Alternatives (3.5+):**

```python
# Dictionary unpacking (creates new dict)
merged = {**defaults, **user_pref}

# Union operator (Python 3.9+)
merged = defaults | user_pref

# Keep original unchanged
merged = defaults.copy()
merged.update(user_pref)
```

**Data Science Application:**

- **Configuration management:** Merging default settings with user preferences
- **Data pipeline configs:** Combining base parameters with experiment-specific settings
- **Feature engineering:** Merging multiple feature dictionaries
- **API response handling:** Combining data from multiple sources

---

## Key Takeaways - Day 5

1. **Dictionaries use Hash Tables:** O(1) lookups make them ideal for fast data access and mapping.
2. **Safe Access with `.get()`:** Prevents KeyError exceptions when keys might not exist.
3. **Frequency Counting Pattern:** Essential for text analysis, categorical data, and histogram generation.
4. **Sets vs Lists:** Use sets for membership testing (O(1)), lists for ordered/indexed data (O(n)).
5. **Dictionary Merging:** `.update()` modifies in-place; `{**a, **b}` creates new dictionary.
6. **Iteration Methods:** `.items()` for key-value pairs, `.keys()` for keys, `.values()` for values.
7. **Hash Table Performance:** Dictionaries and sets trade memory for speed - worth it for large datasets.

---

## Common Dictionary Methods

```python
# Creating dictionaries
dict = {"key": "value"}
dict = dict(key="value")
dict = {k: v for k, v in pairs}  # Dict comprehension

# Accessing data
dict["key"]           # Direct access (raises KeyError if missing)
dict.get("key", default)  # Safe access with default
dict.keys()           # Get all keys
dict.values()         # Get all values
dict.items()          # Get (key, value) tuples

# Modifying dictionaries
dict["new_key"] = value     # Add/update
dict.update(other_dict)     # Merge
dict.pop("key")             # Remove and return value
dict.popitem()              # Remove and return last (key, value)
dict.clear()                # Remove all items

# Checking membership
"key" in dict         # Check if key exists
"key" not in dict     # Check if key doesn't exist
```
