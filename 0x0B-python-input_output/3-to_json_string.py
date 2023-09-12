#!/usr/bin/python3
import json
"""
This module has a function (to_json_string)
that returns the JSON

"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
