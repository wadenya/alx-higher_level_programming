#!/usr/bin/python3
"""Response header value #0"""
import urllib.request
import sys

if len(sys.argv) > 1:
    with urllib.request.urlopen(urllib.request.Request(sys.argv[1])) as response:
        print(dict(response.headers).get('X-Request-Id'))
