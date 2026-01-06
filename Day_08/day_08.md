# Day 08: Algorithm Complexity & Performance Optimization

## Topics Covered

### 1. Time Complexity Analysis

- **Linear Scan O(N)**: Searching through lists sequentially
- **Hash Lookup O(1)**: Constant-time lookups using sets and dictionaries
- **Quadratic Time O(N²)**: Nested loops and inefficient string operations

### 2. Common Performance Patterns

#### Linear Scan (`linear_scan.py`)

- Created a list of 10 million numbers
- Demonstrated O(N) time complexity when checking if a value exists in a list
- Checked if -5 exists in `numbers_list` using linear search

#### Hash Lookup (`hash_lookup.py`)

- Created both a list and set of 10 million numbers
- Demonstrated O(1) time complexity for set membership testing
- Checked if -5 exists in `numbers_set` using hash-based lookup
- **Key Learning**: Sets provide instant lookups compared to lists

#### Quadratic Nested Loop (`quadratic_nested_loop.py`)

- Demonstrated O(N²) complexity with nested loops
- Finding duplicates between two lists using brute force approach
- **Warning**: This approach is inefficient for large datasets

#### Queue Bottleneck (`queue_bottleneck.py`)

- Compared `list.pop()` vs `list.pop(0)` performance
- Introduced `collections.deque` for efficient queue operations
- Used `queue.popleft()` for O(1) removal from front
- **Key Learning**: Use deque instead of list for queue operations

#### String Builder (`string_builder.py`)

- Demonstrated O(N²) time complexity when concatenating strings in a loop
- Created a string by adding 10,000 'a' characters using `+=`
- **Key Learning**: String concatenation in loops is inefficient; use `join()` instead

#### Length Trick (`length_trick.py`)

- Attempted to get length of a large number (10 billion)
- **Note**: This demonstrates a common misconception - `len()` works on sequences, not integers

### 3. Exercises

#### Exercise 1 (`exercise1.py`)

**Task**: Check if a value exists in a list

- Implemented pseudo code logic using while loop
- Manual iteration through list indices
- Returns `True` if target found, `False` otherwise
- Demonstrates the underlying mechanism of linear search

#### Exercise 2 (`exercise2.py`)

**Task**: Understand hash lookup mechanics

- Implemented conceptual hash-based lookup for sets/dictionaries
- Steps involved:
  1. Calculate mathematical signature (hash)
  2. Calculate memory address using modulo
  3. Direct jump to memory slot
- Demonstrates why sets/dicts have O(1) lookup time

## Key Takeaways

1. **Choose the right data structure**:

   - Use sets/dicts for membership testing (O(1))
   - Use lists only when order matters and you don't need frequent lookups

2. **Avoid nested loops** when possible:

   - O(N²) complexity grows rapidly with input size
   - Consider using hash-based approaches instead

3. **String operations**:

   - Avoid string concatenation in loops
   - Use `list.append()` then `''.join()` for better performance

4. **Queue operations**:

   - Use `collections.deque` for efficient queue operations
   - `list.pop(0)` is O(N), while `deque.popleft()` is O(1)

5. **Understanding complexity** helps write scalable code:
   - O(1): Constant time
   - O(N): Linear time
   - O(N²): Quadratic time

## Files Created

- `hash_lookup.py` - Hash-based O(1) lookup demonstration
- `linear_scan.py` - Linear O(N) search demonstration
- `quadratic_nested_loop.py` - O(N²) nested loop example
- `queue_bottleneck.py` - Efficient queue operations with deque
- `string_builder.py` - String concatenation performance issue
- `length_trick.py` - Length function exploration
- `exercise1.py` - Linear search implementation
- `exercise2.py` - Hash lookup concept implementation
- `insertion_trap.py` - (Empty file)
