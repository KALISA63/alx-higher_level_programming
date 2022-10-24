#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.

        *Prototype: def is_kind_of_class(obj, a_class):
        *You are not allowed to import any module
"""


def is_kind_of_class(obj, a_class):
    """ This function return True if the object is a instance of, if the
        object is an instance of a class that inherited from"""
    return isinstance(obj, a_class)
