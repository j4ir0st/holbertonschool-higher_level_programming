#!/usr/bin/python3
""" First Rectangle """


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, v_width):
        self.__width = v_width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, v_height):
        self.__height = v_height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, v_x):
        self.__x = v_x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, v_y):
        self.__y = v_y
