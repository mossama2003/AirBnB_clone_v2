#!/usr/bin/python3

import unittest
import os

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        self.r = Review()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_is_subclass(self):
        """Test that Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.r.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that Review has class attributes place_id, user_id, and text"""
        self.assertTrue("place_id" in self.r.__dict__)
        self.assertTrue("user_id" in self.r.__dict__)
        self.assertTrue("text" in self.r.__dict__)

    def test_has_string_attributes(self):
        """Test that Review has attributes with string value"""
        self.assertEqual(type(self.r.place_id), str)
        self.assertEqual(type(self.r.user_id), str)
        self.assertEqual(type(self.r.text), str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.r.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in self.r.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        string = "[Review] ({}) {}".format(
            self.r.id,
            self.r.__dict__,
        )
        self.assertEqual(string, str(self.r))


if __name__ == "__main__":
    unittest.main()
