#!/usr/bin/python3
"""
contains class_to_json(obj)
"""


def class_to_json(obj):
    """eturns the dictionary description with simple data structure"""
    return obj.__dict__
