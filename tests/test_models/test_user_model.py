#!/usr/bin/python3

import unittest
import os

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that User has class attributes email, password, first_name, and
        last_name"""
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("password" in self.user.__dict__)
        self.assertTrue("first_name" in self.user.__dict__)
        self.assertTrue("last_name" in self.user.__dict__)

    def test_has_string_attributes(self):
        """Test that User has attributes with string value"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.user.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in self.user.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        string = "[User] ({}) {}".format(
            self.user.id,
            self.user.__dict__,
        )
        self.assertEqual(string, str(self.user))


if __name__ == "__main__":
    unittest.main()
