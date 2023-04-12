#!/usr/bin/python3
"""
inserts a line to the next line
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line 
    containing a specific string """
    with open(filename, 'r', encoding='utf-8') as f:
        lines_list = []
        while True:
            lines = f.readlines()
            if line == "":
                break
            lines_list.append(line)
            if search_string in line:
                lines_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_string)
