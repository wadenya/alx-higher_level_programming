#!/usr/bin/python3
"""
Functions inside functions
"""


def inherits_from(obj, a_class):
    """Returns True if the object isclass dir or indir from the spefic class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
