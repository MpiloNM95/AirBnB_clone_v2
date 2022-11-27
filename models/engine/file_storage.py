#!/usr/bin/python3
from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage():
    '''Serializes instances to a JSON file and deserializes JSON file to instances'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''Saves in __objects dictionary, the object with key <obj class name>.id'''
        key = '{}.{}'.format(obj.__class__.__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes and saves __objects to the JSON file (path: __file_path)'''
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file_object:
            dump(my_dict, file_object)

    def reload(self):
        '''Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists'''
        class_types = {'Basemodel': BaseModel, 'User': User, 'Amenity': Amenity, 'Place': Place, 
                       'Review': Review, 'State': State, 'City': City}

        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file_object:
                my_dict = load(file_object)
                for key in my_dict.keys():
                    for Class, instance in class_types.items():
                        if my_dict[key]['__class__'] == Class:
                            FileStorage.__objects[key] = ((instance)(**my_dict[key]))
        except:
            return
