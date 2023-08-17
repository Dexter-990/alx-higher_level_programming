#!/usr/bin/python3

def uniq_add(my_list=[]):
    def reduc(seq):
        sum_ = sum(seq)
        return sum_
    new_list = reduc(list(set(my_list)))
    return new_list
