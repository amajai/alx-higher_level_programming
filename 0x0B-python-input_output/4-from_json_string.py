#!/usr/bin/python3
"""
The module has function (from_json_string) return object
represented by JSON string
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
