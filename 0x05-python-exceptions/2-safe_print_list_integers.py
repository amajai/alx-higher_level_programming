#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    p = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                c += 1
            p += 1
        print()
        return c
    except ValueError:
        for i in range(p, x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                c += 1
        print()
        return c
