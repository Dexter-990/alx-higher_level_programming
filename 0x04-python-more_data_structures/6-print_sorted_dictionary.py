#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, val in dict(sorted(a_dictionary.items(), key=lambda x: x[0])).items():
        print("{}: {}".format(key, val))
