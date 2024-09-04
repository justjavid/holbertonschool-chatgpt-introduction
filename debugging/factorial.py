#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n
    return result

if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("Number must be non-negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
    sys.exit(1)

f = factorial(number)
print(f)

