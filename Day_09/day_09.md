# Day 09: Python Generators and Yield
---
## Topics Covered

### 1. Introduction to Generators and `yield` Keyword

Learned about Python generators - special functions that return an iterator and allow lazy evaluation of data.

**Key Concepts:**
- Generators use `yield` instead of `return`
- They pause execution and save state between calls
- Memory efficient for large datasets

#### Basic Yield Example (`yield.py`)
```python
def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)
```

---

### 2. Yield vs Return - How Generators Work (`basic_yield.py`)

Explored the difference between `yield` and `return`:

| Feature | `return` | `yield` |
|---------|----------|---------|
| Execution | Terminates function | Pauses function |
| State | Lost after return | Preserved between yields |
| Memory | Stores all values | Generates values on-demand |
| Output | Single value | Multiple values (iterator) |

**How it works internally:**
- Save stack frame (state, line number)
- Yield value
- Restore stack frame when resumed

---

### 3. Infinite Sequences with Generators

#### Simple Infinite Loop (`infinite_sequence.py`)
```python
def infinite_loop():
    i = 0
    while True:
        yield i
        i = i + 1
```

#### Fibonacci Infinite Sequence (`infinite.py`)
```python
# f(n) = f(n-1) + f(n-2)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fibonacci():
    print(i)
```

**Key Learning:** Generators can produce infinite sequences without running out of memory because values are generated on-demand.

---

### 4. Memory Efficiency: List vs Generator (`memory.py`)

Compared memory usage between list comprehension and generator expression:

```python
import sys
number = 1000000

# List comprehension - stores all values in memory
list_comparison = [x for x in range(number)]
print(sys.getsizeof(list_comparison))  # ~8 MB

# Generator expression - generates values on-demand
generator = (x for x in range(number))
print(sys.getsizeof(generator))  # ~200 bytes
```

**Result:** Generators are significantly more memory-efficient, especially for large datasets!

---

### 5. Generator Internal Structure (`memory_profile.py`)

Explored the internal structure of a generator object:
- **code_object**: Contains the function bytecode
- **frame_object**: Saves the execution frame (state)

---

## Key Takeaways

1. **Generators are lazy** - They produce values only when requested
2. **Memory efficient** - Don't store all values in memory at once
3. **State preservation** - Generators remember where they left off
4. **Infinite sequences** - Can create sequences that never end
5. **Use cases** - Great for large files, data streams, and infinite sequences

---

## Files Created

| File | Description |
|------|-------------|
| `yield.py` | Basic generator with yield keyword |
| `basic_yield.py` | Understanding yield vs return |
| `infinite_sequence.py` | Simple infinite counter generator |
| `infinite.py` | Fibonacci sequence generator |
| `memory.py` | Memory comparison: list vs generator |
| `memory_profile.py` | Generator internal structure |

---

## Related Concepts
- Iterators
- Lazy Evaluation
- Memory Management
- List Comprehensions vs Generator Expressions
