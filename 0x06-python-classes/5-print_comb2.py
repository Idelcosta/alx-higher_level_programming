#!/usr/bin/python3
"""definition of a class Square"""


class Square:
    """ a square Attributes: __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args: size (int): size of a side of the square
        Returns: None.
        """
        self.size = size

    def area(self):
        """calculation of the area of a square
        Returns: area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """get of __size
        Returns: The size of the square
        """
        return self.__size

    @size.set
    def size(self, value):
        """setter of __size
        Args: value (int): size of a side of the square
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size have to be an integer")
        else:
            if value < 0:
                raise ValueError("size have to be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square
        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
