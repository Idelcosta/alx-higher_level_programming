#!/usr/bin/python3
"""
Definition of a square
"""

class Square:
    """ Defines a Square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size have to be an integer")
        if size < 0:
            raise ValueError("size have to be >= 0")
        self.__size = size

    def area(self):
        """ give area of square"""
        return (self.__size ** 2)
