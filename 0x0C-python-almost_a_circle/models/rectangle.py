#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base:"""
from models.base import Base


class Rectangle(Base):
    """ Class About Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Check if is an integer if set value to width """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """ Get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Check if is an integer if set value to height """
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """ Get the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Check if is an integer if set value to x """
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """ Get the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Check if is an integer if set value to y """
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    @staticmethod
    def integer_validator(name, value):
        """ Check if Value is a positive Number """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'height' or name == 'width'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'y' or name == 'x'):
            raise ValueError('{} must be >= 0'.format(name))

    def display(self):
        """"Print the rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Print the descriptcion about this rectangle"""
        string = ("[Rectangle] ({}) {}/{} - {}/{}"
                  .format(self.id, self.__x, self.__y, self.__width,
                          self.__height))
        return string

    def update(self, *args, **kwargs):
        """update the attributes about this class"""
        attr = ["id", "width", "height", "x", "y"]
        my_len = len(attr)
        if len(args) > 0:
            for i, argv in enumerate(args):
                if i < my_len:

                    self.__setattr__(attr[i], argv)
        else:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def to_dictionary(self):
        """ Return To Diccionary About The Class """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
