import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def logarithm(a, b):
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("a must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
