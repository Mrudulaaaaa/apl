# Sample answer for the factorial problem.
# This has been specifically written so as to pass each of the tests.

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial can only be computed for integers")
    elif n <= 0:
        raise ValueError("Factorial can only be computed on integers >= 1")
    else:
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
