#!/usr/bin/python3
def no_c(my_string):
    str_list = [c for c in my_string if c not in "cC"]
    new_str = ''.join(str_list)
    return new_str
