#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except ZeroDivisionError as zerr:
        print("Exception: {}".format(zerr), file=sys.stderr)
        result = None
    except IndexError as ierr:
        print("Exception: {}".format(ierr), file=sys.stderr)
        result = None
    except ValueError as verr:
        print("Exception: {}".format(verr), file=sys.stderr)
        result = None
    except TypeError as terr:
        print("Exception: {}".format(terr), file=sys.stderr)
        result = None
    return result
