#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in sorted(a_dictionary.items(), key=lambda e: e[0]):
        if v == value:
            del a_dictionary[k]
    return a_dictionary
