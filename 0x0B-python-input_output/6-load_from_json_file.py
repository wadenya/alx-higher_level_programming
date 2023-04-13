#!/usr/bin/python3
"""
function that creats an object from json
"""

import json


def load_from_json_file(filename):
    """create an object """
    with open(filename, 'r',encoding='utf-8') as f:
        return json.load(f)
