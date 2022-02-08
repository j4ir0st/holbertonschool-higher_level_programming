#!/usr/bin/python3
""" And now, the Square! """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        str2 = "[Square]"
        str2 += " (" + str(self.id) + ") "
        str2 += str(self.x) + "/" + str(self.y) + " - "
        str2 += str(self.width)
        return str2

    def update(self, *args, **kwargs):
        l_ar = len(args)
        if not args or l_ar == 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value
        if (l_ar > 0):
            self.id = args[0]
        if (l_ar > 1):
            self.size = args[1]
        if (l_ar > 2):
            self.x = args[2]
        if (l_ar > 3):
            self.y = args[3]

    def to_dictionary(self):
        d = dict([('x', self.x), ('y', self.y), ('id', self.id)])
        d['size'] = self.width
        return (d)

    @property
    def size(self):
        return (self.width, self.height)

    @size.setter
    def size(self, v_size):
        if not (isinstance(v_size, int)):
            raise TypeError('width must be an integer')
        if (v_size <= 0):
            raise ValueError('width must be > 0')
        self.width = v_size
        self.height = v_size
