#!/usr/bin/python3
""" Define A Function That Read A Text File """


def read_file(filename=""):
    """ Function That Read a File A Print The Text """
    with open(filename, mode="r", encoding='utf-8') as theFilename:
        contents = theFilename.read()
        print(contents, end="")
