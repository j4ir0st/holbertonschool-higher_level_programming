#!/usr/bin/python3
""" Read file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes the given file """
    with open(filename, 'w', encoding='UTF8') as fo:
        json.dump(my_obj, fo)
    fo.close()
