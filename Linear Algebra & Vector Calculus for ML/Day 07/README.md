# Day 07: Building a Micro Autograd System

## Overview

This exercise implements a minimal automatic differentiation engine from scratch and uses it to build a single neuron. The goal is to understand how gradients flow through a computation graph, which is the core idea behind deep learning frameworks.

## Problems Covered

### Problem 1: The Value Class and Autograd

You implemented a `Value` class that represents a scalar value in a computation graph.

Key features:

- Stores both the numeric value (`data`) and its gradient (`grad`).
- Tracks the operation that produced it and its parent nodes (`_op`, `_prev`).
- Supports:
  - Addition via `__add__` with gradient propagation.
  - Multiplication via `__mul__` with gradient propagation.
  - A `relu()` method implementing the ReLU activation:
    - Forward: returns `max(0, x)`.
    - Backward: passes gradient only when the output is positive.
- Implements a `backward()` method that:
  - Builds a topological ordering of the computation graph.
  - Initializes the gradient of the final output to 1.0.
  - Walks the graph in reverse order and calls each node's `_backward` function to apply the chain rule.

This mirrors how larger autograd engines (such as those in deep learning libraries) work internally, but on a small and transparent scale.

### Problem 2: Building a Single Neuron

You then used the `Value` class to construct and analyze a simple neuron with two inputs.

Steps:

- Created input values:
  - `x1 = 2.0`
  - `x2 = -3.0`
- Defined learnable parameters (weights and bias):
  - `w1 = -1.0`
  - `w2 = 1.0`
  - `b = 6.0`
- Built the neuron computation:
  - Linear combination: `w1 * x1 + w2 * x2 + b`
  - Applied ReLU activation to this sum.
- Ran a forward pass to obtain the neuron output.
- Called `backward()` on the output to propagate gradients through the graph.
- Printed the gradients of `w1`, `w2`, `x1`, `x2`, and `b` to see how each value influences the output.

This demonstrates how a computation graph can be built from basic operations and how automatic differentiation computes gradients needed for optimization.

## Key Concepts

- Computation graph: nodes represent values, edges represent dependencies between operations.
- Automatic differentiation: systematic application of the chain rule over a computation graph.
- ReLU activation: introduces nonlinearity while keeping gradient computation simple.
- Parameter gradients: show how much a small change in each parameter affects the output.

## Dependencies

- Pure Python (no external libraries required for the core autograd implementation).
