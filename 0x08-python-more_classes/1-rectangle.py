#!/usr/bin/python3
"""
Creating a Square class
Rectangle: A class
Atributtes: Size
"""


class Rectangle:
    """    Square Class with size atributte   """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, s_width):
        if not (isinstance(s_width, int)):
            raise TypeError('width must be an integer')
        if (s_width < 0):
            raise ValueError('width must be >= 0')
        self.__width = s_width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, s_height):
        if not (isinstance(s_height, int)):
            raise TypeError('height must be an integer')
        if (s_height < 0):
            raise ValueError('height must be >= 0')
        self.__height = s_height
