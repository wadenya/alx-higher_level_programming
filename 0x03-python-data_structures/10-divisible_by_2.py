#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list."""
    new = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new[i] = 1
        else:
            new[i] = 0
    return (new)
