#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new = []
    quo = 0
    while i < list_length:
        try:
            quo = my_list_1[i] / my_list_2[i]
            i += 1
        except TypeError:
            print("wrong type")
            quo = 0
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            quo = 0
            i += 1
        except IndexError:
            print("out of range")
            i += 1
            quo = 0
        finally:
            new.append(quo)
    return new
