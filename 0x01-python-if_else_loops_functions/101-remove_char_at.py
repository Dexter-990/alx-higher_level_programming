#!/usr/bin/python3
def remove_char_at(strn, n):
    if n >= len(strn) or n < 0:
        new = strn
    else:
        new = strn[:n] + strn[n+1:]
    return new
