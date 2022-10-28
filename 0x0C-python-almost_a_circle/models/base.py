#!/usr/bin/python3
"""Create A Class Called Base"""
import json
import csv


class Base:
    """ This class is called Base, it will be used in the future """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This function is the initializacion """
        if (id is None):
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns The Json String Representation of List_Dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) is list:
            for dictionaries in list_dictionaries:
                if type(dictionaries) is not dict:
                    return "[]"
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        list_dicts = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for my_class in list_objs:
                if isinstance(my_class, cls):
                    list_dicts.append(my_class.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        if cls.__name__ in ['Rectangle', 'Square']:
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, 'r') as f:
                read_data = f.read()
                list_dicti = cls.from_json_string(read_data)
                my_list = []
                for i_dict in list_dicti:
                    my_list.append(cls.create(**i_dict))
                return my_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Function that serializes and write a file in csv"""
        filename = cls.__name__ + ".csv"
        my_dict = []
        if cls.__name__ == 'Rectangle':
            my_attr = ["id", "width", "height", "x", "y"]
        if cls.__name__ == 'Square':
            my_attr = ["id", "size", "x", "y"]
        for my_objs in list_objs:
            my_dict.append(cls.to_dictionary(my_objs))

        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=my_attr)
            writer.writeheader()
            writer.writerows(my_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Funcion that deserializes and read a file csv """
        results = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as File:
                reader = csv.DictReader(File)
                for row in reader:
                    res = {key: int(val) for key, val in row.items()}
                    results.append(cls.create(**res))
        except FileNotFoundError:
            return []
        return results
