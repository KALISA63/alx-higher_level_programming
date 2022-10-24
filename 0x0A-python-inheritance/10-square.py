#!/usr/bin/python3
"""
Class Called BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is Square that inherits from Rectangle"""

    def __init__(self, size):
        """This is the instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
