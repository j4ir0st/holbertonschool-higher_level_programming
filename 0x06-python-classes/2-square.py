#!/usr/bin/python3
"""
Creating a Square class
Square: A class
Atributtes: Size
"""


class Square:
    """    Square Class with size atributte   """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
