#!/usr/bin/python3
""" Read file """
from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


try:
    list1 = load("add_item.json")
except:
    list1 = []

for i in argv[1:]:
    list1.append(i)

save(list1, "add_item.json")
