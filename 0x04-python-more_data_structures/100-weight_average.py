#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product = 0
    summ = 0
    for item in my_list:
        product = item[0] * item[1]
        summ += product
    res = [i[1] for i in my_list]
    res_added = sum(res)
    return summ / res_added
