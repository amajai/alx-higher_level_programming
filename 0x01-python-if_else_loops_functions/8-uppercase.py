#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        if i + 1 == len(str):
            print("{}".format(c))
        else:
            print("{}".format(c), end="")
