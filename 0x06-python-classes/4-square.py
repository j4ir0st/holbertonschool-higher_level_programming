#!/usr/bin/python3
"""
Creating a Square class
Square: A class
Atributtes: Size
"""


class Square:
    """    Square Class with size atributte   """
    def __init__(self, size=0):
        self.size = size

    """    Square Class with size atributte   """
    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, s_size):
        if not isinstance(s_size, int):
            raise TypeError('size must be an integer')
        if (s_size < 0):
            raise ValueError('size must be >= 0')
        self.__size = s_size
