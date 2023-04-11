#!/usr/bin/python3
"""
Class that inverts
"""


class MyInt(int):
    """MyInt inherited"""
    def __eq__(self, other):
        """Override the default == operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Override the default != operator"""
        return int.__eq__(self, other)
