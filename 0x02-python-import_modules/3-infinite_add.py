#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summ = 0
    num = 0
    for i in range(1, len(argv)):
        num = int(argv[i])
        summ += num
    print("{}".format(summ))
