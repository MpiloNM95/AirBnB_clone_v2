#!/usr/bin/python3
"""
Base Model for AirBnB
"""
from datetime import datetime
import json
from uuid import uuid4
import models


class BaseModel:
     """Class that defines all common attr/methods for other classes"""

     def __init__(self, *args, **kwargs):
         """Initialization of Class"""
