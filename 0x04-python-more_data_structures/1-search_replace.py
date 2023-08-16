#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = my_list[:]
        for i in range(len(new_list)):
            if new_list[i] == search:
                new_list[i] = replace
                break
        return new_list
    return my_list[:]
