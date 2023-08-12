#!/usr/bin/python3
step = 33
i = 122
while i >= 65 and i <= 122:
    print("{}".format(chr(i)), end='')
    if i >= 65 and i <= 90:
        i = i + 31
    elif i >= 97 and i <= 122:
        i = i - 33
    if i == 96:
        break
