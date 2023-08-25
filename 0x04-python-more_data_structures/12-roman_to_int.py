#!/usr/bin/python3
dich = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman_string):
    result = 0
    num = 0
    res = isinstance(roman_string, str)
    if not res:
        return 0
    for i in roman_string[::-1]:
        value = dich[i]
        if value >= num:
            result += value
        else:
            result -= value
        num = value
    return result
