#!/usr/bin/python3
"""Search API"""
import requests
import sys

if len(sys.argv) > 1:

    q = sys.argv[1]
else:
    q = ""

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

try:
    data = response.json()
    if 'id' in data and 'name' in data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
