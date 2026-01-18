# Day 13: Advanced File Handling in Python

## Overview

Day 13 focused on advanced file handling techniques in Python, covering various file operations, data serialization formats, and best practices for working with files efficiently and safely.

---

## Topics Covered

### 1. Safe File Handling with Context Managers

**File:** `safe_open.py`

Learned how to safely open and write to files using the `with` statement, which ensures proper resource cleanup even if errors occur.

```python
with open("try.txt", "w") as f:
    f.write("This file is written safely")
```

---

### 2. Custom Context Manager

**File:** `context_manager.py`

Implemented a custom context manager class to measure execution time using `__enter__` and `__exit__` magic methods.

```python
class T:
    def __enter__(s): s.t = time.time()
    def __exit__(s, *_): print(time.time() - s.t)
```

---

### 3. File Modes: Write, Append, and Exclusive Create

**File:** `append_write.py`

Explored different file opening modes:
- `w` - Write mode (overwrites existing content)
- `a` - Append mode (adds to existing content)
- `x` - Exclusive create mode (fails if file exists)

Also learned to handle `FileExistsError` when using exclusive create mode.

---

### 4. Binary File Operations

**File:** `binary.py`

Learned to read and write binary data using `rb` and `wb` modes:
- Writing binary data with byte literals (`b'...'`)
- Reading binary content from files

---

### 5. File Encoding

**File:** `encoding.py`

Practiced specifying file encoding (UTF-8) to properly handle special characters and Unicode content.

---

### 6. Buffering and Large File Handling

**File:** `buffering.py`

Explored efficient handling of large files:
- Writing 1,000,000 lines to a file
- Reading files line by line for memory-efficient processing

---

### 7. Path Manipulation with pathlib

**File:** `pathlib.py`

Used the `pathlib` module for cross-platform path manipulation:
- Creating `Path` objects
- Joining paths using the `/` operator

```python
from pathlib import Path
folder = Path("data")
file = "file.txt"
full_path = folder / file
```

---

### 8. CSV File Handling

**File:** `csv_parsing.py`

Learned to work with CSV files using the `csv` module:
- Writing CSV data with `csv.writer`
- Reading CSV data with `csv.DictReader` for dictionary-based access

---

### 9. JSON File Handling

**File:** `json.py`

Practiced JSON serialization using the `json` module:
- Writing Python dictionaries to JSON files with `json.dump()`
- Using `indent` parameter for pretty-printed output

---

### 10. Object Serialization with Pickle

**File:** `pickle.py`

Learned to serialize Python objects using the `pickle` module:
- Creating custom classes
- Saving object instances to binary files with `pickle.dump()`

```python
import pickle
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Rashidul", 23)
with open("user.pkl", "wb") as f:
    pickle.dump(user, f)
```

---

## Files Created

| File | Description |
|------|-------------|
| `safe_open.py` | Safe file writing with context manager |
| `context_manager.py` | Custom context manager for timing |
| `append_write.py` | Different file modes demonstration |
| `binary.py` | Binary file read/write operations |
| `encoding.py` | UTF-8 encoding for special characters |
| `buffering.py` | Large file handling with buffering |
| `pathlib.py` | Cross-platform path manipulation |
| `csv_parsing.py` | CSV file reading and writing |
| `json.py` | JSON serialization |
| `pickle.py` | Object serialization with pickle |

---

## Key Takeaways

- Always use context managers (`with` statement) for file operations to ensure proper resource cleanup
- Choose the appropriate file mode based on the operation needed
- Use UTF-8 encoding for consistent handling of text across platforms
- The `pathlib` module provides a modern, object-oriented approach to path handling
- Python provides built-in support for common data formats like CSV, JSON, and binary serialization
- The `pickle` module allows serialization of complex Python objects
