#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    arr = my_list
    legt = len(arr)
    i = 0
    while i < legt:
        j = 0
        while j < legt - i - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
            j += 1
        i += 1
    return arr[len(arr) - 1]
