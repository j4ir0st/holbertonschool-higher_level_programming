#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Reads the file """
    with open(filename, 'r', encoding='UTF8') as fo:
        buff = fo.read()
    print(buff, end='')
    fo.close()
