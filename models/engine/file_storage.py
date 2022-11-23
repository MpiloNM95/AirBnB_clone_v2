#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
