#!/usr/bin/python3
"""Response header value #1"""
import requests
import sys

if len(sys.argv) > 1:

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
