#!/usr/bin/python3
""" POST an email #1 """
import requests
import sys

if len(sys.argv) == 3:

    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
