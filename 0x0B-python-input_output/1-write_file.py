#!/usr/bin/python3
"""
function that writes string to a text file(UTF8)
"""


def write_file(filename="", text=""):
    """write string to text and returns number of characters written"""
    with open(filename, 'w', encoding="utf-8") as fil:
        print(fil.write(text)
