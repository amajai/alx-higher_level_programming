#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = my_list[::-1]
    for n in rev:
        print("{:d}".format(n))
