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
        except Exception:
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

    def test_to_dict_values(self):
        """Test that values in to_dict are the same as in __dict__"""
        new_dict = self.place.to_dict()
        for key, value in new_dict.items():
            self.assertEqual(value, self.place.__dict__[key])

    def test_init(self):
        """Test that the init method creates an instance of Place"""
        self.assertTrue(isinstance(self.place, Place))

    def test_init_arg(self):
        """Test that the init method takes one argument"""
        with self.assertRaises(TypeError):
            bad = Place(None)

    def test_init_kwarg(self):
        """Test that the init method takes one keyword argument"""
        with self.assertRaises(TypeError):
            bad = Place(x=None)

    def test_str_method(self):
        """Test that the str method produces a string"""
        self.assertTrue(type(str(self.place)) is str)

    def test_before_todict(self):
        """Test instances before using to_dict conversion"""
        self.assertTrue(hasattr(self.place, "__init__"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "id"))

    def test_after_todict(self):
        """Test instances after using to_dict conversion"""
        my_model = self.place.to_dict()
        self.assertIsInstance(my_model, dict)
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(hasattr(my_model, "__dict__"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))

    def test_class_attributes(self):
        """Test that class attributes are the same"""
        self.assertEqual(self.place.__class__.__name__, "Place")
        self.assertEqual(self.place.created_at, self.place.updated_at)

    def test_save(self):
        """Test that save method updates time"""
        old = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old, self.place.updated_at)


if __name__ == "__main__":
    unittest.main()
