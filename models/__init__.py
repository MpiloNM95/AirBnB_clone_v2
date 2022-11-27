#!/usr/bin/python3
'''This file makes the models folder a python package'''

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
