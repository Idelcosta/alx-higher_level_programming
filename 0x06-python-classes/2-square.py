#!/usr/bin/python3
""" definition of a square """


class Square:
    """ a private instance attribute size """
    def __init__(self, size=0):
        """
        size: size of square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size have to be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size have to be an integer')
