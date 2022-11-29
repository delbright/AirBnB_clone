#!/usr/bin/python3
<<<<<<< HEAD
""" Check Filestorage class """
import unittest
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_storage(unittest.TestCase):
    """ check the class """

    def setUp(self):
        """ check empty """
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ check remove class """
        try:
            remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        """ check empty class  """
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """ check  all function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_save_create(self):
        """ Save  """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_new_empty(self):
        """ check new method """
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_classes(self):
        """ check  new method is valid """
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User(id='01')
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City(id='02')
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity(id='03')
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place(id='04')
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review(id='05')
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State(id='06')
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_reload(self):
        """ check reload classes """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id
        storage.save()

        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)
        self.assertTrue(obj1_key in storage.all().keys())
        self.assertEqual(obj1.id, storage.all()[obj1_key].id)
        self.assertTrue(obj2_key in storage.all().keys())
        self.assertEqual(obj2.id, storage.all()[obj2_key].id)
        self.assertTrue(obj3_key in storage.all().keys())
        self.assertEqual(obj3.id, storage.all()[obj3_key].id)
        self.assertTrue(obj4_key in storage.all().keys())
        self.assertEqual(obj4.id, storage.all()[obj4_key].id)
        self.assertTrue(obj5_key in storage.all().keys())
        self.assertEqual(obj5.id, storage.all()[obj5_key].id)
        self.assertTrue(obj6_key in storage.all().keys())
        self.assertEqual(obj6.id, storage.all()[obj6_key].id)
=======
"""Test Suite for FileStorage in models/file_storage.py"""
import os.path
import unittest

import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    @classmethod
    def setUp(self):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Code to execute after tests are executed"""
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Tests all() method of the FileStorage class"""
        self.assertTrue(type(models.storage.all()) is dict)

        # What if arg is passed? Ohh! TypeError, do your job!
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """Tests the new() method of the FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + dummy_bm.id,
                      models.storage.all().keys())
        self.assertIn(dummy_bm, models.storage.all().values())
        self.assertIn("User." + dummy_user.id, models.storage.all().keys())
        self.assertIn(dummy_user, models.storage.all().values())
        self.assertIn("State." + dummy_state.id, models.storage.all().keys())
        self.assertIn(dummy_state, models.storage.all().values())
        self.assertIn("Place." + dummy_place.id, models.storage.all().keys())
        self.assertIn(dummy_place, models.storage.all().values())
        self.assertIn("City." + dummy_city.id, models.storage.all().keys())
        self.assertIn(dummy_city, models.storage.all().values())
        self.assertIn("Amenity." + dummy_amenity.id,
                      models.storage.all().keys())
        self.assertIn(dummy_amenity, models.storage.all().values())
        self.assertIn("Review." + dummy_review.id,
                      models.storage.all().keys())
        self.assertIn(dummy_review, models.storage.all().values())

        # What if more than one arg were passed to this guy?
        # TypeError, we need you here!
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

        # What if None was passed? That guy needs learn a lesson...
        # AttributeError, will you join us?
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_method(self):
        """Time to deal with reload() method in FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            self.assertIn("User." + dummy_user.id, save_text)
            self.assertIn("State." + dummy_state.id, save_text)
            self.assertIn("Place." + dummy_place.id, save_text)
            self.assertIn("City." + dummy_city.id, save_text)
            self.assertIn("Amenity." + dummy_amenity.id, save_text)
            self.assertIn("Review." + dummy_review.id, save_text)

        # What happens when an arg is passed? TypeError has been my agent!
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """Tests the reload method... Quite tricky!"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn("User." + dummy_user.id, objects)
        self.assertIn("State." + dummy_state.id, objects)
        self.assertIn("Place." + dummy_place.id, objects)
        self.assertIn("City." + dummy_city.id, objects)
        self.assertIn("Amenity." + dummy_amenity.id, objects)
        self.assertIn("Review." + dummy_review.id, objects)

        # What happens when an arg is passed? TypeError is raised
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
