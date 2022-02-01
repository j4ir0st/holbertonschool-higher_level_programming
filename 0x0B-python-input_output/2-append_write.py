#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """ Writes text at the end of the file """
    with open(filename, 'a', encoding='UTF8') as fo:
        buff = fo.write(text)
    fo.close()
    return (buff)
