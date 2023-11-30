#!/usr/bin/python3
""" module with function to find peak"""


def find_peak(nums_list):
    """finds a peak in a list of unsorted integers."""
    if nums_list:
        L = 0
        R = len(nums_list) - 1
        while L < R:
            m = (L + R) // 2
            if nums_list[m] > nums_list[m + 1]:
                R = m
            else:
                L = m + 1
        return nums_list[L]
