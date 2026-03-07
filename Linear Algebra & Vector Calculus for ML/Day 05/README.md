# Day 05: Gradients and Directional Derivatives

## Overview

This exercise introduces the concept of the gradient, a fundamental tool in multivariable calculus and optimization. The gradient is a vector that points in the direction of the steepest ascent of a function at a given point.

## Problems Covered

### Problem 1: Numerical Partial Derivatives

This problem demonstrates how to approximate partial derivatives of a multivariable function numerically using the finite difference method (specifically, the forward difference quotient).

- The partial derivative with respect to x is approximated as `(f(x+h, y) - f(x, y)) / h`
- The partial derivative with respect to y is approximated as `(f(x, y+h) - f(x, y)) / h`

Here, `h` is a very small step size. This method allows us to compute derivatives without needing to find the analytical solution.

### Problem 2: Constructing the Gradient Vector

The gradient of a multivariable function `f` (denoted as ∇f) is a vector containing all of its partial derivatives. For a function `f(x, y)`, the gradient is:

∇f = [∂f/∂x, ∂f/∂y]

This problem involves taking the numerically computed partial derivatives from Problem 1 and packing them into a NumPy array to form the gradient vector.

### Problem 3: The Directional Derivative

The directional derivative measures the rate of change of a function in a specific direction. It is calculated as the dot product of the gradient vector and a unit vector `u` representing the direction.

Directional Derivative (D_u f) = ∇f ⋅ u

This tells us how much the function `f` changes as we take a small step in the direction of `u`. The result from this problem shows the slope of the function in that specific direction.

## Key Concepts

- **Partial Derivative**: The rate of change of a multivariable function with respect to one variable, holding others constant.
- **Gradient**: A vector of all partial derivatives, pointing in the direction of the function's steepest ascent.
- **Directional Derivative**: The rate of change of a function in a non-axis-aligned direction.

## Dependencies

- NumPy

## Usage

Run each cell in `exercise.ipynb` sequentially to see the results of each problem.
