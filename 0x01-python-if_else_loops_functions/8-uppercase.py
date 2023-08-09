#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        print("{}".format(c), end="")
    print("")
    return 0
