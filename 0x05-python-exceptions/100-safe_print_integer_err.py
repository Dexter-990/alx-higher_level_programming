#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as er:
        print("Exception: {}".format(er), file=stderr)
        return False
    except TypeError as te:
        print("Exception: {}".format(te), file=stderr)
        return False
