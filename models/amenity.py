#!/usr/bin/python3
'''The Amenity class that inherits from the BaseModel'''

from models.base_model import BaseModel

class Amenity(BaseModel):
    '''This class takes care of all application amenities'''
    name = ''
    count = 0
