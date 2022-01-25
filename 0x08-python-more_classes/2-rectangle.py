#!/usr/bin/python3
"""
Creating a Rectangle class
Rectangle: A class
Atributtes: width, height
"""


class Rectangle:
    """    Rectangle Class with width, height atributtes   """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

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