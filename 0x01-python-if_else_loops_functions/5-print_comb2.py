#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        break
    if i >= 0 and i <= 9:
        i = f"0{i}"
    print("{}".format(i), end=', ')
print("{}".format(i))
