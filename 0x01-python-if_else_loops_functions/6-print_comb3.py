#!/usr/bin/python3
c = 0
d = 1
while (c < 10):
    while (d < 10):
        if (c == 8):
            print("{}{}".format(c, d))
        else:
            print("{}{}".format(c, d), end=", ")
        d += 1
    c += 1
    d = c + 1
