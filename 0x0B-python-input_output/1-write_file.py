#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ Writes the given file """
    with open(filename, 'w', encoding='UTF8') as fo:
        buff = fo.write(text)
    fo.close()
    return (buff)
