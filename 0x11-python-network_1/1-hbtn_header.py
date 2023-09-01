#!/usr/bin/python3
#Response header value #0
import urllib.request
import sys

if len(sys.argv) > 1:
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
