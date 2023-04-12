#!/usr/bin/python3
"""
 Function to save an object to a file in json format
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, 'w', encoding='utf-8') as f_obj:
        json.dump(my_obj, f_obj)
