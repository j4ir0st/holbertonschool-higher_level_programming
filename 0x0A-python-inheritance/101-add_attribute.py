#!/usr/bin/python3
""" Inheritance class """


def add_attribute(obj, att, value):
    """ Adds a new attribute to an object if it’s possible """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
        return
    raise TypeError("can't add new attribute")
