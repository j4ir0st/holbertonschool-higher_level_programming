#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dir(hidden_4)
    for p in dir(hidden_4):
        if(p[0:2] != "__"):
            print(p)
