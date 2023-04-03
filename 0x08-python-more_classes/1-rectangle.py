#!/usr/bin/python3
"""class rectangle that defines a rectangle"""
class Rectangle:
    """Attribute int with width and height of rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @poperty
    def width(self):
        """getter of rectangle width"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter of rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @poperty
    def height(self):
        """getter of rectangle height"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter of rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
