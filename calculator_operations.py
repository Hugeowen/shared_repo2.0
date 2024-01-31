import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def absolute_value(a):
    return abs(a)

def quadratic(a):
    return a * a

def square_root(a):
    return math.sqrt(a)
