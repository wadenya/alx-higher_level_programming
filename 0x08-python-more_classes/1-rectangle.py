#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Rectangle information: width, height"""
    def __init__(self, width=0, height=0):

        self.height = height
        self.width = width

    @property
    def width(self):
        """private instance attribute width (getter)"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance attribute width (setter)"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height (getter)"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance attribute height (setter)"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
