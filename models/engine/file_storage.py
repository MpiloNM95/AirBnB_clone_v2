#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        If a cls specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new = {}
        for key, values in self.__objects.items():
            new[key] = values.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        Only if the file exists, else do nothing, no exception
        """
        classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
                   'State': State, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for keys, values in objects.items():
                    temp = keys.split('.')
                    new = classes[temp[0]](**values)
                    self.new(new)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributesError, KeyError):
            pass

    def close(self):
        """Call the reload method"""
        self.reload()
