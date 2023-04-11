#!/usr/bin/python3
"""
class Rectangle that inherits BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle representation"""
    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string rep of rectangle instance"""
        return "[Rectangle] {%d}/{%d}".format(self.__width, self.__height)
