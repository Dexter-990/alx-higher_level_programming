#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    arr = my_list[:]
    for i in range(len(my_list)):
        arr[i] = i % 2
    return arr
