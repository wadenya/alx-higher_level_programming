#!/usr/bin/python3
"""
function that reads a text file(UTF8)
"""


def read_file(filename=""):
    """Read text and print in stdout"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
