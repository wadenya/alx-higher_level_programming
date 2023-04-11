#!/usr/bin/python3
"""
MyList class contains list class
"""


class MyList(list):
    """subclass of list initializer"""
    def __init__(self):
        """initializes the object we have"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list in order"""
        print(sorted(self))
