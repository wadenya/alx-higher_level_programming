#!/usr/bin/python3
"""
has JSON string
"""

import json

def from_json_string(my_str):
    """returns an object rep by a JSON string"""
    return json.load(my_str)
