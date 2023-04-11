#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
"""

def is_same_class(obj, a_class):
    """return true if object is exactly class a_class, otherwise false"""
    return (type(obj) == a_class)
