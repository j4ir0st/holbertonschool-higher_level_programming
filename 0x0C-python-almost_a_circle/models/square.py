#!/usr/bin/python3
""" And now, the Square! """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return (self.width, self.height)

    @size.setter
    def size(self, v_size):
        if  not (isinstance(v_size, int)):
            raise TypeError('width must be an integer')
        if (v_size <= 0):
            raise ValueError('width must be > 0')
        self.width = v_size
        self.height = v_size
