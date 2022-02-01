#!/usr/bin/python3
""" Inheritanced function """


class MyList(list):
    """ Prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))
