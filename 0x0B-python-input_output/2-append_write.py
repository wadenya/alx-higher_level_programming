#!/usr/bin/python3
"""
function that appends a string at end of a text file(UTF8)
"""


def append_write(filename="", text=""):
    """append a string to text at end and returns number of characters added"""
    with open(filename, 'a', encoding='utf=8') as fil:
        return fil.write(text)
