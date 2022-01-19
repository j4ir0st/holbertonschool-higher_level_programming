#!/usr/bin/python3
"""
Creating a Square class
Square: A class
Atributtes: Size
"""


class Square:
    """    Square Class with size atributte   """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """    Square Class with size atributte   """
    def area(self):
        return (self.__size ** 2)

    """    Square Class with size atributte   """
    def my_print(self):
        x = 0
        y = 0
        z = 0
        if (self.__size == 0):
            print("")
        else:
            while (z < self.__position[1]):
                print("")
                z += 1
            while (x < self.__size):
                print(" " * self.__position[0], end="")
                while y < self.__size:
                    print("#", end="")
                    y += 1
                print("")
                x += 1
                y = 0

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, s_pos):
        if not isinstance(s_pos, tuple) or len(s_pos) != 2 \
           or not isinstance(s_pos[0], int) \
           or not isinstance(s_pos[1], int) \
           or s_pos[0] < 0 or s_pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = s_pos
