#!/usr/bin/python3

"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Overriding constructor from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Get the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ Check if is an integer if set value to size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes about this class"""
        attr = ["id", "size", "x", "y"]
        my_len = len(attr)
        if len(args) > 0:
            for i, argv in enumerate(args):
                if i < my_len:

                    self.__setattr__(attr[i], argv)
        else:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def to_dictionary(self):
        """Return a dictionary about the class"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
