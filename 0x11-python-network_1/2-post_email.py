#!/usr/bin/python3
# POST an email #0
import urllib.request
import urllib.parse
import sys

if len(sys.argv) == 3:

    #Data to send
    data = urlib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    #Send POST request
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))
