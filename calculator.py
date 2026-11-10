"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

import math

def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b): b / a # raise ZeroDivisionError if a == 0

def log(a, b): math.log(a, b)# use math library + raise ValueError

def exp(a, b): a**b

