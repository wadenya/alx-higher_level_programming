#!/usr/bin/python3
for letter in range(26):
    if letter % 2 == 0:
        print('{:c}'.format(122 - letter), end='')
    else:
        print('{:c}'.format(90 - letter), end='')
