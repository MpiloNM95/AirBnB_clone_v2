#!/usr/bin/python3
"""State test"""
import unittest
from models.base_model import BaseModel
from models.state import State
import pep8
import inspect


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestState(unittest.TestCase):
    """test State module"""
    def test_class(self):
        """test class"""
        self.assertEqual(State.name, "")
        self.assertTrue(State, BaseModel)

    def __init__(self, *args, **kwargs):
        """ Inicialization """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
