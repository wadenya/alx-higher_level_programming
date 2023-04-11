#!/usr/bin/python3
"""
Adds new attribute to object
"""


def add_new_attr(obj, attr, value):
    """Attribute to add"""
    if hasattr(obj, '__setattr__'):
    setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
