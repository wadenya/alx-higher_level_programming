#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nt = 0
    for i in range(x):
        print("{:d}".format([i]), end="\n")
        nt += 1
        except(ValueError, TypeError):
            continue
        print()
        return nt
