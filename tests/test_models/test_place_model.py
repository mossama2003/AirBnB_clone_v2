#!/usr/bin/python3

import unittest
import os

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.place = Place()

    def tearDown(self):
        """Clean everything up after running setup"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_has_attributes(self):
        """Test that Place has class attributes city_id, user_id, name,
        description, number_rooms, number_bathrooms, max_guest, price_by_night,
        latitude, longitude, and amenity_ids, and they are all strings"""
        self.assertTrue("city_id" in self.place.__dict__)
        self.assertTrue("user_id" in self.place.__dict__)
        self.assertTrue("name" in self.place.__dict__)
        self.assertTrue("description" in self.place.__dict__)
        self.assertTrue("number_rooms" in self.place.__dict__)
        self.assertTrue("number_bathrooms" in self.place.__dict__)
        self.assertTrue("max_guest" in self.place.__dict__)
        self.assertTrue("price_by_night" in self.place.__dict__)
        self.assertTrue("latitude" in self.place.__dict__)
        self.assertTrue("longitude" in self.place.__dict__)
        self.assertTrue("amenity_ids" in self.place.__dict__)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        new_dict = self.place.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        for attr in self.place.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_str(self):
        """Test that the str method has the correct output"""
        string = "[Place] ({}) {}".format(
            self.place.id,
            self.place.__dict__,
        )
        self.assertEqual(string, str(self.place))

    def test_save(self):
        """Test that save updates the updated_at attribute"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)
