#!/usr/bin/python3

import unittest
import os

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def tearDown(self):
        """Clean everything up after running setup"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that State has class attributes name"""
        self.assertTrue("name" in self.state.__dict__)

    def test_has_string_attributes(self):
        """Test that State has attributes with string value"""
        self.assertEqual(type(self.state.name), str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.state.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in self.state.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        string = "[State] ({}) {}".format(
            self.state.id,
            self.state.__dict__,
        )
        self.assertEqual(string, str(self.state))


if __name__ == "__main__":
    unittest.main()
