#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as args
    names = dir(args)
    for i in names:
        if i[0] != '_':
            print(i)
