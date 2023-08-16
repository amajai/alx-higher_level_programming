#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list:
        return list(map(lambda n: n*number, my_list))
    return my_list
