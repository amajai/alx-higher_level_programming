#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]
        for n in my_list[1:]:
            if n > max_value:
                max_value = n
        return max_value
