#!/usr/bin/python3
""" module with function to find peak"""


def find_peak(nums_list):
    """finds a peak in a list of unsorted integers."""
    if nums_list:
        l = 0
        r = len(nums_list) - 1
        while l < r:
            m = (l + r) // 2
            if nums_list[m] > nums_list[m + 1]:
                r = m
            else:
                l = m + 1
        return nums_list[l]
