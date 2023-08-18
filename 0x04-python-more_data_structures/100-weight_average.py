#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denom = 0
        for t in my_list:
            numerator += t[0] * t[1]
            denom += t[1]
        return numerator / denom
    return 0
