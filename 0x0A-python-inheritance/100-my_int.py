#!/usr/bin/python3
""" Inheritance class """


class MyInt(int):
    """ Int Inheritanced class """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
