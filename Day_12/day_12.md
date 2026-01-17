# Day 12: Object-Oriented Programming in Python

## Overview

Day 12 focused on exploring the fundamental concepts of Object-Oriented Programming (OOP) in Python. This session covered essential topics including class construction, variable scoping, inheritance, special methods, and property decorators.

---

## Topics Covered

### 1. Constructor and Object Initialization

**File:** `constructor.py`

Learned how to use the `__init__` method to initialize objects with specific attributes. The constructor is automatically called when a new instance of a class is created.

- Creating a `User` class with `username` and `is_active` attributes
- Understanding how the constructor sets initial values for object attributes

---

### 2. The Self Reference

**File:** `self_reference.py`

Explored why `self` is used in Python OOP. The `self` parameter refers to the current instance of the class and allows access to instance attributes and methods.

- Demonstrated how `self` enables methods to modify instance attributes
- Created a `Car` class that uses `self.speed` to track the car's speed

---

### 3. Class Variables vs Instance Variables

**File:** `class_variable.py`

Understood the difference between class variables (shared across all instances) and instance variables (unique to each instance).

- Class variable `species` is shared by all `Person` instances
- Instance variables like `name` are unique to each object
- Modifying a class variable affects all instances

---

### 4. Private Variables and Name Mangling

**File:** `private_variable.py`

Learned about private variables in Python using the double underscore prefix (`__`). Python uses name mangling to make these variables harder to access from outside the class.

- Created a `User` class with a private `__password` attribute
- Demonstrated how to access private variables using name mangling (`_ClassName__variable`)

---

### 5. Property Decorator

**File:** `property.py`

Explored the `@property` decorator which allows methods to be accessed like attributes. This is useful for computed properties.

- Created a `User` class with a computed `age` property
- The `age` property calculates the user's age based on their birth year

---

### 6. String Representation Methods

**File:** `string_representation.py`

Learned the difference between `__str__` and `__repr__` magic methods:

- `__str__`: Returns a human-readable string representation (used by `print()`)
- `__repr__`: Returns an unambiguous representation useful for debugging (used in lists and containers)

---

### 7. Inheritance

**File:** `inheritance.py`

Studied how to create child classes that inherit from parent classes. Child classes can override parent methods to provide specialized behavior.

- Created a `User` base class with a `role()` method
- Created an `Admin` class that inherits from `User` and overrides the `role()` method

---

### 8. Super and Proxy

**File:** `super_proxy.py`

Learned how to use the `super()` function to call methods from the parent class. This is essential when extending parent class functionality in child classes.

- Used `super().__init__()` to initialize parent class attributes
- Extended the `Admin` class with additional attributes while preserving parent initialization

---

### 9. Object Equality

**File:** `Equality.py`

Explored how to implement custom equality comparison between objects using the `__eq__` magic method.

- Implemented `__eq__` in the `User` class to compare users by their `id`
- Used `isinstance()` to ensure type safety in comparisons
- Returned `NotImplemented` for unsupported comparison types

---

### 10. Operator Overloading

**File:** `operator.py`

Learned how to overload operators to define custom behavior for built-in operations. This allows objects to work with operators like `+`, `-`, etc.

- Created a `Vector` class with `__add__` method to support vector addition
- Combined `__str__` for readable output of vector objects
- Demonstrated adding two vector objects using the `+` operator

---

## Summary

Day 12 provided a comprehensive introduction to Object-Oriented Programming in Python, covering:

| Concept | Key Takeaway |
|---------|--------------|
| Constructor | Initialize objects with `__init__` |
| Self Reference | Access instance attributes using `self` |
| Class vs Instance Variables | Shared vs unique attributes |
| Private Variables | Use `__` prefix for encapsulation |
| Property Decorator | Create computed attributes with `@property` |
| String Representation | `__str__` for users, `__repr__` for debugging |
| Inheritance | Extend and override parent class behavior |
| Super Function | Call parent class methods with `super()` |
| Object Equality | Custom comparison with `__eq__` |
| Operator Overloading | Define custom operator behavior |

---

## Files Created

| File Name | Description |
|-----------|-------------|
| `constructor.py` | Object initialization with constructors |
| `self_reference.py` | Understanding the self parameter |
| `class_variable.py` | Class vs instance variables |
| `private_variable.py` | Private variables and name mangling |
| `property.py` | Property decorator usage |
| `string_representation.py` | `__str__` and `__repr__` methods |
| `inheritance.py` | Basic inheritance implementation |
| `super_proxy.py` | Using super() for parent class access |
| `Equality.py` | Object equality comparison |
| `operator.py` | Operator overloading with `__add__` |
