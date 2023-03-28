#!/usr/bin/python3
"""Define a class MagicClass"""
import math

class MagicClass:
    """This rep a circle"""
    def __int__(self, radius=0):
        """Initialize the Magic Class"""
        self.__radius = 0
        if type(radius) is not int type(radius) is mot float:
            raise TypeError('radius must be a number')
        self.__radius = radius

        def area(self):
            """Calculates circle area"""
            return (self.__radius ** 2) * math.pi

        def circumfreence(self):
            """Cicle circumfrance cal""
            return 2 * math.pi * self.radius
