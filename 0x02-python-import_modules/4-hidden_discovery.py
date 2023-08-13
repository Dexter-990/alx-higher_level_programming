#!/usr/bin/python3
import hidden_4 as args
names = dir(args)
for i in names:
    i = i.replace('__', '')
    print("{}".format(i))
