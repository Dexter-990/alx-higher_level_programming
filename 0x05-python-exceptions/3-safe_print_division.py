#!/usr/bin/python3
def safe_print_division(a, b):
    quo = 0
    ins = None
    try:
        quo = a / b
        ins = quo
    except ZeroDivisionError:
        ins = None
        quo = "None"
    finally:
        print("Inside result: {}".format(quo))
        return ins
