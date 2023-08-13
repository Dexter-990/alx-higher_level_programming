#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)
    if arg == 1:
        print("0 arguments.")
    else:
        args = "argument"
        idx = 0
        x = 0
        if arg > 2:
            args = args + 's'
        print("{} {}:".format(len(argv) - 1, args))
        for i in range(len(argv) - 1):
            x += 1
            idx += 1
            print("{}: {}".format(idx, argv[x]))

