#!/usr/bin/python3
<<<<<<< HEAD
""" testing State """
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
=======
"""Test suite for the State class of the models.state module"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
