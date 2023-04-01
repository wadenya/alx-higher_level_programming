#!/usr/bin/python3
"""
This is 5-text_indentation module
It supplies one function, text_indentation(text).
"""

def text_indentation(text):
    """prints a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for e in text:
        if flag == 0:
            if e == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if e == '.' or e == '?' or e == ':':
                print(e)
                print()
                flag = 0
            else:
                print(e, end="")
