#!/usr/bin/python3
'''The Review class that inherits from the BaseModel'''

from models.base_model import BaseModel

class Review(BaseModel):
    '''This class takes care of all application reviews'''
    place_id = ''
    user_id = ''
    text = ''
    count = 0
