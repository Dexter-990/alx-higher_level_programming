#!/usr/bin/python3
def uppercase(strg):
    for i in strg:
        i = ord(i)
        if islower(i):
            i -= 32
        else:
            i -= 0
        print("{}".format(chr(i)), end='')
    print("")
def islower(c):
    if c >= 97 and c <= 122:
        return True
    return False
