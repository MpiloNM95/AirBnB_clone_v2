#!/usr/bin/python3
"""Defines the Place class."""
import models
from os import getenv
from models.base_models import Base
from models.base_models import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship
