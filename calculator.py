import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return b / a

def logarithim(a, b):
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("a must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
