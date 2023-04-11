#!/usr/bin/python3
"""
class BaseGeometry
"""

class BaseGeometry:
    """public area attribute"""
    def area(self):
        """Exeption error raised"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Value is an int and less 0r == zero"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".formart(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".formart(name))
