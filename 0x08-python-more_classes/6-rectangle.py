#!/usr/bin/python3
"""
Creating a Rectangle class
Rectangle: A class
Atributtes: width, height
"""


class Rectangle:
    """    Rectangle Class with width, height atributtes   """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        x = 0
        y = 0
        str1 = ""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        else:
            while x < self.__height:
                while y < self.__width:
                    str1 = str1 + '#'
                    y += 1
                if (x != self.__height - 1):
                    str1 = str1 + '\n'
                x += 1
                y = 0
        return (str1)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
