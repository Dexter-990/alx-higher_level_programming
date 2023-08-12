#!/usr/bin/python3
for i in range(0, 100):
    if i == 89:
        break
    if i >= 0 and i <= 9:
        i = f"0{i}"
    i = str(i)
    if int(i[0]) >= int(i[-1]):
        continue
    print("{}".format(i), end=', ')
print("{}".format(i))
