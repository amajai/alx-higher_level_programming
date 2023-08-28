#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        my_list[x-1]
        for i in range(x):
            print(f"{my_list[i]}", end="")
            c += 1
        print()
        return c
    except IndexError:
        for e in my_list:
            print(f"{e}", end="")
            c += 1
        print()
        return c
