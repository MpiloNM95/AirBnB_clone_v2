#!/usr/bin/python3
"""test the Console itself"""
import unittest
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8
from unittest.mock import patch
from io import StringIO
import cmd
