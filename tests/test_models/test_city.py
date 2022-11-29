#!/usr/bin/python3
<<<<<<< HEAD
""" testing city """
import unittest
import pep8
from models.city import City

class City_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
=======
"""Test suite for the City class of the models.city module"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertFalse(bool(getattr(self.city, attr)))
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
