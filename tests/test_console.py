#!/usr/bin/python3
""" Unittest for the Console """

import pep8
import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv, pathconf
from console import HBNBCommand



