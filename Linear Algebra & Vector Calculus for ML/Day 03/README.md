# Day 03: Eigenvalues and Eigenvectors in Machine Learning

## Overview

This exercise explores practical applications of eigenvalues and eigenvectors, which are fundamental concepts in linear algebra used extensively in machine learning algorithms.

## Problems Covered

### Problem 1: Accelerating Matrix Powers

Demonstrates two methods to compute the k-th power of a matrix:

- Direct power: Using `np.linalg.matrix_power(A, k)`
- Eigendecomposition: Decomposing A into Q, Lambda, and Q inverse, then computing A^k = Q _ Lambda^k _ Q^-1

The eigendecomposition method is computationally efficient for large k because raising a diagonal matrix to a power only requires raising each diagonal element to that power.

### Problem 2: The Core of PCA (1D Projection)

Implements the fundamental steps of Principal Component Analysis:

1. Compute the covariance matrix of the dataset using `np.cov(X, rowvar=False)`
2. Find eigenvalues and eigenvectors of the covariance matrix
3. Identify the principal eigenvector (the one with the highest eigenvalue)
4. Project the data onto the principal eigenvector using the dot product

This reduces a 2D dataset of 100 samples to 1D while preserving the direction of maximum variance.

### Problem 3: The Symmetry Superpower

Demonstrates a key property of symmetric matrices: their eigenvectors are always orthogonal.

For a symmetric matrix S, the dot product of any two distinct eigenvectors equals zero, confirming orthogonality. This property is why symmetric matrices are preferred in many algorithms, as they guarantee a complete set of orthogonal eigenvectors.

## Key Concepts

- Eigendecomposition: A = Q _ Lambda _ Q^-1
- Covariance matrix: Measures how features vary together
- Principal Component Analysis: Dimensionality reduction using eigenvectors
- Orthogonality: Eigenvectors of symmetric matrices are perpendicular

## Dependencies

- NumPy
