# https://github.com/darkdarcool/lab11-DR-BT
# Partner 1: Darren Reddy
# Partner 2: Bryan Tran

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if b <= 0 or b == 1:
        raise ValueError("Your base cannot be less than 0 or equal to 1")
    if a <= 0:
        raise ValueError("a must be positive")
    return math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("a must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
