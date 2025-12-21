# Day 07 - Error Handling and Exceptions

## Topics Covered

- Exception handling with try/except blocks
- Multiple exception types (ValueError, ZeroDivisionError)
- Using finally clause for cleanup code
- Raising custom exceptions with `raise`
- Input validation and error recovery
- While loops with exception handling for robust user input

## Exercises Completed

### 1. **error_handling_syntax.py**

Basic syntax for error handling with multiple exception types:

- Taking user input and converting to integer
- Handling ValueError for invalid text input
- Handling ZeroDivisionError when dividing by 100
- Using a while loop to keep asking until valid input is received

### 2. **cleanup_crew.py**

Dividing two numbers with proper exception handling:

- Try/except block for division operation
- Catching ValueError and ZeroDivisionError
- Using `finally` clause to ensure cleanup code always runs
- Demonstrating that finally executes regardless of exception occurrence

### 3. **custom_signal.py**

Raising custom exceptions for validation:

- Taking user input for a number
- Manually raising ValueError if the number is negative
- Using custom error messages with `raise ValueError("No negatives")`
- Catching and displaying the custom error message

### 4. **input_guard.py**

Robust age input validation:

- While loop for continuous input attempts
- Converting string input to integer
- Catching ValueError for non-numeric input
- Breaking out of loop only when valid input is received
- User-friendly error messages

### 5. **math_safety_net.py**

Preventing division by zero errors:

- Setting a variable to zero
- Attempting division operation (100/x)
- Catching ZeroDivisionError specifically
- Displaying appropriate error message instead of program crash

## Key Concepts Learned

- **Try/Except**: Catching and handling exceptions gracefully
- **Multiple Exception Handlers**: Handling different error types separately
- **Finally Clause**: Executing cleanup code regardless of exceptions
- **Raising Exceptions**: Creating custom error conditions with `raise`
- **Input Validation**: Using exceptions to validate user input
- **Error Recovery**: Implementing retry logic with while loops
- **Defensive Programming**: Anticipating and handling potential errors

## Practical Applications

- User input validation in real-world applications
- Preventing program crashes from unexpected input
- Providing meaningful error messages to users
- Ensuring resource cleanup with finally blocks
- Building robust and fault-tolerant programs
