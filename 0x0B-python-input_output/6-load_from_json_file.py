#!/usr/bin/python3
'''Module for the load_from_json_file method'''
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a 'JSONFile' """
    with open(filename, 'r') as f:
        return json.load(f)
