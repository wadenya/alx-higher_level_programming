#!/usr/bin/python3
""" defines a square """

class Square:
    """ square with a private instance attribute size """
    def __init__(self, size=0):
        """Args:
            size: size of square"""
        if type(size) is int:
            if size > 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        def area(self):
            """Finds area of a square
            returns: square area"""
            return.__size = size ** 2
