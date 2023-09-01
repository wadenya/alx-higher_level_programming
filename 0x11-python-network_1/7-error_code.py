#!/usr/bin/python3
"""Error code #1"""
import requests
import sys

if len(sys.argv) > 1:

    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
