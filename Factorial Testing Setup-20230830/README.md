# Unit testing

Unit tests are a way of testing the behaviour of a function systematically.  Ideally you write down a set of *unit* tests - simple tests - before you even start writing your function.  Then as you write the function, you make sure that each test passes.

This is partly art, partly science.  There is no guaranteed way to know that you have got all the tests you need to be sure that your function is correct, and in some cases you may end up writing unnecessary tests.  Experience is generally the best way to get good at writing tests.

## Factorial

For testing a factorial function, we can think of the following tests:

- If the input is *not* an integer, this should raise an Exception - it would make sense to raise a `TypeError`.
- If the input is an integer but < 1, then this would indicate a `ValueError`.
- Otherwise the computed factorial can be checked against the known value for some test cases.

Note that this is not actually complete.  We should also check for large numbers or overflow, but in Python at least overflow is not easy to trigger due to the automatic handling of large integers.

# Purpose of testing

An important note: the purpose of testing is **NOT** to look into performance issues.  How fast the code runs is not important - we are only looking at functional correctness.  On the other hand, a highly efficient piece of code that is sometimes wrong may end up failing functional tests.

# How to test

Here we will use the `pytest` module.  There is another module called `unittest` that is a built-in module in Python.  However, `pytest` offers some easier syntax and is generally easier to use, so we will go with that for the purpose of this course.

