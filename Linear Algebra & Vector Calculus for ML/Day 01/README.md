# Day 01: Linear Algebra Fundamentals for Machine Learning

This notebook covers essential linear algebra concepts that form the foundation of machine learning algorithms.

## Problem 1: Linear Combinations

A linear combination is a sum of vectors, each multiplied by a scalar (weight).

Given vectors h1, h2, h3 representing house features (square footage, bedrooms, age) and weights w1, w2, w3, the linear combination is:

y = w1 _ h1 + w2 _ h2 + w3 \* h3

This concept is fundamental in ML because:

- Neural networks compute weighted sums of inputs
- Feature aggregation in ensemble methods uses linear combinations
- Regression models predict outputs as linear combinations of features

## Problem 2: Detecting Multi-collinearity

Multi-collinearity occurs when features in a dataset are linearly dependent, meaning one feature can be expressed as a linear combination of others.

The matrix rank tells us the number of linearly independent columns. If the rank is less than the number of columns, multi-collinearity exists.

In this problem:

- Temp(F) = Temp(C) \* 1.8 + 32
- A bias column of 1s is added to account for the constant term (32)
- The rank will be less than 4, indicating linear dependence

Why this matters in ML:

- Multi-collinearity causes numerical instability in linear regression
- It inflates variance of coefficient estimates
- Feature selection should remove redundant features

## Problem 3: Standard Basis Generation

The standard basis for R^n consists of n vectors, where each vector has a 1 in one position and 0s elsewhere.

For R^4, the standard basis is:

- e1 = [1, 0, 0, 0]
- e2 = [0, 1, 0, 0]
- e3 = [0, 0, 1, 0]
- e4 = [0, 0, 0, 1]

NumPy's np.eye(n) function generates the identity matrix, whose rows are the standard basis vectors.

Applications in ML:

- One-hot encoding of categorical variables
- Representing unit directions in feature space
- Building transformation matrices

## Key NumPy Functions Used

- np.array(): Create arrays from lists
- np.linalg.matrix_rank(): Compute the rank of a matrix
- np.eye(n): Generate an n x n identity matrix
