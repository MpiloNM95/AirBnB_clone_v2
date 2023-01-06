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


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                              ForeignKey("places.id"),
                              primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                              ForeignKey("amenities.id"),
                              primary_key=True, nullable=False))

