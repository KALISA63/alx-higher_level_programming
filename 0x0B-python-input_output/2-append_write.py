#!/usr/bin/python3
""" Define A Function That APppends a string at the end the a Text File """


def append_write(filename="", text=""):
    """ Function That appends a string at the end File and Returns the
    the number of characters added """
    with open(filename, mode="a", encoding='utf-8') as theFilename:
        contents = theFilename.write(text)
    return contents
