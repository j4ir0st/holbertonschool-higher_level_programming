#!/usr/bin/python3
""" Create object from a JSON file """
import json


def class_to_json(obj):
    return (json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True))
