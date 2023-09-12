#!/usr/bin/python3
"""
This module has function script that adds all arguments to a Python list, and
then save them to a file

"""
import sys, os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main(argv=[]):
    """script that adds all arguments to a Python list, and then save them to a file
    """
    filename = "add_item.json"
    obj = []
    if os.path.exists(filename):
        obj = load_from_json_file(filename)

    for item in argv:
        obj.append(item)

    save_to_json_file(obj, filename)


if __name__ == "__main__":
    main(sys.argv[1:])
