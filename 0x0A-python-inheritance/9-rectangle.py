#!/usr/bin/python3
"""
Class Called BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This Class called Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """This is the Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This function is the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ This function return to a descripcion about this class"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
