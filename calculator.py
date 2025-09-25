def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Return division a / b. Raises ZeroDivisionError if b == 0"""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
