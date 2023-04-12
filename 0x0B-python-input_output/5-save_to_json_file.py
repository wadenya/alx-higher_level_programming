#!/usr/bin/python3
"""
has JSON string
"""

import json

def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open("filename", mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
