#!/usr/bin/python3
"""test the FileStorage method"""
import json
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from os import path
