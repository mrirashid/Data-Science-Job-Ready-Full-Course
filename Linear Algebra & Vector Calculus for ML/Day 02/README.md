# Day 02 - Linear Algebra Operations with NumPy

This notebook covers fundamental linear algebra operations essential for machine learning using NumPy.

## Problem 1: Matrix Multiplication vs Hadamard Product

This exercise demonstrates the difference between standard matrix multiplication and element-wise multiplication.

### Concepts

- Standard Matrix Multiplication (AB and BA): Computed using `np.dot()` or the `@` operator. The result depends on the order of operands, meaning AB is not equal to BA in general.
- Element-wise (Hadamard) Product: Computed using the `*` operator. Each element is multiplied by the corresponding element in the other matrix.

### Code

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[0, 1],
              [-1, 0]])

AB = np.dot(A, B)  # Standard matrix multiplication
BA = np.dot(B, A)  # Order matters
element_wise = A * B  # Hadamard product
```

### Key Takeaway

Matrix multiplication is not commutative. This property is important when applying transformations in neural networks and other ML algorithms.

---

## Problem 2: Batch Geometric Transformations

This exercise applies a shear transformation to multiple 2D points using vectorized operations.

### Concepts

- Shear Matrix: A transformation matrix that shifts points parallel to an axis.
- Vectorized Operations: Applying transformations to all data points simultaneously without loops.

### Code

```python
data_points = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [1, 2],
    [1.5, 1.5]
])  # Shape: (5, 2)

shear_matrix = np.array([
    [1, 1.5],
    [0, 1]
])  # Shape: (2, 2)

transformed_points = (shear_matrix @ data_points.T).T
```

### Explanation

1. `data_points.T` transposes the data from shape (5, 2) to (2, 5)
2. `shear_matrix @ data_points.T` performs matrix multiplication: (2, 2) x (2, 5) = (2, 5)
3. The final `.T` transposes the result back to (5, 2)

### Key Takeaway

Vectorized matrix operations are more efficient than looping through individual points. This pattern is used extensively in ML for batch processing.

---

## Problem 3: Solving Linear Systems

This exercise solves a real-world pricing problem using a system of linear equations.

### Problem Statement

Given two cloud computing cost equations:

- 3 GPU hours + 2 CPU hours = 28 dollars
- 1 GPU hour + 4 CPU hours = 16 dollars

Find the hourly price of GPU and CPU.

### Concepts

- System of Linear Equations: Represented in matrix form as Ax = b
- NumPy Linear Algebra Solver: `np.linalg.solve()` finds the solution vector x

### Code

```python
coeffs = np.array([[3, 2],
                   [1, 4]])
b = np.array([28, 16])

prices = np.linalg.solve(coeffs, b)
```

### Solution

- GPU Price: 8.00 dollars per hour
- CPU Price: 2.00 dollars per hour

### Key Takeaway

Many ML problems involve solving systems of linear equations, including linear regression, optimization, and finding model parameters.

---

## Summary

This session covered three core linear algebra concepts:

1. Matrix multiplication and its non-commutative property
2. Geometric transformations using matrix operations
3. Solving linear systems with NumPy

These operations form the foundation for understanding how machine learning algorithms process data, apply transformations, and optimize parameters.
