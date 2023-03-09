#!/usr/bin/python3
from sys import argv
add = 0
for h in argv[1:]:
    add += int(h)
print("{:d}".format(add))
