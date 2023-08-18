#!/usr/bin/python3
def best_score(a_dictionary):
    dich = a_dictionary
    if a_dictionary:
        so = sorted(dich.items(), key=lambda x: x[1])
        return so[-1][0]
    return None
