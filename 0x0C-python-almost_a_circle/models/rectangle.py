#!/usr/bin/python3
""" First Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def area(self):
        return(self.__width * self.__height)

    def display(self):
        h = 0
        w = 0
        z = 0
        while (z < self.__y):
                print("")
                z += 1
        while h < self.__height:
            print(" " * self.__x, end="")
            while w < self.__width:
                print("#", end="")
                w += 1
            print("")
            h += 1
            w = 0

    def update(self, *args, **kwargs):
        l_ar = len(args)
        if not args or l_ar == 0:
            for key, value in kwargs.items():
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "id":
                    self.id = value
        if (l_ar > 0):
            self.id = args[0]
        if (l_ar > 1):
            self.__width = args[1]
        if (l_ar > 2):
            self.__height = args[2]
        if (l_ar > 3):
            self.__x = args[3]
        if (l_ar > 4):
            self.__y = args[4]

    def to_dictionary(self):
        return (dict([('x', self.x), ('y', self.y), ('id', self.id), ('heigth', self.height), ('width', self.width)]))

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, v_width):
        if  not (isinstance(v_width, int)):
            raise TypeError('width must be an integer')
        if (v_width <= 0):
            raise ValueError('width must be > 0')
        self.__width = v_width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, v_height):
        if  not (isinstance(v_height, int)):
            raise TypeError('height must be an integer')
        if (v_height <= 0):
            raise ValueError('height must be > 0')
        self.__height = v_height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, v_x):
        if  not (isinstance(v_x, int)):
            raise TypeError('x must be an integer')
        if (v_x < 0):
            raise ValueError('x must be >= 0')
        self.__x = v_x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, v_y):
        if  not (isinstance(v_y, int)):
            raise TypeError('y must be an integer')
        if (v_y < 0):
            raise ValueError('y must be >= 0')
        self.__y = v_y
