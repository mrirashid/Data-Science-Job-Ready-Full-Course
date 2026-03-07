# Day 06: Jacobians, Hessians, and Curvature in Machine Learning

## Overview

This exercise focuses on multivariable calculus tools that are essential for understanding and optimizing machine learning models: the Jacobian matrix, the Hessian matrix, and curvature-based classification of critical points.

## Problems Covered

### Problem 1: Jacobian of a Vector-Valued Function

You worked with a vector-valued function of two variables using SymPy:

- Defined symbolic variables x1 and x2.
- Built three output functions:
  - y1 = x1^2 + sin(x2)
  - y2 = x1 \* x2
  - y3 = exp(x1) + 2x2
- Constructed the vector Y = [y1, y2, y3]^T and input vector X = [x1, x2]^T.
- Computed the symbolic Jacobian matrix J = dY/dX using SymPy.
- Evaluated the Jacobian at the point (x1 = 1, x2 = 0) and converted the result to a NumPy array for clean numerical output.

This shows how the Jacobian captures all first-order partial derivatives of a vector-valued function, which is useful for sensitivity analysis and backpropagation in neural networks.

### Problem 2: Hessian and Curvature Classification

You analyzed the curvature of scalar functions near critical points using the Hessian matrix:

- Implemented a function to classify critical points based on the eigenvalues of a 2x2 Hessian matrix.
- For a given Hessian H, you:
  - Computed its eigenvalues using NumPy.
  - Classified the point as:
    - Local Minimum if all eigenvalues are positive.
    - Local Maximum if all eigenvalues are negative.
    - Saddle Point if the eigenvalues have mixed signs.
    - Unknown otherwise.
- Applied this classification to three example Hessian matrices corresponding to points A, B, and C, and printed both the eigenvalues and the classification.

This illustrates how second-order information (the Hessian) helps determine the type of critical point, which is important for understanding optimization landscapes in machine learning.

## Key Concepts

- Jacobian matrix: Matrix of first-order partial derivatives for vector-valued functions.
- Hessian matrix: Matrix of second-order partial derivatives for scalar-valued functions.
- Eigenvalues of the Hessian: Determine local curvature and classify critical points.
- Curvature classification:
  - Positive definite Hessian: local minimum.
  - Negative definite Hessian: local maximum.
  - Indefinite Hessian: saddle point.

## Dependencies

- NumPy
- SymPy
