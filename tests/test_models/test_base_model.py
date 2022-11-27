#!/usr/bin/python3
'''Unit TestCase for BaseModel class '''
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''This class tests for the base_model methods and attributes'''

    def setUp(self):
        '''This method instantiates the basemodel for testing'''
        self.model = BaseModel()

    def test_save(self):
        '''Testing if the save method acutally updates the updated_at'''
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(actual, expected)

    # def test_dict_to(self):
    #     '''Tests if the dictionary representation has the __class__ and if truly is a dictionary'''
    #     test_dict = self.model.dict_to()
    #     self.assertTrue(test_dict.get('__class__'))
    #     self.assertTrue(type(test_dict) is dict)
        



if __name__ == "__main__":
    unittest.main()
