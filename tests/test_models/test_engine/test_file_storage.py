#!/usr/bin/python3
"""test the FileStorage method"""
import json
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
