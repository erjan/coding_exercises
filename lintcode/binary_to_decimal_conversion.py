'''
Python's functools module provides a number of useful features, one of which is biased function that make function calls more easily by setting default values for the arguments.

The int() function can convert strings to integers, and when only strings are passed in, the int() function will convert them to decimal by default. However, the int() function also provides an additional base argument with default value 10. If the base arguments are passed in, the function will do base conversions.

In order to avoid redefining the base parameter every time we use the int() function for binary conversions,we need to use the functools module to help us create a partial function that fixes the base parameter for binary and decimal conversions we need you to write the code in solution.py that is required to compute the decimal conversion of a binary string n.

We will import your code from solution.py to main.py and run it. If your code is logically correct and runs successfully, the program will output the correct decimal conversion result for the variable n
'''


# write your code here
import functools

def func():
    # write your code here
    # define the partial function
    # return partial function
    return functools.partial(int, base=2)
