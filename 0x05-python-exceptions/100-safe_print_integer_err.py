#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as er:
        print("{}".format(er), file=stderr)
    except TypeError as er:
        print("{}".format(er), file=stderr)
