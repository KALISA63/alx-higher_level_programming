#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    print(obj)
    if isinstance(obj, type):
        raise TypeError("[TypeError] can't add new attribute")
    print(id(obj))
    obj.attribute = value
