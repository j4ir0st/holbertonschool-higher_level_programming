#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To JSON function """
        if (list_dictionaries is None or list_dictionaries == ""):
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the given file """
        if (list_objs is None):
            with open(cls.__name__ + ".json", 'w', encoding='UTF8') as fo:
                fo.write(to_json_string("[]"))
        else:
            with open(cls.__name__ + ".json", 'w', encoding='UTF8') as fo:
                fo.write(
                    to_json_string([elem.to_dictionary()for elem in list_objs])
                )
