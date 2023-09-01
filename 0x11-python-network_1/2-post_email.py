#!/usr/bin/python3
""" POST an email #0 """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    eml_val = sys.argv[2]
    data = urllib.parse.urlencode({'email': eml_val}).encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
