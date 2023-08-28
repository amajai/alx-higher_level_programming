#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as verr:
        print("Exception: {}".format(verr), file=sys.stderr)
        return False
    except TypeError as terr:
        print("Exception: {}".format(terr), file=sys.stderr)
        return False
