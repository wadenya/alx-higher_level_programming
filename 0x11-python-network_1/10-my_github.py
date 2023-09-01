#!/usr/bin/python3
"""Response header value #1"""
import requests
import sys

if len(sys.argv) > 2:

    usnme = sys.argv[1]
    tok = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(usnme, tok))
    try:
        print(response.json()['id'])
    except KeyError:
        print("None")
