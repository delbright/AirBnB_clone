#!/usr/bin/python3
<<<<<<< HEAD
""" testing Amenity """
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
=======
"""Test suite for Amenity class of the models.amenity module"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
