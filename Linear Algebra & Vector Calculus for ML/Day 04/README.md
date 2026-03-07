# Day 04: Singular Value Decomposition

## Overview

This exercise covers Singular Value Decomposition (SVD), one of the most important matrix factorization techniques in machine learning. SVD decomposes any matrix A into three matrices: U, Sigma, and V transpose.

## Problems Covered

### Problem 1: SVD Mechanics and Orthogonality

Demonstrates the fundamental properties of SVD:

1. Computed SVD using `np.linalg.svd(X, full_matrices=False)`
2. Reconstructed the original matrix from its decomposition: X = U @ diag(Sigma) @ Vt
3. Verified that U has orthonormal columns by checking U^T @ U equals the identity matrix

Key insight: SVD provides a perfect factorization that can always reconstruct the original matrix exactly.

### Problem 2: Low-Rank Approximation

Demonstrates how SVD enables data compression:

1. Computed full SVD of matrix A
2. Truncated U, Sigma, and Vt to keep only the top k=2 singular values and corresponding vectors
3. Computed the rank-k approximation: A_k = U_k @ Sigma_k @ Vt_k
4. Measured information loss using the Frobenius norm of (A - A_k)

Key insight: The Eckart-Young theorem guarantees this is the best possible rank-k approximation in terms of minimizing the Frobenius norm error.

### Problem 3: Proving SVD is PCA

Demonstrates the connection between SVD and Principal Component Analysis:

1. Mean-centered the data by subtracting column means
2. Computed SVD of the centered data to get right singular vectors (Vt)
3. Computed the covariance matrix and its eigenvectors
4. Showed that SVD right-singular vectors match PCA eigenvectors when sorted by descending eigenvalues

Key insight: For mean-centered data, performing SVD is mathematically equivalent to performing PCA. The right singular vectors (rows of Vt) are the principal components.

## Key Concepts

- SVD Decomposition: A = U @ Sigma @ Vt
- U contains left singular vectors (orthonormal columns)
- Sigma contains singular values on the diagonal (sorted in descending order)
- Vt contains right singular vectors (orthonormal rows)
- Low-rank approximation for dimensionality reduction and compression
- SVD as an efficient method to compute PCA

## Dependencies

- NumPy

## Usage

Run each cell in `exercise.ipynb` sequentially to see the results of each problem.
