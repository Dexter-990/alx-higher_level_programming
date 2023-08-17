#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def lam(x):
        return replace if x == search else x

    new_list = [lam(x) for x in my_list]
    return new_list
