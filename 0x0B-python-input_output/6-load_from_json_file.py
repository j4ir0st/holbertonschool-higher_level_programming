#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ Writes a function on JSON file """
    with open(filename, 'r', encoding='UTF8') as fo:
        return json.load(fo)
