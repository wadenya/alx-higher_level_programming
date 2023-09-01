#!/usr/bin/python3
""" Error code #0"""
import urllib.request
import urllib.error
import sys

if len(sys.argv) > 1:
    
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
