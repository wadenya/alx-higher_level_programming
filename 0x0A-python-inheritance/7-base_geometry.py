#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """public attribute area"""
    def area(self):
        """exception error raised"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value is integer ang greater than  0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
