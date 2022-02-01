#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ check if the object is an instance of a class """
    if type(obj) != a_class:
        return (isinstance(obj, a_class))
    return (False)
