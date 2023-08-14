#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
        return None
    for row in matrix:
        for column in range(3):
            print("{:d}".format(row[column]), end=" " if column != 2 else "")
        print()
