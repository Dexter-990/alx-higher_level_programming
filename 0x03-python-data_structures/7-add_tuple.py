#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a = tuple_a
    t_b = tuple_b
    # if both tuples are of lenght 0
    if len(t_a) == 0 and len(t_b) == 0:
        return (0, 0)

    # if both tuples are of lenght 1
    elif len(t_a) == 1 and len(t_b) == 1:
        return (t_a[0] + t_b[0], 0)

    # if tuple a is 1 and tuple b is 2
    elif len(t_a) == 1 and len(t_b) >= 2:
        sum_a = t_a[0] + t_b[0]
        sum_b = t_b[1]

    # if tuple a is 2 and tuple b is 1
    elif len(t_b) == 1 and len(t_a) >= 2:
        sum_a = t_a[0] + t_b[0]
        sum_b = t_a[1]

    # if both tuples are of lenght 2 or more
    elif len(t_a) >= 2 and len(t_b) >= 2:
        sum_a = t_a[0] + t_b[0]
        sum_b = t_a[1] + t_b[1]

    # if t_a is 2 and t_b is 0
    elif len(t_a) >= 2 and len(t_b) == 0:
        sum_a = t_a[0]
        sum_b = t_a[1]

    # if t_a is 2 and t_b is 0
    elif len(t_b) >= 2 and len(t_a) == 0:
        sum_a = t_b[0]
        sum_b = t_b[1]

    return (sum_a, sum_b)
