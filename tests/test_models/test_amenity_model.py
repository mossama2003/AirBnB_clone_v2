#!/usr/bin/python3

import unittest
import os

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean everything up after running setup"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that Amenity has class attributes name and state_id"""
        self.assertTrue("name" in self.amenity.__dict__)
        self.assertTrue("state_id" in self.amenity.__dict__)

    def test_has_string_attributes(self):
        """Test that Amenity has attributes with string value"""
        self.assertEqual(type(self.amenity.name), str)
        self.assertEqual(type(self.amenity.state_id), str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.amenity.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in self.amenity.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        string = "[Amenity] ({}) {}".format(
            self.amenity.id,
            self.amenity.__dict__,
        )
        self.assertEqual(string, str(self.amenity))


if __name__ == "__main__":
    unittest.main()
