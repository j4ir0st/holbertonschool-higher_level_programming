#!/usr/bin/python3
""" Base class """
"""import json"""


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    """def to_json_string(list_dictionaries):
        if (list_dictionaries is None or list_dictionaries == ""):
            return ("[]")
        return (json.dumps(list_dictionaries))"""