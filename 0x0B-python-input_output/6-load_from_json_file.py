#!/usr/bin/python3
"""
This module has function (load_from_json_file) that creates an Object from
a JSON file

"""
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
