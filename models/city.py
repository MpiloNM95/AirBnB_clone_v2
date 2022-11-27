#!/usr/bin/python3
'''The City class that inherits from the BaseModel'''

from models.base_model import BaseModel

class City(BaseModel):
    '''This class takes care of all city related matters of the application'''
    state_id = ''
    name = ''
    count = 0
