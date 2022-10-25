#!/usr/bin/python3
""" Define A Function That Write in A Text File """


def write_file(filename="", text=""):
    """ Function That Write a File and Returns the number of
    iiaracter written """
    with open(filename, mode="w", encoding="utf-8") as theFilename:
        contents = theFilename.write(text)
    return contents
