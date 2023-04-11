#!/usr/bin/python3
"""
class square inherits Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square rep"""
    def __init__(self, size):
        """init a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area"""
        return self.__size ** 2

    def __str__(self):
        """prints square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
