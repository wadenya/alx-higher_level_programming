#!/usr/bin/python3
"""What's my status? #1"""
import requests

response =  requests.get('https://alx-intranet.hbtn.io/status')
body = response.text
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
