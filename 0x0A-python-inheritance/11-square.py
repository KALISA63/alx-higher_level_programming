#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is Square that inherits from Rectangle"""

    def __init__(self, size):
        """This is the instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Calculates the area of a square'''
        return self.__size * self.__size

    def __str__(self):
        """This Function Return A Description about the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
