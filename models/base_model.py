#!/usr/bin/python3
'''Defines a base model class for the AirBnB project.'''

from datetime import datetime
from uuid import uuid4
import models

class BaseModel():
    '''A blueprint model that defines all other methods /attributes for other classes'''

    def __init__(self, *args, **kwargs):
        '''Creating an instance of a new basemodel'''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    time = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, time)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Returns the string representation of the instantiated object'''
        return ('[{}] ({}) {}').format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute "updated_at" with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__ of the instance'''
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
