#!/usr/bin/python3

import unittest
import os

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def tearDown(self):
        """Clean everything up after running setup"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that City has class attributes name and state_id, and they are
        all strings"""
        self.assertTrue("name" in self.city.__dict__)
        self.assertTrue("state_id" in self.city.__dict__)
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        for attr in self.city.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """Test that the str method has the correct output"""
        string = "[City] ({}) {}".format(
            self.city.id,
            self.city.__dict__,
        )
        self.assertEqual(string, str(self.city))
