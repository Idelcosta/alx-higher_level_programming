#!/usr/bin/python3
"""Definition of a class Square"""


class Square:
    """__size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        size (int): size of a side of the square
        Returns: None.
        """
        self.size = size

    def area(self):
        """calculates the area of a square
        Returns: area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        Returns: The size of the square
        """
        return self.__size

    @size.set
    def size(self, value):
        """Args: value (int): the size of a size of the square
        Returns: None.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

