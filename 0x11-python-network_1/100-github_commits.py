#!/usr/bin/python3
"""Response header value #1"""
import requests
import sys

if len(sys.argv) == 3:
    reponm = sys.argv[1]
    ownernm = sys.argv[2]

    url = f"https://api.github.com/repos/{ownernm}/{reponm}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'), commit.get('commit').get('author').get('name')))
