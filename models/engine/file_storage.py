#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj
