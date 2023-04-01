#!/usr/bin/python3
"""
The 4-print_square module supplies one function that print_square(size).
"""

def print_square(size):
    """prints square with "#"'s that has length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        raise TypeError("size must be an integer")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
