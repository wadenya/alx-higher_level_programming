#!/usr/bin/python3
"""
has JSON string
"""

import json

def to_json_string(my_obj):
    """returns JSON representation of an object"""
    return json.dump(my_obj)
