# Python: Exceptions
In this project we are expected to know what are errors and exceptions, the difference between them, how to use, handle and the purpose of an exception.

## First things first: What do we need to know to do this projects?

### What’s the difference between errors and exceptions

| Aspect | Errors | Exceptions |
| :------------------- | :---------- | :---------- |
| Definition            | Problems that occur at runtime and prevent the program from continuing to execute.      | Unexpected or erroneous events that occur during the execution of a program.       |
| Causes             | Often caused by factors outside the control of the programmer, such as hardware failures, operating system issues, or lack of system resources      | Typically caused by factors within the program control, such as invalid user input, file I/O errors, or network communication problems.     |
| Examples               | Syntax errors, logic errors, runtime errors  (e.g., division by zero, out-of-memory errors).| Invalid user input, file I/O errors, network communication problems.       |
| Ocurrence             | Can occur during any stage of program execution.      | Typically occur during the execution of a program when certain conditions are met.    |
| Handling              | Generally handled by fixing the code to correct the underlying issue.      | Handled using try-except blocks to catch and handle specific types of exceptions.     |
| Impact on the program               | Often results in program crashes or termination.      | Can disrupt the normal flow of the program's instructions but can be gracefully recovered from using exception handling mechanisms.       |
| Examples on Python               | Syntax errors, runtime errors like division by zero, out-of-memory errors.      | ValueError, TypeError, FileNotFoundError, etc       |

### What are exceptions and how to use them
Exceptions are objects that represent exceptional conditions that have occurred during the execution of a program. They can be raised (or thrown) when an error occurs, and they can be caught (or handled) by code that anticipates and responds to those errors.
To use exceptions, you can use the `try`, `except`, `finally`, and `raise` keywords:
- `try`: This keyword is used to enclose the code block that might raise an exception.
- `except`: This keyword is used to catch and handle exceptions that occur within the corresponding try block.
- `finally`: This keyword is used to specify cleanup actions that should be performed regardless of whether an exception occurred.
- `raise`: This keyword is used to explicitly raise an exception.

### When do we need to use exceptions
We should use exceptions when we anticipate that certain conditions might cause our program to behave unexpectedly or terminate prematurely. By catching and handling exceptions, we can gracefully recover from errors, provide helpful error messages to users, and prevent our program from crashing.

### How to correctly handle an exception
To correctly handle an exception, we should enclose the code that might raise the exception within a `try` block, and use one or more `except` blocks to catch and handle specific types of exceptions. We can also use a `finally` block to ensure that cleanup actions are performed, such as closing files or releasing resources.
Here's an example of it:
```
try:
    # Attempt to convert user input to an integer
    num = int(input("Enter a number: "))
    
    # Print the square of the number
    print("Square of the number:", num ** 2)

except ValueError:
    # Handle the exception if user input cannot be converted to an integer
    print("Invalid input. Please enter a valid number.")

finally:
    # Perform cleanup actions
    print("Thank you for using the program!")
```
### What’s the purpose of catching exceptions
The purpose of catching exceptions is to gracefully handle errors and prevent them from causing our program to crash. By catching exceptions, we can provide feedback to users, log error messages for debugging purposes, and take appropriate actions to recover from errors and continue executing our program.

### How to raise a builtin exception
To raise a built-in exception, we can use the raise keyword followed by the name of the exception class. For example:
```
raise ValueError("Invalid input")
```

### When do we need to implement a clean-up action after an exception
We might need to implement a cleanup action after an exception occurs to ensure that resources are properly released and that our program remains in a consistent state. This is important for operations that involve file I/O, network communication, database transactions, or other resource-intensive tasks. We can use a `finally` block to guarantee that cleanup actions are performed regardless of whether an exception occurred.
