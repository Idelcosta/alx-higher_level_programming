#!/usr/bin/python3
"""definition: square class"""


class Square:
    """Representation of a square
    Attributes:
        __size (int): side of the square
    """
    def __init__(self, size):
        """Initializes a square
        size (int): size of a side of the square
        Returns: None.
        """
        self.__size = size
