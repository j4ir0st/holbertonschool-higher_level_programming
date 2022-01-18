#!/usr/bin/python3
p = 0
for i in range(122, 96, -1):
    p = i
    if (p % 2 != 0):
        p = p - 32
    print("{:c}".format(p), end='')
