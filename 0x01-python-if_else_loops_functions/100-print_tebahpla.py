#!/usr/bin/python3
change = False
for i in range(122, 96, -1):
    if change:
        c = chr(i - 32)
    else:
        c = chr(i)
    print("{}".format(c), end="")
    change = not change
