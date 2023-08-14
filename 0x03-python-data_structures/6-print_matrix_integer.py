#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 3:
        for row in matrix:
            for column in range(3):
                if column == 2:
                    print("{}".format(row[column]))
                else:
                    print("{}".format(row[column]), end=' ')
    else:
        print("")
