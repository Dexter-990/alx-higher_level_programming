#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dich = a_dictionary
    res = [k for k, v in dich.items() if v == value]
    for i in res:
        del dich[i]
    return dich
