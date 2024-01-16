#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.base = BaseModel()

    def tearDown(self):
        """Clean everything up after running setup"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_is_subclass(self):
        """Test that BaseModel is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.base.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that BaseModel has class attributes id, created_at,
        and updated_at, and they are all strings"""
        self.assertTrue("id" in self.base.__dict__)
        self.assertTrue("created_at" in self.base.__dict__)
        self.assertTrue("updated_at" in self.base.__dict__)
        self.assertEqual(type(self.base.id), str)
        self.assertEqual(type(self.base.created_at), str)
        self.assertEqual(type(self.base.updated_at), str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.base.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        for attr in self.base.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        string = "[BaseModel] ({}) {}".format(
            self.base.id,
            self.base.__dict__,
        )
        self.assertEqual(string, str(self.base))
