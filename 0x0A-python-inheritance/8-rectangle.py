#!/usr/bin/python3
"""
Class Called BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This Class called Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This is the Instantiation of a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
