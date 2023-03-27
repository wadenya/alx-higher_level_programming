def safe_print_list(my_list=[], x=0):
    n = 0
    for m in range(x):
        try:
            print(my_list[m], end = "\n")
            n += m
        except IndexError:
            break
    return n
    print()
