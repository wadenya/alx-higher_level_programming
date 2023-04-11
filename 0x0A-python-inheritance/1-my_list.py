#!/usr/bin/python3
"""
MyList contains all contents of list
"""

class MyList(list):
    """subclasses are down here"""
    def __init__(self):
        """I can initialize an object"""
        super().__init__()

    def print_sorted(self):
        """I print list in a sorted assending order"""
        print(sorted(self))
