#!/usr/bin/python3
""" Defines the HBNB console """
import cmd
import shlex import split
import datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    AirBnB clone console
    contains the entry point of the comm interpreter
    quit and EOF to exit the program
    help dispays help
    an empty line + ENTER doesn't execute anything
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty spaces."""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
