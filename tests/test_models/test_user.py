#!/usr/bin/python3
"""Tests user class"""
import unittest
from models.base_model import BaseModel
from models.user import User
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocs(unittest.TestCase):
    """Base model document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.base_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(User.__doc__) >= 1)


class Test_user(unittest.TestCase):
    """Tests the user class"""

    def __init__(self, *args, **kwargs):
        """ inicialization """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ tests the first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ tests the last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ tests email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ tests password """
        new = self.value()
        self.assertEqual(type(new.password), str)
